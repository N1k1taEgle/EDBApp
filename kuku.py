from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class ExcelDB(MDApp):
    def build(self):
        return MDLabel(text="Hello,EDB", halign ="center")


ExcelDB().run()