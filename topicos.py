import sublime
import sublime_plugin


def settings():
    return sublime.load_settings('Topicos.sublime-settings')


def number_sep():
    sep = settings().get('number_separator')
    if settings().get('space_before_separator'):
        space_before = ' '
    if settings().get('space_after_separator'):
        space_after = ' '
    return "%s%s%s" % (space_before, sep, space_after)


def bullet_sep():
    return "%s " % (settings().get('bullet_char'),)


class NumberedListCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sep = number_sep()
        selections = self.view.sel()
        n = 0
        for selection in selections:
            offset = 0
            for line in self.view.lines(selection):
                n += 1
                offset += self.view.insert(edit,
                                           line.begin() + offset,
                                           str(n) + sep)


class BulletListCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        bullet = bullet_sep()
        selections = self.view.sel()
        for selection in selections:
            offset = 0
            for line in self.view.lines(selection):
                offset += self.view.insert(edit,
                                           line.begin() + offset,
                                           bullet)
