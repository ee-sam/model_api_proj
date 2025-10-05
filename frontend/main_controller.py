from PySide6.QtCore import QObject

class MainController(QObject):
    def __init__(self, view, model):
        self.main_view = view
        self.main_model = model
        self.connect_signals()

    def connect_signals(self):
        self.main_view.pushButton_Summarize.clicked.connect(self.handle_summarize)
        self.main_view.pushButton_Save.clicked.connect(self.handle_save)

    def handle_summarize(self):
        input_text = self.main_view.get_input_text()
        summary = self.main_model.summarize(input_text)
        self.main_view.set_output_text(summary)

    def handle_save(self):
        output_text = self.main_view.textEdit_Output.toPlainText()
        self.main_model.save_output(output_text)