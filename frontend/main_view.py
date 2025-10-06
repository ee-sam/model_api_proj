from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from main_view_ui import Ui_MainWindow

# View wrapper
class MainView(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.textEdit_Output.setReadOnly(True)

    def get_input_text(self):
        return self.textEdit_Input.toPlainText()
    
    def set_output_text(self, text):
        self.textEdit_Output.setPlainText(text)

    def update_label_progress_text(self, msg: str):
        self.label_Progress.setText(msg)

    def get_save_path(self):
        save_path, _ = QFileDialog.getSaveFileName(
            self,
            caption = "Save Summary",
            dir = "summary.txt",
            filter = "Text Files (*.txt);;All Files (*)"
        )
        return save_path
    
    def show_message(self, title, text):
        QMessageBox.information(self, title, text)