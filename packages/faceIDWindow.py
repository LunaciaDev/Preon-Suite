from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import QImage, QPixmap

from packages.ui.faceIDWindowClass import Ui_faceIDWindow

class FaceIDWindow(QWidget):
    cancelRegistration = Signal()

    def __init__(self):
        super(FaceIDWindow, self).__init__()
        self.ui = Ui_faceIDWindow()
        self.ui.setupUi(self)

        self.ui.cancelButton.clicked.connect(self.onCancelButtonClicked)

    @Slot(QImage)
    def setLoginCameraFeed(self, image):
        self.ui.faceIDCameraFeed.setPixmap(QPixmap.fromImage(image))

    @Slot()
    def onCancelButtonClicked(self):
        self.cancelRegistration.emit()
    
    @Slot()
    def onFinishRegistration(self):
        self.ui.cancelButton.setText("Return")
        self.ui.infoLabel.setText("Registration complete. You can now return.")