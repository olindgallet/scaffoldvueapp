# About scaffoldvueapp.py

`scaffoldvueapp.py` is a script for creating file folders (images, video, etc.) and downloading commonly used files for web apps.  For my use case this is Bootstrap and Grunt.

In addition, I wanted to try using the plumbum library for Python.  In the future I want to continue making scripts for Linux to make tasks easier.

# Installing scaffoldvueapp.py in Linux

1.  Open a terminal then navigate to your download folder.
2.  Run `wget -4 https://raw.githubusercontent.com/olindgallet/scaffoldvueapp/master/scaffoldvueapp.py` to download the file.
3.  Run `chmod +x scaffoldvueapp.py` to make the file executable.
4.  Run `sudo mv scaffoldvueapp.py /usr/bin/scaffoldvueapp`.  This moves the script into the `/usr/bin/` folder so that users can use the script from the command line.  If you want to install it for only the local user, use `/usr/local/bin` instead.
5.  Verify that the file has moved by typing `scaffoldvueapp help`.  If successful, then the script will run and display some help text.

# Using scaffoldvueapp.py

1.  Open a terminal and navigate to your work folder.
2.  Run `npm init vue@3` and follow the prompts.  This will create a directory for your Vue app.
3.  Run `cd <project-name>` to change directory into the app.
4.  Run `npm install` to download requisite files for the Vue app.
5.  Run `scaffoldvueapp`.
