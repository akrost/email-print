import imaplib
import email


class Mail:
    """
    Class that handles all communication with mail
    """
    def __init__(self, username, password, server="imap.gmail.com", port=993):
        """
        Opens a connection and selects the default folder
        :param username: Mail username (e-mail address)
        :param password: Mail password
        :param server: IMAP server
        :param port: IMAP port
        """
        self.username = username
        self.password = password
        self.server = server
        self.port = port

        self.imap = self._open_connection()
        self.select()

    def _open_connection(self):
        """
        Opens a IMAP4 SSL connection and logs in.
        :return: Connection object
        """
        imap = imaplib.IMAP4_SSL(self.server, self.port)
        imap.login(self.username, self.password)
        return imap

    def select(self, folder=""):
        """
        Selects a given folder
        :param folder: Folder to select
        :return: IMAP response
        """
        if folder != "":
            return self.imap.select(folder)
        else:
            return self.imap.select()

    def close(self):
        """
        Closes and logs out connection
        :return: None
        """
        self.imap.close()
        self.imap.logout()

    def get_all_messages(self):
        """
        Gets all messages from the currently selected folder.
        :return: List of message UIDs
        """
        try:
            result, data = self.imap.uid("search", None, "ALL")
            if result == "OK":
                return data[0].split()
        except Exception as e:
            pass
        return []

    def get_new_messages(self):
        """
        Gets all unread messages from the currently selected folder.
        :return: List of message UIDs
        """
        try:
            result, data = self.imap.uid("search", "(UNSEEN)")
            if result == "OK":
                return data[0].split()
        except Exception as e:
            pass
        return []

    def get_mail_by_uid(self, msg_uid):
        """
        Gets email from a given UID.
        :param msg_uid: UID of the message that should be retrieved
        :return: email object, or None if UID doesn't exist
        """
        result, data = self.imap.uid("fetch", msg_uid, "(RFC822)")
        if data[0]:
            raw_email = data[0][1].decode("utf-8")
            return email.message_from_string(raw_email)
        else:
            return None

    def delete_mail(self, msg_uid):
        """
        Deletes mail with the given UID.
        :param msg_uid: Message UID of the message that should be deleted
        :return: None
        """
        self.imap.store(msg_uid, '+FLAGS', '\\Deleted')
        self.imap.expunge()
