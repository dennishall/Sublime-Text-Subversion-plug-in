Sublime Text 2 Subversion plug-in
=================================

A very basic subversion plugin for the [Sublime Text 2](http://www.sublimetext.com/2) text editor, based on [burriko's plugin](https://github.com/burriko/sublime-subversion).

The aim is to provide a quick method to commit simple changes without leaving Sublime Text 2.  To this end the only subversion commands that are supported are:

* 'status', to check what will be commited
* 'update', to get the latest version of a file
* 'add', to add new files to the commit
* 'commit', to commit changes

Committing will show you a diff of your changes, and allow you to enter a single line of text for the commit message.


Usage
-----

 * Copy both files into your 'Sublime Text 2/Packages/User' folder which you should be able to find in your profile folder.
 * Make sure that you have the subversion command line client installed and that it's in your path.
 * All commands are accessed via keyboard shortcuts, which you can view/change by opening Default.sublime-keymap.


Known Issues
------------

Very occasionally Sublime Text 2 will freeze when generating the diff.  Killing the svn process (`ps -A | grep svn`, note the process id of svn (not grep!), and `kill -9 THE_PROCESS_ID#`) will bring Sublime Text 2 back to life.
