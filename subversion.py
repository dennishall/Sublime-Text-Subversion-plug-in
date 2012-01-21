import sublime, sublime_plugin, sys, os, subprocess, time

class SubversionCommand():
  args = ""

  def log(self, text, panel_name = 'svn'):
    # get_output_panel doesn't "get" the panel, it *creates* it,
    # so we should only call get_output_panel once
    if not hasattr(self, 'output_view'):
      self.output_view = self.window.get_output_panel(panel_name)
    v = self.output_view

    # Write this text to the output panel and display it
    edit = v.begin_edit()
    v.insert(edit, v.size(), text + '\n')
    v.end_edit(edit)
    v.show(v.size())

    self.window.run_command("show_panel", {"panel": "output." + panel_name})

  def get_path(self):
    if self.window.active_view():
      return self.window.active_view().file_name()
    elif self.window.folders():
      return self.window.folders()[0]
    else:
      sublime.error_message(__name__ + ': No place to run svn from')
      return False

  def run_svn(self, dir, svn_command):

    filename = self.window.active_view().file_name()

    # creates an output panel (clobbers any existing one - fine by me)
    self.window.get_output_panel("svn")

    # show the output panel (toggles it?)
    self.window.run_command("show_panel", {"panel": "output.svn"})

    def cancellation(param=None):
      self.log("SVN commit cancelled by user")
      self.window.run_command("close")
      # sleep long enough for the window to close ..
      #time.sleep(0.2)
      # .. then tell the user that the svn commit was cancelled.
      #sublime.error_message("SVN commit cancelled by user")

    def continuation(commit_message=""):
      if svn_command == "commit":
        self.args += " " + filename + " -m \"" + commit_message + "\""
      if svn_command == "add":
        self.args += " " + filename
      #self.log(" view name: " + str(self.window.active_view().id()))
      self.log("--- SVN ---")
      self.log(self.args)
      self.log(self.getOutputOfSysCommand(self.args, cwd=dir))

    try:
      if not dir:
        raise NotFoundError('The file open in the selected view has not yet been saved')

      self.args = "svn " + svn_command

      if svn_command == "commit":
        svn_diff = self.getOutputOfSysCommand("svn diff "+filename, cwd=dir)
        if(svn_diff == ""):
          self.log("No changes to commit")
        else:
          self.createWindowWithText(self.window.active_view(), svn_diff)
          self.window.show_input_panel("svn commit", "commit message goes here", continuation, None, cancellation)
      else:
        continuation()

    except (OSError) as (exception):
      self.log(str(exception))
      sublime.error_message(__name__ + ': svn error (?)')
    except (Exception) as (exception):
      sublime.error_message(__name__ + ': ' + str(exception))

  def getOutputOfSysCommand(self, commandText, cwd):
    p = subprocess.Popen(commandText, shell=True, bufsize=1024, stdout=subprocess.PIPE, cwd=cwd)
    p.wait()
    stdout = p.stdout
    return stdout.read()

  # Open a new buffer containing the given text
  def createWindowWithText(self, view, textToDisplay):
    new_view = self.window.new_file()
    edit = new_view.begin_edit()
    new_view.insert(edit, 0, textToDisplay)
    new_view.end_edit(edit)
    new_view.set_scratch(True)
    new_view.set_read_only(True)
    new_view.set_name("svn diff")
    new_view.set_syntax_file("Packages/Diff/Diff.tmLanguage")
    return new_view.id()



# svn status works at the DIRECTORY LEVEL
class SubversionStatusCommand(sublime_plugin.WindowCommand, SubversionCommand):
  #self.log('>> subversion status ... ')
  def run(self):
    path = self.get_path()
    if not path:
      return

    if os.path.isfile(path):
      path = os.path.dirname(path)

    self.run_svn(path, "status")


# svn update works at the DIRECTORY LEVEL
class SubversionUpdateCommand(sublime_plugin.WindowCommand, SubversionCommand):
  def run(self):
    #self.log('>> subversion update ... ')
    path = self.get_path()
    if not path:
      return

    if os.path.isfile(path):
      path = os.path.dirname(path)

    self.run_svn(path, "update")

# svn add works at the FILE LEVEL
class SubversionAddCommand(sublime_plugin.WindowCommand, SubversionCommand):
  #self.log('>> subversion add ... ')
  def run(self):
    path = self.get_path()
    if not path:
      return

    if os.path.isfile(path):
      path = os.path.dirname(path)

    self.run_svn(path, "add")

# svn commit works at the FILE LEVEL
class SubversionCommitCommand(sublime_plugin.WindowCommand, SubversionCommand):
  def run(self):
    #self.log('>> subversion commit ... ')
    path = self.get_path()
    if not path:
      return

    if os.path.isfile(path):
      path = os.path.dirname(path)

    self.run_svn(path, "commit")





