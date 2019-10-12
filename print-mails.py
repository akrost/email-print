import configparser
import mimetypes
import os

from mail import Mail
from printer import Printer
from utils import extract_mail_address_from_sender


def main():
    config = configparser.ConfigParser()
    script_directory = os.path.dirname(os.path.realpath(__file__))
    conf_file_path = os.path.join(script_directory, "email.config")
    config.read(conf_file_path)
    username = config.get("mail", "mail_address")
    passsword = config.get("mail", "mail_pw")
    imap_server = config.get("mail", "imap_server")
    imap_port = config.get("mail", "imap_port")

    mail = Mail(username, passsword, server=imap_server, port=imap_port)

    #all_messages_uids = gmail.get_all_messages()
    new_messages_uids = mail.get_new_messages()

    whitelist_sender = config.get("whitelist", "sender")
    whitelist_extensions = config.get("whitelist", "extensions")

    print_folder = config.get("printer", "print_folder")
    printer = Printer(print_folder)
    for msg_uid in new_messages_uids:
        # Get mail from server
        msg = mail.get_mail_by_uid(msg_uid)

        # Check if msg comes form whitelisted mail
        sender = extract_mail_address_from_sender(msg["From"])
        if sender not in whitelist_sender:
            # Delete message that is not from whitelisted sender
            mail.delete_mail(msg_uid)
            print("Email from {} was deleted. Sender not on whitelist".format(sender))
            continue

        # Check message for attachments
        for counter, part in enumerate(msg.walk()):
            content_type = part.get_content_type()
            print(content_type)
            if content_type == "application/x-pdf":
                ext = ".pdf"
            else:
                ext = mimetypes.guess_extension(content_type)

            # Check if extension is a whitelisted on
            if ext and ext in whitelist_extensions:
                print("The extension {} is whitelisted and therefor will be printed".format(ext))
                printer.print(file_name=part.get_filename(),
                              file_content=part.get_payload(decode=True))

    mail.close()


if __name__ == "__main__":
    main()

