# Thank you to OdatNurd for initial help with adding build variables

import sublime
import sublime_plugin
import os.path
import platform

from Default.exec import ExecCommand

class BuildVarSetup(ExecCommand):
    def run(self, **kwargs):
        # ---------------------------------------------
        # MODIFY VARS HERE to set custom locations/file names
        # Examples shown are Windows based, but MacOS/Linux paths are also supported

        # Folder containing Tickompiler
        # example: tk_loc = "C:/Users/Me/Projects/RHM/Tools/"
        tk_loc = ""

        # Folder containing base.bin
        # example: base_loc = "C:/Users/Me/Projects/RHM/Tools/"
        base_loc = ""      

        # Citra rhmm folder (you shouldn't won't need to change this, but you can)
        # example: citra_loc = "C:/Users/Me/AppData/Roaming/Citra/sdmc/rhmm/"
        citra_loc = "" 

        # Tickompiler and base.bin filenames (probably leave these alone)
        tk_name = "tickompiler.jar"
        base_name = "base.bin"
        # ---------------------------------------------

        # Find tickomplier (if not found in custom location)
        msg = ""
        if not os.path.exists(tk_loc + tk_name):
            tk_loc = os.path.expanduser("~/Desktop/RH_tools/")
            if not os.path.exists(tk_loc + tk_name):
                tk_loc = os.path.expanduser("~/Desktop/")
                if not os.path.exists(tk_loc + tk_name):
                    tk_loc = os.path.expanduser("~/Documents/RH_tools/")
                    if not os.path.exists(tk_loc + tk_name):
                        tk_loc = os.path.expanduser("~/Documents/")
                        if not os.path.exists(tk_loc + tk_name):
                            msg += "Couldn't find tickompiler, trying in same dir. as tickflow file\n"
                            tk_loc = ""

        # Find base.bin (looks in custom location or Tickompiler folder)
        if not os.path.exists(base_loc + base_name):
            base_loc = tk_loc
            if not os.path.exists(base_loc + base_name):
                msg += "Couldn't find base.bin, trying in same dir. as tickflow file\n"
                base_loc = ""
        
        base_loc += base_name
        tk_loc += tk_name

        # Find Citra rhmm folder (if not in custom location, checks default Windows and Mac/Linux install location)
        if not os.path.exists(citra_loc):
            citra_loc = os.path.expanduser("~/AppData/Roaming/Citra/sdmc/rhmm/")        # Windows
            if not os.path.exists(citra_loc):
                citra_loc = os.path.expanduser("~/.local/share/citra-emu/sdmc/rhmm/")   # macOS/Linux
                if not os.path.exists(citra_loc):
                    msg += "Couldn't find the Citra/rhmm folder\n"
        msg += "============================="

        # Fix some things if on Windows
        if platform.system() == "Windows":
            msg = msg.replace("\n","&& echo ")
            tk_loc = tk_loc.replace("/","\\")
            base_loc = base_loc.replace("/","\\")
            citra_loc = citra_loc.replace("/","\\")
        
        variables = {
            "tickompiler": tk_loc,
            "base_loc": base_loc,
            "citra_loc": citra_loc,
            "msg": msg
        }
        for key in ('shell_cmd', 'cmd', 'working_dir'):
            if key in kwargs:
                kwargs[key] = sublime.expand_variables(kwargs[key], variables)

        super().run(**kwargs)
