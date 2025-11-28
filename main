import sqlite3
import subprocess
import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QInputDialog

SCREEN_SIZE = [980, 900]


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 80, *SCREEN_SIZE)
        self.setWindowTitle('Отображение картинки')
        self.pixmap = QPixmap('203f4d56-7ecf-43a6-ad3d-62644c251578.jpg')
        self.image = QLabel(self)
        self.image.move(0, -50)
        self.image.resize(980, 1000)
        self.image.setPixmap(self.pixmap)
        self.button_1 = QPushButton(self)
        self.button_1.move(420, 330)
        self.button_1.resize(240, 40)
        self.button_1.setText("Войти")
        self.button_1.clicked.connect(self.sign)
        self.button_2 = QPushButton(self)
        self.button_2.move(420, 410)
        self.button_2.resize(240, 40)
        self.button_2.setText("Зарегистрироваться")
        self.button_2.clicked.connect(self.register)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def sign(self):
        con = sqlite3.connect("liquids_sort_puzzle_database.sqlite")
        cur = con.cursor()
        name, ok_pressed = QInputDialog.getText(self, "Логин",
                                                "Введите свой логин:")
        proverka = cur.execute(
            f"""SELECT id_player FROM liquids_sort_puzzle WHERE name = '{name}'""").fetchall()
        z = list(proverka)
        if not z:
            name, ok_pressed = QInputDialog.getText(self, "Логин",
                                                    f"Такого пользователя нет.\nВведите другой логин:")
            proverka = cur.execute(
                f"""SELECT id_player FROM liquids_sort_puzzle WHERE name = '{name}'""").fetchall()
            z = list(proverka)
        if z:
            if ok_pressed:
                con = sqlite3.connect("liquids_sort_puzzle_database.sqlite")
                cur = con.cursor()
                cur.execute(f"""UPDATE player SET id_player = '{z[0][0]}'""").fetchall()
                process = subprocess.Popen([sys.executable, "start_game.py"])
                con.commit()
                con.close()
                sys.exit(app.exec())
        else:
            ex = Example()
            ex.show()

    def register(self):
        con = sqlite3.connect("liquids_sort_puzzle_database.sqlite")
        cur = con.cursor()
        name, ok_pressed = QInputDialog.getText(self, "Логин",
                                                "Придумайте новый логин:")
        proverka = cur.execute(
            f"""SELECT EXISTS (SELECT 1 FROM liquids_sort_puzzle WHERE name = '{name}');""").fetchall()
        if int(proverka[0][0]) == 1:
            name, ok_pressed = QInputDialog.getText(self, "Логин",
                                                    f"Такой пользователь уже существует.\nПридумайте другой логин:")
            proverka = cur.execute(
                f"""SELECT EXISTS (SELECT 1 FROM liquids_sort_puzzle WHERE name = '{name}');""").fetchall()
        if int(proverka[0][0]) == 0:
            if ok_pressed:
                con = sqlite3.connect("liquids_sort_puzzle_database.sqlite")
                cur = con.cursor()
                res = cur.execute('''
                        SELECT id_player 
                        FROM liquids_sort_puzzle''').fetchall()
                now_id_player = list(max(res))
                res1 = cur.execute(f"""UPDATE player SET id_player = '{proverka[0][0]}'""").fetchall()
                cur.execute(f"""INSERT INTO liquids_sort_puzzle(id_player, name, level_number) 
                VALUES({int(now_id_player[0]) + 1}, '{name}', '0')""").fetchall()
                ex = Example()
                ex.show()
                con.commit()
                con.close()
        else:
            ex = Example()
            ex.show()

app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec())
