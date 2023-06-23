import os
import sys

from script import get_response, remove_model
from src.loadingLbl import LoadingLabel

# Get the absolute path of the current script file
script_path = os.path.abspath(__file__)

# Get the root directory by going up one level from the script directory
project_root = os.path.dirname(os.path.dirname(script_path))

sys.path.insert(0, project_root)
sys.path.insert(0, os.getcwd())  # Add the current directory as well

from PyQt5.QtCore import Qt, QCoreApplication, QThread, pyqtSignal, QTimer
from PyQt5.QtGui import QGuiApplication, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QFormLayout, QLineEdit, QVBoxLayout, QWidget, \
    QApplication, QTextBrowser, QFrame, QPushButton, QSpinBox, QLabel

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)  # HighDPI support
# qt version should be above 5.14
QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

QApplication.setFont(QFont('Arial', 12))

QApplication.setWindowIcon(QIcon('hf-logo.svg'))


class Thread(QThread):
    jobFinished = pyqtSignal(list)

    def __init__(self, num_beams, num_return_sequences, context):
        super().__init__()
        self.__num_beams = num_beams
        self.__num_return_sequences = num_return_sequences
        self.__context = context

    def run(self):
        resp = get_response(self.__num_beams, self.__num_return_sequences, self.__context)
        self.jobFinished.emit(resp)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__initVal()
        self.__initUi()

    def __initVal(self):
        self.__current_model_prefix = 'Selected Model:'
        self.__descriptionLbl_original_text = 'Loading'

    def __initUi(self):
        self.setWindowTitle('PyQt Pegasus-Paraphrase Model usage example')

        num_beams = 10
        num_return_sequences = 10
        context = "The ultimate test of your knowledge is your capacity to convey it to another."

        sep = QFrame()
        sep.setFrameShape(QFrame.HLine)
        sep.setFrameShadow(QFrame.Sunken)

        self.__numBeamsSpinBox = QSpinBox()
        self.__numBeamsSpinBox.setValue(num_beams)
        self.__numReturnSequences = QSpinBox()
        self.__numReturnSequences.setValue(num_return_sequences)
        self.__contextLineEdit = QLineEdit()
        self.__contextLineEdit.setText(context)

        self.__submitBtn = QPushButton('Submit')
        self.__submitBtn.clicked.connect(self.__submit)

        self.__answerBrowser = QTextBrowser()
        self.__answerBrowser.setPlaceholderText('Result will be generated in here')

        lay = QFormLayout()
        lay.addRow('Beams', self.__numBeamsSpinBox)
        lay.addRow('Return Sequences', self.__numReturnSequences)
        lay.addRow('Context', self.__contextLineEdit)
        lay.setContentsMargins(0, 0, 0, 0)

        paramWidget = QWidget()
        paramWidget.setLayout(lay)

        self.__descriptionLbl = LoadingLabel()

        lay = QVBoxLayout()
        lay.addWidget(paramWidget)
        lay.addWidget(self.__submitBtn)
        lay.addWidget(self.__descriptionLbl)
        lay.addWidget(self.__answerBrowser)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)
        self.setCentralWidget(mainWidget)

        self.resize(640, 400)

    def __submit(self):
        self.__t = Thread(self.__numBeamsSpinBox.value(), self.__numReturnSequences.value(), self.__contextLineEdit.text())
        self.__t.start()
        self.__t.jobFinished.connect(self.__setAnswerBrowserText)

        self.__descriptionLbl.start()
        self.__submitBtn.setEnabled(False)

    def __setAnswerBrowserText(self, paraphrase_lst: list):
        self.__answerBrowser.setText('\n'.join(paraphrase_lst))

        self.__descriptionLbl.stop()
        self.__submitBtn.setEnabled(True)

    def __removeModel(self):
        remove_model()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

