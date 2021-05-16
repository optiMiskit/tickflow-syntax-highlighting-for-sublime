# Plugin to disable word completion 
# Written by the Sublime Text community

import sublime
import sublime_plugin

class SampleListener(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        return ([], sublime.INHIBIT_WORD_COMPLETIONS)