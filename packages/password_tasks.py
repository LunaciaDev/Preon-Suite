import keyring as kr
from PySide6.QtCore import Slot

class password_tasks:
    def __init__(self):
        pass
    
    @Slot(str, str)
    def login(username, password):
        stored_password = kr.get_password("system", username)
        if stored_password is None or password != stored_password:
            print("Incorrect Username or Password") 
            return False
        else:
            print("Login completed") 
            return True

    @Slot(str, str)            
    def register(username, password):
        #TODO: Make the user double check password
        kr.set_password("system", username, password)


    # def passreset():
