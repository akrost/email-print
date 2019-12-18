import re
import datetime


def extract_mail_address_from_sender(sender):
    """
    Extracts the mail address from a sender string like "John Doe <john-doe@gmail2.com>" or "john-doe@gmail.com"
    :param sender: sender string
    :return: email address
    """
    if is_valid_email(sender):
        return sender
    else:
        pattern = r"<(.+?)>"
        if re.search(pattern, sender):
            address = re.search(pattern, sender).group(1)
            if is_valid_email(address):
                return address

    return "no email found"


def format_filename(filename):
    """
    Add the current date and time to the given filename and remove whitespaces.
    :param filename: Filename, e.g. "My Invoice.pdf"
    :return: New filename, e.g. "20190928_20:18:56_My_Invoice.pdf
    """
    date_and_time = datetime.datetime.now().strftime("%Y%m%d_%H:%M:%S")
    new_file_name = "_".join([date_and_time, filename])
    new_file_name = new_file_name.replace(" ", "_")
    return new_file_name


def is_valid_email(email):
    """
    Checks if a string is a valid email address. Returns True if string is valid email, returns False otherwise
    :param email: email address to check
    :return: True if valid, False otherwise
    """
    pattern = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"

    if re.search(pattern, email):
        return True
    else:
        return False
