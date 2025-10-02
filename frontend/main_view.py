from PySide6.QtWidgets import QMainWindow
from main_view_ui import Ui_MainWindow

# View wrapper
class MainView(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def get_input_txt(self):
        return self.textEdit_Input.toPlainText()
    
    def set_output_txt(self, text):
        self.textEdit_Output.setPlainText(text)



