import keyring as kr
from PySide6.QtCore import Slot, Signal, QObject

class password_tasks(QObject):
    loginStatus = Signal(bool)
    registerStatus = Signal(bool)

    def __init__(self):
        super(password_tasks, self).__init__()
    
    @Slot(str, str)
    def login(self, username, password):
        stored_password = kr.get_password("system", username)
        
        if stored_password is None or password != stored_password:
            self.loginStatus.emit(False)
            return
        
        self.loginStatus.emit(True)

    @Slot(str, str)            
    def register(self, username, password):
        kr.set_password("system", username, password)
        self.registerStatus.emit(True)

