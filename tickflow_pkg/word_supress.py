# Plugin to disable word completion from the Sublime Text community

import sublime
import sublime_plugin

class SampleListener(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        # Apparently you have to return a completion now for some reason... what
        # For Sublime Text 3, change ["-----"] to []
        return (["-----"], sublime.INHIBIT_WORD_COMPLETIONS)