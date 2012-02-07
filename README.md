Sublime Text 2 Subversion Plug-in
=================================

A very basic subversion plugin for the [Sublime Text 2](http://www.sublimetext.com/2) text editor, based on [burriko's plugin](https://github.com/burriko/sublime-subversion).

The aim is to provide a quick method to commit simple changes without leaving Sublime Text 2.  To this end the only subversion commands that are supported are:

* 'status', to check what files have been modified
* 'update', to get the latest version of a file
* 'add', to add new files to the commit
* 'commit', to commit changes with a brief message

Committing will show you a colorized diff of your changes, and allow you to enter a single line of text for the commit message.

NOTE:
The commands 'status' and 'update' run at the FOLDER level of the current file, but 'add' and 'commit' only operate upon the current file.


Usage
-----
 
 * In Sublime Text 2, select Preferences > Browse Packages. A finder/explorer instance will open to "Packages". Open the "User" subfolder.
 * Copy `subversion.py` and `Default.sublime-keymap` into the `Sublime Text 2/Packages/User` folder that you opened in the previous step.
 * You may need to restart ST2 so that it will compile the .py file to a .pyc file.
 * All commands are accessed via keyboard shortcuts, which you can view/change by opening `Default.sublime-keymap`.


Prerequisites
-------------

 * A subversion *command line client* (not tortoise) installed and in your `path` (i.e., you can type `svn -h` in a command window and it lists the svn commands).


Known Issues
------------

Very occasionally Sublime Text 2 will freeze when generating the diff.  Killing the svn process (`ps -A | grep svn`, note the process id of svn (not grep!), and `kill -9 THE_PROCESS_ID#`) will bring Sublime Text 2 back to life.
