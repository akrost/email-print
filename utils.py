import re
import datetime


def extract_mail_address_from_sender(sender):
    """
    Extracts the mail address from a sender string like "John Doe <john-doe@gmail2.com>"
    :param sender: sender string
    :return: email address
    """
    pattern = "<(.+?)>"
    address = re.search(pattern, sender).group(1)
    return address


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
