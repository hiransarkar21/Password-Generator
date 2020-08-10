from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import random
import Passwords as auth_file

Font = QFont()
Font.setWordSpacing(3)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.window_configuration()
        self.user_interface()

    def window_configuration(self):

        self.setWindowTitle("Password Generator")
        self.setFixedWidth(650)
        self.setFixedHeight(600)
        self.setFont(Font)
        self.setWindowIcon(QIcon("D:\\AlgoTrading\\passwords_icon.png"))
    

    def user_interface(self):

        header_style = QLabel(self)
        header_style.move(0, 0)
        header_style.resize(650, 20)
        header_style.setStyleSheet("background-color: black; font-size: 18px;")

        saved_passwords_button = QPushButton(self)
        saved_passwords_button.setIcon(QIcon("D:\\AlgoTrading\\passwords_icon.png"))
        saved_passwords_button.move(600, 40)
        saved_passwords_button.setIconSize(QSize(32,32))
        saved_passwords_button.setStyleSheet("background-color: #f0f0f0; border: 0px medium;")
        saved_passwords_button.clicked.connect(self.show_saved_passwords)

        app_name = QLabel(self)
        app_name.setText("Password Generator")
        app_name.move(210, 120)
        app_name.setStyleSheet("color: black; font-size: 25px; font-weight: light;")

        self.site_name = QLineEdit(self)
        self.site_name.move(170, 230)
        self.site_name.setPlaceholderText("Name of the Site".center(33))
        self.site_name.resize(300, 45)
        self.site_name.setStyleSheet("background-color: white; border: 0px medium; border-radius: 5px; padding-left: 15px; padding-right: 15px; font-size: 18px;")

        self.password_length = QLineEdit(self)
        self.password_length.move(170, 300)
        self.password_length.setPlaceholderText("Password Length".center(33))
        self.password_length.resize(300, 45)
        self.password_length.setStyleSheet("background-color: white; border: 0px medium; border-radius: 5px; padding-left: 15px; padding-right: 15px; font-size: 18px;")

        self.get_password = QPushButton(self)
        self.get_password.setText("Get Password")
        self.get_password.move(250, 400)
        self.get_password.resize(150, 50)
        self.get_password.setStyleSheet("background-color: black; color: white; font-size: 18px; border: 0px medium; border-radius: 15px;")
        self.get_password.clicked.connect(self.send_password_request)

        self.footer_text = QLabel(self)
        self.footer_text.move(240, 530)
        self.footer_text.resize(400,40)
        self.footer_text.setStyleSheet("color: black; font-size: 18px;")
        

        self.timer = QTimer(self)
        self.timer.setInterval(5000)
        self.timer.timeout.connect(self.timerAction)
        
    
        bottom_style = QLabel(self)
        bottom_style.move(0, 580)
        bottom_style.resize(650, 20)
        bottom_style.setStyleSheet("background-color: black; font-size: 18px;")

    def show_saved_passwords(self):

        class Passwords(QWidget):
            def __init__(self):

                super().__init__()
                self.window_configuration()
                self.user_interface()

            def window_configuration(self):

                self.setFixedHeight(600)
                self.setFixedWidth(650)
                self.setFont(Font)
                self.setWindowTitle(" Saved Passwords ")
                self.setWindowIcon(QIcon("D:\\AlgoTrading\\passwords_icon.png"))

            def user_interface(self):

                text = QLabel("Saved Passwords", self)
                text.move(250, 50)
                text.setStyleSheet("color: black; font-size: 20px;font-weight: light;")
                self.saved_passwords = QTextEdit(self)
                self.saved_passwords.move(50, 130)
                self.saved_passwords.resize(550, 420)
                self.saved_passwords.setStyleSheet("border: 0px medium; border-radius: 7px; font-size: 18px;")
                self.saved_passwords.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.saved_passwords.setReadOnly(True)


                try:

                    data_file = open("C:\\Users\\Jay\\Desktop\\Password Generator\\Passwords.txt")

                except:

                    self.saved_passwords.setText("\n  No Passwords Saved ")

                else:

                    read_data = data_file.read()
                    self.saved_passwords.setText(read_data)


        self.saved_passwords_window = Passwords()
        self.saved_passwords_window.show()


    def send_password_request(self):

        site_name = self.site_name.text()
        password = str()

        for x in auth_file.passwords:
            if int(len(x)) == int(self.password_length.text()):
                password = x
                QApplication.clipboard().setText(password)
                break

            else:
                continue

        password_file = open("C:\\Users\\Jay\\Desktop\\Password Generator\\Passwords.txt", "a")
        position = password_file.tell()
        password_file.seek(position, 0)
        password_file.write("\n")
        password_file.write("  " + site_name + " : " + password)
        password_file.write("\n")
        password_file.close()

        self.get_password.setText("Copied")
        self.footer_text.setText("Application Exits in 5s")
        self.timer.start()

    def timerAction(self):

        #sys.exit()
        #self.timer.stop()
        pass
            
            
def main():

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

main()
