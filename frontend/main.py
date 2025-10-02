import sys
from PySide6.QtWidgets import QApplication
from main_view import MainView

def main():
    app = QApplication(sys.argv)
    view = MainView()
    # model = MainModel()
    # controller = MainController()

    view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()