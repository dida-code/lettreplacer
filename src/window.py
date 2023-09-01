# window.py
#
# Copyright 2023 dida-code
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from gi.repository import Gtk, Gio
from gi.repository import GdkPixbuf



@Gtk.Template(resource_path='/io/github/dida_code/lettreplacer/window.ui')
class LettreplacerWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'LettreplacerWindow'

    tekst = Gtk.Template.Child()
    button = Gtk.Template.Child()
    button_about = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)



        self.button.connect("clicked", self.printText)
        self.button_about.connect("clicked", self.prikazi_about)

    def printText(self, widget):

        replacements = {
        "æ": "ć",
        "Æ": "Ć",
        "": "ž",
        "": "Ž",
        "": "š",
        "": "Š",
        "è": "č",
        "È": "Č",
        "ð": "đ"
    }

        buffer = self.tekst.get_buffer()
        start_iter, end_iter = buffer.get_bounds()
        text = buffer.get_text(start_iter, end_iter, include_hidden_chars=True)

        for original, replacement in replacements.items():
            text = text.replace(original, replacement)

        buffer.set_text(text)

    def prikazi_about(self, widget):
        about = Gtk.AboutDialog()
        about.set_program_name("LettReplacer")
        about.set_version("0.1")
        about.set_authors(['Dimitrije Kocic'])
        about.set_comments("A small application for automatically changing certain letters in text")
        about.set_website("https://github.com/dida-code/lettreplacer.git")
        about.set_license_type(Gtk.License.GPL_3_0)
        logo_pixbuf = GdkPixbuf.Pixbuf.new_from_resource("/io/github/dida_code/lettreplacer/txt.png")
        about.set_logo(logo_pixbuf)
        about.run()
        about.destroy()

if __name__ == "__main__":
    win = LettreplacerWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
