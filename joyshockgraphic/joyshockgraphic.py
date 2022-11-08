import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("joyshockgraphic/resources/joyshockgraphic.ui", self)

        # Connect button groups
        self.bgInputGroups.buttonClicked.connect(self.switch_input)
        self.bgInputSettings.buttonClicked.connect(self.load_input)
        self.bgInputs.buttonClicked.connect(self.pick_bind)
        self.bgLibrary.buttonClicked.connect(self.handle_profile)

    def switch_input(self):
        pass

    def load_input(self):
        pass

    def pick_bind(self):
        pass

    def handle_profile(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
