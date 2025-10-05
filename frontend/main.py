import sys
from PySide6.QtWidgets import QApplication
from main_view import MainView
from main_model import MainModel
from main_controller import MainController

def main():
    app = QApplication(sys.argv)
    main_view = MainView()
    main_model = MainModel()
    main_controller = MainController(main_view, main_model)

    main_view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()