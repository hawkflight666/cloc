#!/usr/bin/python3
"""
Author : Mohammad Rehan
Email : rehan.mohd@gmail.com
Date : 18/04/2022

Python program is used to execute cloc on given
Github repository and send output through
email as an attachment
"""
import os
import smtplib
import platform
from email import encoders
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename


# Configurable parameters
github_url="http://github.com/example/example.git"
sender_email_addr="your_email@gmail.com"
sender_email_pass="password"
receiver_email_addr="receiver@gmail.com"
output_file = "ClocReport.txt"


def isplatform(plform):
    os_type = platform.system()
    if os_type==plform:
        return True
    else:
        return False

def download_git_repo():
    # Download repository from Git Public repo
    dirName = github_url.split('/')
    dirName = dirName[len(dirName) - 1].split('.')[0]
    if not os.path.exists(dirName):
        try:
            cloc_cmd = "git clone " + github_url
            os.system(cloc_cmd)
            print("Repository downlaod completed.")
        except OSError:
            print(f"Error in downloading git repository from {github_url}")
            exit(0)
    return dirName

# NOTE: To login and send email from this script from your gmail account please make 'Allow less secure apps' ON
# Go to the Less secure app access section of your Google Account. You might need to sign in.
# Turn Allow less secure apps off.
# If the two step verification is on, we cannot use the less secure access.
def login(email_address, email_pass, s):
    s.ehlo()
    # start TLS for security
    s.starttls()
    s.ehlo()
    # Authentication
    s.login(email_address, email_pass)
    print("login to email account.")

def send_mail():
    # The mail is sent using Python SMTP library.
    s = smtplib.SMTP("smtp.gmail.com", 587)
    print("Sending CLOC through email..")
    login(sender_email_addr, sender_email_pass, s)

    # message to be sent
    subject = "CLOC Report"
    message = EmailMessage()
    message = MIMEMultipart()
    mail_content = """
    Dear Receiver,
        Please find attached CLOC report herewith.
    
    With Regards 
    Mohammad Rehan"""

    # The subject line
    # The body and the attachments for the mail
    message['From'] = sender_email_addr
    message['To'] = receiver_email_addr
    message['Subject'] = subject

    message.attach(MIMEText(mail_content, 'plain'))
    attach_file = open(output_file, 'rb')  # Open the file as binary mode
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload)  # encode the attachment
    # add payload header with filename
    payload.add_header('Content-Disposition', "attachment; filename= %s" % basename(output_file))
    message.attach(payload)

    s.sendmail(sender_email_addr,receiver_email_addr,message.as_string())
    print("CLOC report send To " + receiver_email_addr)

    # terminating the session
    s.quit()
    print("Email sent.")

def run_cloc(github_dir):

    try:
        if isplatform('Windows'):
            print("Running CLOC on Windows..")
            cloc_cmd = "cloc-1.92.exe " + github_dir + "> " + output_file
            os.system(cloc_cmd)
        elif isplatform('Linux'):
            cloc_cmd = "cloc " + github_dir + "> " + output_file
            os.system(cloc_cmd)
        elif isplatform('Darwin'):
            # output = os.system('cloc-1.92.exe {github_dir}')
            print("Darwin not supported!")
        else:
            print("Os not supported!")
        #output_file = open(output_file, "r", encoding = "utf_8")
    except IOError:
        print("Error executing command : %s " % IOError.with_traceback())
    print("CLOC report generated..")
    #return output_file.read()

def main():
    # Download git repository on local machine
    dirName=download_git_repo()

    # Run CLOC to calculate loc
    run_cloc(dirName)

    # Send CLOC report through email
    send_mail()


if __name__ == "__main__":
    main()