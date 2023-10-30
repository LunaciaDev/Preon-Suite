import keyring as kr
from PySide6.QtCore import Slot, Signal, QObject

class password_tasks(QObject):
    loginStatus = Signal()

    def __init__(self):
        super(password_tasks, self).__init__()
    
    @Slot(str, str)
    def login(self, username, password):
        stored_password = kr.get_password("system", username)
        
        if stored_password is None or password != stored_password:
            self.loginStatus.emit(False, "Incorrect Username or Password")
            return
        
        self.loginStatus.emit(True, "")

    @Slot(str, str)            
    def register(username, password):
        #TODO: Make the user double check password
        kr.set_password("system", username, password)


