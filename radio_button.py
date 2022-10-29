print("Hello World")

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QCheckBox, QRadioButton, QLabel, QPushButton,QLineEdit


class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.radio_yazisi = QLabel("Hangi programlama dilini daha çok seviyorsun ?")
        self.java = QRadioButton("Java")                #####################
        self.python = QRadioButton("Python")            #####################
        self.php = QRadioButton("Php")                  #####################

        self.yazi_alanı = QLabel("")
        self.button = QPushButton("Gönder")

        v_box = QVBoxLayout()
        v_box.addWidget(self.radio_yazisi)
        v_box.addWidget(self.java)
        v_box.addWidget(self.python)
        v_box.addWidget(self.php)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alanı)
        v_box.addWidget(self.button)

        self.setLayout(v_box)

        self.setWindowTitle("Survey")

        self.show()

        self.button.clicked.connect(lambda: self.click(self.java.isChecked(), self.python.isChecked(),self.php.isChecked()))
                        ##burda lambda kullanıyoruz çünkü normalde connnect in içine bir fonksiyon objesi gireriz. (self.function_name)
                        ###############                                              bir fonksiyon değil (self.function_name())


    def click(self,java, python, php):
        if java:
            self.yazi_alanı.setText("En sevdiğin Programlama Dili Java <3 <3")

        elif python:
            self.yazi_alanı.setText("En sevdiğin Programlama Dili Python <3 <3")

        elif php:
            self.yazi_alanı.setText("En sevdiğin Programlama Dili Php <3 <3")













app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())