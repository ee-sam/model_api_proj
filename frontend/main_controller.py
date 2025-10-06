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
        if not input_text.strip():
            self.main_view.update_label_progress_text("Please enter some text")
            return
        else:
            self.main_view.update_label_progress_text("Connecting to API")
        result = self.main_model.summarize(input_text)
        if "error" in result:
            self.main_view.set_output_text(result["error"])
            self.main_view.update_label_progress_text("ERROR: Failed to summarize")
        else:
            self.main_view.set_output_text(result["summary"])
            self.main_view.update_label_progress_text(f'INFO: Summarized from original {result["original_length"]} words to summary {result["summary_length"]} words')

    def handle_save(self):
        output_text = self.main_view.textEdit_Output.toPlainText()
        if not output_text.strip():
            self.main_view.update_label_progress_text("")
            return
        else:
            save_path = self.main_view.get_save_path()
        if not save_path:
            self.main_view.update_label_progress_text("ERROR: Save path is empty")
            return
        try:
            self.main_model.save_output(output_text, save_path)
            self.main_view.update_label_progress_text(f"Saved to {save_path}")
            self.main_view.show_message("SUCCESS", f"Summary saved to:\n{save_path}")
        except Exception as e:
            self.main_model.save_output("ERROR", f"Failed to save: {e}")