# CLOCResultsMailer
A simple Python script that downloads a user-provided GitHub repo link, runs it against CLOC (count lines of code) and emails the results to a provided address. 

# Requirements prior to running this script

**This script requires the following:**

1. Python 3.1 or higher.
2. Pip installed and accessible to Python (*primary emphasis on windows, see below*).
3. Git installed and accessible to Python (*again... windows emphasis... see below*).
4. The CLOC program is downloaded/installed and accessible in the directory that you will run the script (further details below).



## Script assumptions

This script assumes that you are currently working/executing out of the folder where the script is located and CLOC is accessible.

** This script also utilizes Gmail specifically for the SMTP implementation ***

# Installing CLOC



## Unix/Linux-based operating systems

*Main link*: http://cloc.sourceforge.net/

The instructions on the main page provide multiple methods of downloading/installing CLOC on the system of your choice

## Windows-based operating systems 

For windows, it will be easier to use the following link to download a simple executable file version (which the script implements):

https://sourceforge.net/projects/cloc/

# Installing Python

Since there are far more comprehensive guides for each OS, you can use this guide for installing python:

https://realpython.com/installing-python/

### LINUX USERS

Depending on how Python was installed, you may need to run a certificate command file for the SMTP mail functions to work properly. For example, I installed Python directly from the main Python website, which included a file called ```Install certificates.commmand```. This would be as simple as double clicking the command file to run it.

### WINDOWS USERS

In the guide, they outline a few methods, however **I would highly advise going with the microsoft store method for simplicity!**

# Installing pip

Pip will be needed for a package that will be installed below. To install pip, you can execute the following command:

```
python3 -m pip install gitpython
```

If on Linux, you may need to append ```sudo``` to the beggining of the command (depending on how python was installed). If using this method, there may be a warning that pip needs to be updated, in which the warning will give instructions.


There are also alternative methods of installing pip in the following resource article:

https://monovm.com/blog/how-to-install-pip-on-windows-linux/


# Installing git

Now you will require git to actually download the repo. You can use the following guide that includes linux and windows methods of installation:

https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

### Windows may require the PATH environment variable to properly function

If this is the case, you can follow this guide for adding environment variables:

https://kb.wisc.edu/cae/page.php?id=24500

Where ```Variable``` will be ```GIT_PYTHON_GIT_EXECUTABLE``` and ```Value``` will be the directory where the git.exe file is located. For example, my installation pointed to:

```C:\Program Files\Git\cmd\git.exe```

For a quick and temporary solution to this issue, you can set the path directly in command prompt with the following command:

```set GIT_PYTHON_GIT_EXECUTABLE=C:\Program Files\Git\cmd\git.exe```

# Minor configuration changes for the script

The script will require a Gmail account to send the email on behalf of. The lines of code to edit will be the following:

```
sender = 
password =
```
Please keep in mind that you will need to modify your account security settings to allow 3rd party applications access the account:

https://support.google.com/accounts/answer/6010255

# Executing the script

At this point, you should have all the necessary dependencies to run the script. From here, you will just need to move into the directory where CLOC and the script are located (Linux users should be able to execute the ```cloc``` command from anywhere) and run the python script using the following:

 **```python3 CLOCResultsMailer.py```**
 
 # Final notes
 
 I am well aware that this is a far cry from a properly secured implementation of this script, this is just for demonstration .
