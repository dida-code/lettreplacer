# window.py
#
# Copyright 2024 dida-code
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


from gi.repository import Gtk, Gdk, Gio, GLib, Pango
from gi.repository import GdkPixbuf
import chardet


@Gtk.Template(resource_path='/io/github/dida_code/lettreplacer/window.ui')
class LettreplacerWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'LettreplacerWindow'

    tekst = Gtk.Template.Child()
    button = Gtk.Template.Child()
    button_about = Gtk.Template.Child()
    cirilica = Gtk.Template.Child()
    latinica = Gtk.Template.Child()
    quit = Gtk.Template.Child()
    help = Gtk.Template.Child()
    podesavanje = Gtk.Template.Child()
    file = Gtk.Template.Child()
    snimi = Gtk.Template.Child()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.file_path = None
                        
        global velicina_font
        velicina_font = "DejaVu Sans 14"
        self.tekst.override_font(Pango.FontDescription(velicina_font))

        self.button.connect("clicked", self.printText)
        self.button_about.connect("activate", self.prikazi_about)
        self.latinica.connect("clicked", self.printLatinica)
        self.cirilica.connect("clicked", self.printCirilica)
        self.quit.connect("activate", self.turn_off)
        self.help.connect("activate", self.prikazi_help)
        self.podesavanje.connect("activate", self.prikazi_podesavanje)
        self.file.connect("activate", self.file_choser)
        self.snimi.connect("clicked", self.snimi_promene)
                
    def printText(self, widget):
        replacements = {"æ":"ć","Æ":"Ć","":"ž","":"Ž","":"š","":"Š","è":"č","È":"Č","ð":"đ"}

        buffer = self.tekst.get_buffer()
        start_iter, end_iter = buffer.get_bounds()
        text = buffer.get_text(start_iter, end_iter, include_hidden_chars=True)

        for original, replacement in replacements.items():
            text = text.replace(original, replacement)

        buffer.set_text(text)

    def printCirilica(self, widget):
        replacements = {"Dj":"Ђ","dj":"ђ","Lj":"Љ","lj":"љ","Nj":"Њ","nj":"њ","Dž":"Џ","dž":"џ","B":"Б","b":"б","V":"В","v":"в","G":"Г","g":"г","D":"Д","d":"д","t":"т","Đ":"Ђ","đ":"ђ","Ž":"Ж","ž":"ж","Z":"З","z":"з","I":"И","i":"и","L":"Л","l":"л","N":"Н","n":"н","P":"П","p":"п","R":"Р","r":"р","S":"С","s":"с","Ć":"Ћ","ć":"ћ","U":"У","u":"у","F":"Ф","f":"ф","H":"Х","h":"х","C":"Ц","c":"ц","Č":"Ч","č":"ч","Š":"Ш","š":"ш"}

        buffer = self.tekst.get_buffer()
        start_iter, end_iter = buffer.get_bounds()
        text = buffer.get_text(start_iter, end_iter, include_hidden_chars=True)

        for original, replacement in replacements.items():
            text = text.replace(original, replacement)

        buffer.set_text(text)

    def printLatinica(self, widget):
        replacements = {"Љ":"Lj","љ":"lj","Њ":"Nj","њ":"nj","Џ":"Dž","џ":"dž","Б":"B","б":"b","В":"V","в":"v","Г":"G","г":"g","Д":"D","д":"d","т":"t","Ђ":"Đ","ђ":"đ","Ж":"Ž","ж":"ž","З":"Z","з":"z","И":"I","и":"i","Л":"L","л":"l","Н":"N","н":"n","П":"P","п":"p","Р":"R","р":"r","С":"S","с":"s","Ћ":"Ć","ћ":"ć","У":"U","у":"u","Ф":"F","ф":"f","Х":"H","х":"h","Ц":"C","ц":"c","Ч":"Č","ч":"č","Ш":"Š","ш":"š"}

        buffer = self.tekst.get_buffer()
        start_iter, end_iter = buffer.get_bounds()
        text = buffer.get_text(start_iter, end_iter, include_hidden_chars=True)

        for original, replacement in replacements.items():
            text = text.replace(original, replacement)

        buffer.set_text(text)

    def prikazi_about(self, widget):
        about = Gtk.AboutDialog()
        about.set_program_name("LettReplacer")
        about.set_version("v1.3.1")
        about.set_authors(['Dimitrije Kocic'])
        about.set_comments("A small application for automatically changing certain letters in text")
        about.set_website("https://github.com/dida-code/lettreplacer.git")
        about.set_license_type(Gtk.License.GPL_3_0)
        logo_pixbuf = GdkPixbuf.Pixbuf.new_from_resource("/io/github/dida_code/lettreplacer/txt.png")
        about.set_logo(logo_pixbuf)
        about.run()
        about.destroy()
          
    def prikazi_help(self, widget):
        print("pomoc")
        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text="Pomoć za korišćenje aplikacije",
            )

        dialog.format_secondary_text("""
        Dugme  Ispravi koristi se za ispravku slova:æ, Æ, , , , , è, È, ð
            Dugme Na ćirilicu i dugme Na latinicu automatski menja
            tekst sa ćirilice na latinicu i obrnuto."""
            )
        dialog.run()
        dialog.destroy()
                
    def turn_off(self,widget):
        self.destroy()
        
    def prikazi_podesavanje(self, widget):
        dialog = Gtk.FontChooserDialog(title="Izaberite Font", transient_for=self, flags=0)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            velicina_font = dialog.get_font()
            print("Izabrani font:", velicina_font)
            self.tekst.override_font(Pango.FontDescription(velicina_font))
        elif response == Gtk.ResponseType.CANCEL:
            print("Izbor otkazan")

        dialog.destroy()
        
    def file_choser(self, widget):
        dialog = Gtk.FileChooserDialog(
            title="Please choose a file", parent=self, action=Gtk.FileChooserAction.OPEN
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN,
            Gtk.ResponseType.OK,
        )
        self.add_filters(dialog)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
            self.file_path = dialog.get_filename()  # Sačuvaj putanju fajla

        # Otvori fajl u binarnom modu i detektuj kodiranje
            with open(self.file_path, 'rb') as file:
                raw_data = file.read()
                result = chardet.detect(raw_data)
                encoding = result['encoding']
                print(f"Detected encoding: {encoding}")

        # Ponovno otvori fajl sa detektovanim kodiranjem
            with open(self.file_path, 'r', encoding=encoding) as file:
                file_content = file.read()
                self.tekst.get_buffer().set_text(file_content)
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
        dialog.destroy()
        
    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        dialog.add_filter(filter_any)

    def on_folder_clicked(self, widget):
        dialog = Gtk.FileChooserDialog(
            title="Please choose a folder",
            parent=self,
            action=Gtk.FileChooserAction.SELECT_FOLDER,
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK
        )
        dialog.set_default_size(800, 400)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Select clicked")
            print("Folder selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
        dialog.destroy()

    def snimi_promene(self, widget):
        if self.file_path:
            buffer = self.tekst.get_buffer()
            start_iter, end_iter = buffer.get_bounds()
            text = buffer.get_text(start_iter, end_iter, include_hidden_chars=True)
            with open(self.file_path, 'w', encoding='utf-8') as file:
                file.write(text)
            print(f"File saved: {self.file_path}")
        else:
            # If file_path is not set, prompt the user with a Save As dialog
            dialog = Gtk.FileChooserDialog(
                title="Save As",
                parent=self,
                action=Gtk.FileChooserAction.SAVE,
            )
            dialog.add_buttons(
                Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                Gtk.STOCK_SAVE, Gtk.ResponseType.OK
            )

            # Set a default filename
            dialog.set_current_name("untitled.txt")

            # Add filters
            filter_text = Gtk.FileFilter()
            filter_text.set_name("Text files")
            filter_text.add_mime_type("text/plain")
            dialog.add_filter(filter_text)

            filter_all = Gtk.FileFilter()
            filter_all.set_name("All files")
            dialog.add_filter(filter_all)

            response = dialog.run()
            if response == Gtk.ResponseType.OK:
                self.file_path = dialog.get_filename()
                print(f"Saving file to: {self.file_path}")

                # Get text from the TextView widget
                buffer = self.tekst.get_buffer()
                start_iter, end_iter = buffer.get_bounds()
                text = buffer.get_text(start_iter, end_iter, include_hidden_chars=True)

                # Save the text to the file
                with open(self.file_path, 'w', encoding='utf-8') as file:
                    file.write(text)
                print("File saved successfully.")
            elif response == Gtk.ResponseType.CANCEL:
                print("Save operation cancelled.")

            dialog.destroy()
                            
if __name__ == "__main__":
    win = LettreplacerWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
