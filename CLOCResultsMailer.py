import git
import subprocess
import smtplib
import ssl
import platform

# Request for the github repo to download.
GitURL = input("Please enter the GitHub repository link: ")

# Request for the recipient email address.
recip = input("Please enter the recipient email address: ")

name = input("Please provide a name for the new folder(without any spaces or invalid file characters): ")


# This is where you would define the email address you would use
# to send the email using the SMTP library in Python. Normally you
# would use something like a config file and import it for security,
# however I kept it like this for simplicity.

# Email account and password to be used to send the results to the recipient.
# This implementation requires gmail.
# The gmail account must also have the 3rd party email sending allowed
sender = "someaccount@gmail.com"
password = "Thisisatest123"

# this is just to pre-initialize the variables as it seems setting them
# in an if-else statement does not instantiate them.
Results = ""



# This if-else block checks the operating system type, downloads the repo and
# runs it through CLOC

# 1. If it's windows, then it set's the path accordingly and doesn't include the
#    shell portion (in running CLOC) since it's executing a .exe file.

# 2. For everything else, I have it to auto-assume it's shell and accomodates
#    accordingly.

# 3. After the repo is downloaded with the correct path, then it kicks off
#    subprocess to run CLOC against the repo within the OS and then saves
#    the results.
if (platform.system() == 'Windows'):
   Path = name
   print("\n\nDownloading repo...")
   git.Repo.clone_from(GitURL, Path)
   print("\n\n Complete. Now running CLOC against the repo...")
   Results = subprocess.getoutput("cloc.exe " + Path)
else:
    Path = "./"+name
    print("Downloading repo...")
    git.Repo.clone_from(GitURL, Path)
    print("\n\n Complete. Now running CLOC against the repo...")
    Results = subprocess.check_output(['cloc ' + Path], shell=True)


# The following is a generic implementation from the SMTP lib in python
# for sending an email

print("\n\n Complete. Now sending the email...")
port = 465  # SSL port for SMTP
smtp_server = "smtp.gmail.com" # SMTP server being used

# Default implementation of sending an email via gmail and python.
# Numerous examples are online.
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context = context) as server:
    server.login(sender, password)
    server.sendmail(sender, recip, Results)


print("\n\n Script complete.")

