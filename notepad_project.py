
import os
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QFileDialog

from PyQt5.QtWidgets import QAction,qApp, QMainWindow



class NotePad(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()


    def init_ui(self):

        self.yazi_alanı = QTextEdit()
        self.temizle = QPushButton("Temizle")
        self.ac = QPushButton("Aç")
        self.kaydet = QPushButton("Kaydet")

        h_box = QHBoxLayout()

        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)

        h_box.addStretch()


        v_box = QVBoxLayout()
        v_box.addWidget(self.yazi_alanı)
        v_box.addLayout(h_box)


        self.setLayout(v_box)

        self.setWindowTitle("NotePad")


        self.temizle.clicked.connect(self.yaziyi_temizle)
        self.ac.clicked.connect(self.dosya_ac)
        self.kaydet.clicked.connect(self.dosya_kaydet)
        self.show()



    def yaziyi_temizle(self):
            self.yazi_alanı.clear()


    def dosya_ac(self):
        dosya_ismi = QFileDialog.getOpenFileName(self, "Dosya Aç", os.getenv("Desktop"))              #os.getenv("Desktop") da yazabilirsin
        with open(dosya_ismi[0], "r") as file:
            self.yazi_alanı.setText(file.read())


    def dosya_kaydet(self):
        dosya_ismi = QFileDialog.getSaveFileName(self, "Dosya Kaydet", os.getenv("Desktop"))
        with open(dosya_ismi[0], "w") as file:
            file.write(self.yazi_alanı.toPlainText())


class Menu(QMainWindow):


    def __init__(self):
        super().__init__()






app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())