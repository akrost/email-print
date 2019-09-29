# E-Mail Printer
Turn a regular printer into a network printer that prints attachments of emails using a Raspberry Pi.

## Usage

### Hardware Setup
Connect your Raspberry Pi (or any other Unix based computer) to the internet and plug in your printer.

### Download Code
Clone repository
```shell script
git clone https://github.com/akrost/email-print.git
```

### Run Script Regularly
To create a cron job run
```shell script
crontab -e
```

Add a new line at the end of the file:
```shell script
*/5 * * * * /path/to/python3 /path/to/project/print-mails.py
```
This will check your mail account every 5 minutes for new mails and print them.


## How it works
This script connects to your mail account, and fetches all unread messages.
If the email comes from a whitelisted mail address and contains a whitelisted attachment,
the file will be printed with your default printer.


## Note
* Use a dedicated e-mail address for your printer.
* The script was only tested with Gmail, but may also work with other IMAP capable
* The script was only tested with PDFs, but should also work with other mimetypes.
* Use a Raspberry Pi that is connected to the internet and a printer (set up a cronjob)
