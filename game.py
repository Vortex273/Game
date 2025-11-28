import random
import sqlite3
import subprocess
import sys

from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QPixmap, QPainter, QColor
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout

picture = ["6fb53e16-7b8e-4431-ae44-053b0b9abc42-fotor-20251123349512.jpg",
           "6fb53e16-7b8e-4431-ae44-053b0b9abc42-fotor-2025112334956.png"]
color = ["#1f77b4", "#ff7f0e", "#2ca02c", "#9467bd", "#8c564b", "#bcbd22", "#1f77b4", "#1f77b4", "#1f77b4", "#ff7f0e",
         "#ff7f0e", "#ff7f0e", "#2ca02c", "#2ca02c", "#2ca02c", "#9467bd", "#9467bd", "#9467bd", "#8c564b", "#8c564b",
         "#8c564b", "#bcbd22", "#bcbd22", "#bcbd22"]
VESSEL = [[], [], [], [], [], [], ["#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"],
          ["#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"]]
for i in range(6):
    q = ""
    num = 0
    for y in range(4):
        z = random.choice(color)
        color.remove(z)
        if q == z:
            num += 1
            VESSEL[i].append(z)
        else:
            q = z
            VESSEL[i].append(z)
    if num == 4:
        r = random.choice(color)
        while r == VESSEL[i][0]:
            r = random.choice(color)
        VESSEL[i][0] = r


class ImageOverlayApp(QWidget):
    def __init__(self):
        super().__init__()
        self.hod_num = 0
        self.last_bottle = []
        self.before_bottle = []
        self.last_color = []
        self.before_color = []
        self.color_cube0 = VESSEL[0][0]
        self.color_cube1 = VESSEL[0][1]
        self.color_cube2 = VESSEL[0][2]
        self.color_cube3 = VESSEL[0][3]
        self.color_cube4 = VESSEL[1][0]
        self.color_cube5 = VESSEL[1][1]
        self.color_cube6 = VESSEL[1][2]
        self.color_cube7 = VESSEL[1][3]
        self.color_cube8 = VESSEL[2][0]
        self.color_cube9 = VESSEL[2][1]
        self.color_cube10 = VESSEL[2][2]
        self.color_cube11 = VESSEL[2][3]
        self.color_cube12 = VESSEL[3][0]
        self.color_cube13 = VESSEL[3][1]
        self.color_cube14 = VESSEL[3][2]
        self.color_cube15 = VESSEL[3][3]
        self.color_cube16 = VESSEL[4][0]
        self.color_cube17 = VESSEL[4][1]
        self.color_cube18 = VESSEL[4][2]
        self.color_cube19 = VESSEL[4][3]
        self.color_cube20 = VESSEL[5][0]
        self.color_cube21 = VESSEL[5][1]
        self.color_cube22 = VESSEL[5][2]
        self.color_cube23 = VESSEL[5][3]
        self.color_cube24 = VESSEL[6][0]
        self.color_cube25 = VESSEL[6][1]
        self.color_cube26 = VESSEL[6][2]
        self.color_cube27 = VESSEL[6][3]
        self.color_cube28 = VESSEL[7][0]
        self.color_cube29 = VESSEL[7][1]
        self.color_cube30 = VESSEL[7][2]
        self.color_cube31 = VESSEL[7][3]
        self.color_square_rect0 = QRect(76, 235, 106, 80)
        self.color_square_rect1 = QRect(76, 315, 106, 80)
        self.color_square_rect2 = QRect(76, 395, 106, 80)
        self.color_square_rect3 = QRect(76, 475, 106, 73)
        self.color_square_rect4 = QRect(307, 235, 106, 80)
        self.color_square_rect5 = QRect(307, 315, 106, 80)
        self.color_square_rect6 = QRect(307, 395, 106, 80)
        self.color_square_rect7 = QRect(307, 475, 106, 73)
        self.color_square_rect8 = QRect(585, 235, 106, 80)
        self.color_square_rect9 = QRect(585, 315, 106, 80)
        self.color_square_rect10 = QRect(585, 395, 106, 80)
        self.color_square_rect11 = QRect(585, 475, 106, 75)
        self.color_square_rect12 = QRect(830, 235, 106, 80)
        self.color_square_rect13 = QRect(830, 315, 106, 80)
        self.color_square_rect14 = QRect(830, 395, 106, 80)
        self.color_square_rect15 = QRect(830, 475, 106, 74)
        self.color_square_rect16 = QRect(80, 650, 106, 80)
        self.color_square_rect17 = QRect(80, 730, 106, 80)
        self.color_square_rect18 = QRect(80, 810, 106, 80)
        self.color_square_rect19 = QRect(80, 890, 106, 73)
        self.color_square_rect20 = QRect(310, 650, 106, 80)
        self.color_square_rect21 = QRect(310, 730, 106, 80)
        self.color_square_rect22 = QRect(310, 810, 106, 80)
        self.color_square_rect23 = QRect(310, 890, 106, 73)
        self.color_square_rect24 = QRect(590, 650, 106, 80)
        self.color_square_rect25 = QRect(590, 730, 106, 80)
        self.color_square_rect26 = QRect(590, 810, 106, 80)
        self.color_square_rect27 = QRect(590, 890, 106, 76)
        self.color_square_rect28 = QRect(835, 650, 106, 80)
        self.color_square_rect29 = QRect(835, 730, 106, 80)
        self.color_square_rect30 = QRect(835, 810, 106, 80)
        self.color_square_rect31 = QRect(835, 890, 106, 74)
        self.colors = [[self.color_cube0, self.color_cube1, self.color_cube2, self.color_cube3],
                       [self.color_cube4, self.color_cube5, self.color_cube6, self.color_cube7],
                       [self.color_cube8, self.color_cube9, self.color_cube10, self.color_cube11],
                       [self.color_cube12, self.color_cube13, self.color_cube14, self.color_cube15],
                       [self.color_cube16, self.color_cube17, self.color_cube18, self.color_cube19],
                       [self.color_cube20, self.color_cube21, self.color_cube22, self.color_cube23],
                       [self.color_cube24, self.color_cube25, self.color_cube26, self.color_cube27],
                       [self.color_cube28, self.color_cube29, self.color_cube30, self.color_cube31]]
        self.setWindowTitle("Наложение областей")
        self.layout = QVBoxLayout()
        self.background_label = QLabel("Большая картинка")
        self.layout.addWidget(self.background_label)
        self.background_pixmap = None
        self.selected_areas = []
        self.background_pixmap = QPixmap(random.choice(picture))
        self.background_label.setPixmap(self.background_pixmap.scaled(980, 940, Qt.AspectRatioMode.KeepAspectRatio))
        self.setLayout(self.layout)
        self.update_background()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def new_game(self):
        process = subprocess.Popen([sys.executable, "start_game.py"])
        self.close()

    def update_background(self):
        if self.background_pixmap:
            self.btn2 = QPushButton('Начать заново', self)
            self.btn2.resize(100, 50)
            self.btn2.move(25, 25)
            self.btn2.clicked.connect(self.new_game)
            combined_pixmap = QPixmap(self.background_pixmap.size())
            combined_pixmap.fill(Qt.GlobalColor.transparent)
            painter = QPainter(combined_pixmap)
            painter.drawPixmap(0, 0, self.background_pixmap)
            for area in self.selected_areas:
                if area['selected']:
                    painter.fillRect(area['rect'], QColor(255, 0, 0, 100))
            painter.fillRect(self.color_square_rect0, QColor(self.colors[0][0]))
            painter.fillRect(self.color_square_rect1, QColor(self.colors[0][1]))
            painter.fillRect(self.color_square_rect2, QColor(self.colors[0][2]))
            painter.fillRect(self.color_square_rect3, QColor(self.colors[0][3]))
            painter.fillRect(self.color_square_rect4, QColor(self.colors[1][0]))
            painter.fillRect(self.color_square_rect5, QColor(self.colors[1][1]))
            painter.fillRect(self.color_square_rect6, QColor(self.colors[1][2]))
            painter.fillRect(self.color_square_rect7, QColor(self.colors[1][3]))
            painter.fillRect(self.color_square_rect8, QColor(self.colors[2][0]))
            painter.fillRect(self.color_square_rect9, QColor(self.colors[2][1]))
            painter.fillRect(self.color_square_rect10, QColor(self.colors[2][2]))
            painter.fillRect(self.color_square_rect11, QColor(self.colors[2][3]))
            painter.fillRect(self.color_square_rect12, QColor(self.colors[3][0]))
            painter.fillRect(self.color_square_rect13, QColor(self.colors[3][1]))
            painter.fillRect(self.color_square_rect14, QColor(self.colors[3][2]))
            painter.fillRect(self.color_square_rect15, QColor(self.colors[3][3]))
            painter.fillRect(self.color_square_rect16, QColor(self.colors[4][0]))
            painter.fillRect(self.color_square_rect17, QColor(self.colors[4][1]))
            painter.fillRect(self.color_square_rect18, QColor(self.colors[4][2]))
            painter.fillRect(self.color_square_rect19, QColor(self.colors[4][3]))
            painter.fillRect(self.color_square_rect20, QColor(self.colors[5][0]))
            painter.fillRect(self.color_square_rect21, QColor(self.colors[5][1]))
            painter.fillRect(self.color_square_rect22, QColor(self.colors[5][2]))
            painter.fillRect(self.color_square_rect23, QColor(self.colors[5][3]))
            painter.fillRect(self.color_square_rect24, QColor(self.colors[6][0]))
            painter.fillRect(self.color_square_rect25, QColor(self.colors[6][1]))
            painter.fillRect(self.color_square_rect26, QColor(self.colors[6][2]))
            painter.fillRect(self.color_square_rect27, QColor(self.colors[6][3]))
            painter.fillRect(self.color_square_rect28, QColor(self.colors[7][0]))
            painter.fillRect(self.color_square_rect29, QColor(self.colors[7][1]))
            painter.fillRect(self.color_square_rect30, QColor(self.colors[7][2]))
            painter.fillRect(self.color_square_rect31, QColor(self.colors[7][3]))
            self.background_label.setPixmap(combined_pixmap)
            self.selected_areas = [
                {'rect': QRect(70, 235, 120, 320), 'selected': False, 0: self.colors[0]},
                {'rect': QRect(300, 235, 120, 320), 'selected': False, 1: self.colors[1]},
                {'rect': QRect(577, 235, 120, 320), 'selected': False, 2: self.colors[2]},
                {'rect': QRect(825, 235, 120, 320), 'selected': False, 3: self.colors[3]},
                {'rect': QRect(73, 650, 120, 320), 'selected': False, 4: self.colors[4]},
                {'rect': QRect(302, 650, 120, 320), 'selected': False, 5: self.colors[5]},
                {'rect': QRect(583, 650, 120, 320), 'selected': False, 6: self.colors[6]},
                {'rect': QRect(828, 650, 120, 320), 'selected': False, 7: self.colors[7]}
            ]
            self.background_label.mousePressEvent = self.mouse_press_event
            painter.end()

    def mouse_press_event(self, event):
        last_color = ""
        if event.button() == Qt.MouseButton.LeftButton:
            for area in self.selected_areas:
                if area['rect'].contains(event.pos()):
                    area['selected'] = not area['selected']
                    if self.last_bottle == []:
                        if (self.color_square_rect0.contains(event.pos()) or self.color_square_rect1.contains(
                                event.pos())
                                or self.color_square_rect2.contains(event.pos()) or self.color_square_rect3.contains(
                                    event.pos())):
                            self.last_bottle = 0
                        elif (self.color_square_rect4.contains(event.pos()) or self.color_square_rect5.contains(
                                event.pos())
                              or self.color_square_rect6.contains(event.pos()) or self.color_square_rect7.contains(
                                    event.pos())):
                            self.last_bottle = 1
                        elif (self.color_square_rect8.contains(event.pos()) or self.color_square_rect9.contains(
                                event.pos())
                              or self.color_square_rect10.contains(event.pos()) or self.color_square_rect11.contains(
                                    event.pos())):
                            self.last_bottle = 2
                        elif (self.color_square_rect12.contains(event.pos()) or self.color_square_rect13.contains(
                                event.pos())
                              or self.color_square_rect14.contains(event.pos()) or self.color_square_rect15.contains(
                                    event.pos())):
                            self.last_bottle = 3
                        elif (self.color_square_rect16.contains(event.pos()) or self.color_square_rect17.contains(
                                event.pos())
                              or self.color_square_rect18.contains(event.pos()) or self.color_square_rect19.contains(
                                    event.pos())):
                            self.last_bottle = 4
                        elif (self.color_square_rect20.contains(event.pos()) or self.color_square_rect21.contains(
                                event.pos())
                              or self.color_square_rect22.contains(event.pos()) or self.color_square_rect23.contains(
                                    event.pos())):
                            self.last_bottle = 5
                        elif (self.color_square_rect24.contains(event.pos()) or self.color_square_rect25.contains(
                                event.pos())
                              or self.color_square_rect26.contains(event.pos()) or self.color_square_rect27.contains(
                                    event.pos())):
                            self.last_bottle = 6
                        elif (self.color_square_rect28.contains(event.pos()) or self.color_square_rect29.contains(
                                event.pos())
                              or self.color_square_rect30.contains(event.pos()) or self.color_square_rect31.contains(
                                    event.pos())):
                            self.last_bottle = 7
                        self.update_background()
                    else:
                        if (self.color_square_rect0.contains(event.pos()) or self.color_square_rect1.contains(
                                event.pos())
                                or self.color_square_rect2.contains(event.pos()) or self.color_square_rect3.contains(
                                    event.pos())):
                            self.before_bottle = self.last_bottle
                            self.last_bottle = 0
                        elif (self.color_square_rect4.contains(event.pos()) or self.color_square_rect5.contains(
                                event.pos())
                              or self.color_square_rect6.contains(event.pos()) or self.color_square_rect7.contains(
                                    event.pos())):
                            self.before_bottle = self.last_bottle
                            self.last_bottle = 1
                        elif (self.color_square_rect8.contains(event.pos()) or self.color_square_rect9.contains(
                                event.pos())
                              or self.color_square_rect10.contains(event.pos()) or self.color_square_rect11.contains(
                                    event.pos())):
                            self.before_bottle = self.last_bottle
                            self.last_bottle = 2
                        elif (self.color_square_rect12.contains(event.pos()) or self.color_square_rect13.contains(
                                event.pos())
                              or self.color_square_rect14.contains(event.pos()) or self.color_square_rect15.contains(
                                    event.pos())):
                            self.before_bottle = self.last_bottle
                            self.last_bottle = 3
                        elif (self.color_square_rect16.contains(event.pos()) or self.color_square_rect17.contains(
                                event.pos())
                              or self.color_square_rect18.contains(event.pos()) or self.color_square_rect19.contains(
                                    event.pos())):
                            self.before_bottle = self.last_bottle
                            self.last_bottle = 4
                        elif (self.color_square_rect20.contains(event.pos()) or self.color_square_rect21.contains(
                                event.pos())
                              or self.color_square_rect22.contains(event.pos()) or self.color_square_rect23.contains(
                                    event.pos())):
                            self.before_bottle = self.last_bottle
                            self.last_bottle = 5
                        elif (self.color_square_rect24.contains(event.pos()) or self.color_square_rect25.contains(
                                event.pos())
                              or self.color_square_rect26.contains(event.pos()) or self.color_square_rect27.contains(
                                    event.pos())):
                            self.before_bottle = self.last_bottle
                            self.last_bottle = 6
                        elif (self.color_square_rect28.contains(event.pos()) or self.color_square_rect29.contains(
                                event.pos())
                              or self.color_square_rect30.contains(event.pos()) or self.color_square_rect31.contains(
                                    event.pos())):
                            self.before_bottle = self.last_bottle
                            self.last_bottle = 7
                    for t in area.values():
                        last_color = t
                    self.before_color = self.last_color
                    self.last_color = last_color
        if self.before_bottle != []:
            if self.before_bottle != self.last_bottle:
                if set(self.before_color) != {"#FFFFFF"}:
                    self.hod_num += 1
                    self.swap_colors(self.before_bottle, self.last_bottle)
                    self.update_background()

    def swap_colors(self, num1, num2):
        a = self.colors[num1]
        b = self.colors[num2]
        c = b.count("#FFFFFF")
        q = 0
        g = 0
        if "#FFFFFF" in a:
            n = a.count("#FFFFFF")
            a = a[n:]
        yoky = b.copy()
        if "#FFFFFF" in yoky:
            n = yoky.count("#FFFFFF")
            yoky = yoky[n:]
        yoky += [""]
        if yoky[0] != a[0]:
            g = 0
        else:
            if yoky[1] != a[0]:
                g = 1
            else:
                if yoky[2] != a[0]:
                    g = 2
                else:
                    if yoky[3] != a[0]:
                        g = 3
        if yoky == [""]:
            g = 1
        yok = a.copy()
        yok += [""]
        if yok[0] != yok[1]:
            q = 0
        else:
            if yok[1] != yok[2]:
                q = 1
            else:
                if yok[2] != yok[3]:
                    q = 2
                else:
                    if yok[3] != yok[4]:
                        q = 3
        if g != 0 and set(a) != {"#FFFFFF"} and len(a) == 4:
            if c - 1 > q:
                u = c - q - 1
                a, b = b[:q + 1] + a[q + 1:], a[:q + 1] + b[u + len(a[:q + 1]):]
            elif q >= c - 1:
                a, b = b[0:c] + a[c:], a[0:c] + b[c:]
        elif set(b) == {"#FFFFFF"} and g != 0:
            a, b = b[:q + 1] + a[q + 1:], a[:q + 1]
        elif len(a) < 4 and g != 0:
            pop = b.copy()
            if "#FFFFFF" in pop:
                n = pop.count("#FFFFFF")
                pop = pop[n:]
            a, b = b[:q + 1] + a[q + 1:], a[:q + 1] + pop
        if len(a) < 4:
            f = 4 - len(a)
            v = ["#FFFFFF" for _ in range(f)]
            a = v + a
        if len(b) < 4:
            f = 4 - len(b)
            v = ["#FFFFFF" for _ in range(f)]
            b = v + b
        if len(a) == 4:
            if len(b) == 4:
                self.colors[num1] = a
                self.colors[num2] = b
                self.check_win()
                self.before_bottle = []
                self.last_bottle = []

    def check_win(self):
        if len(set(self.colors[0])) == len(set(self.colors[1])) == len(set(self.colors[2])) == len(
                set(self.colors[3])) == len(set(self.colors[4])) == len(set(self.colors[5])) == len(
            set(self.colors[6])) == len(set(self.colors[7])) == 1:
            self.open_second_form()
            self.close()

    def open_second_form(self):
        self.second_form = SecondForm(self, "")
        self.second_form.show()


class SecondForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)
        self.center()

    def initUI(self, args):
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Поздравление')
        greeting_name = args[-1] if args else "Игрок"
        self.lbl = QLabel(f"Поздравляем, {greeting_name}!", self)
        self.lbl.adjustSize()
        label_x = (self.width() - self.lbl.width()) // 2
        self.lbl.move(label_x, 10)
        con = sqlite3.connect("liquids_sort_puzzle_database.sqlite")
        cur = con.cursor()
        tu = cur.execute(f'''SELECT id_player FROM player''').fetchall()
        res = cur.execute(
            f'''SELECT name, level_number FROM liquids_sort_puzzle WHERE id_player = {int(tu[0][0])}''').fetchall()
        yu = cur.execute(f"""UPDATE liquids_sort_puzzle 
                SET level_number = '{int(res[0][1]) + 1}' 
                WHERE id_player = {int(tu[0][0])}""").fetchall()
        res1 = cur.execute(
            f'''SELECT name, level_number FROM liquids_sort_puzzle WHERE id_player = {int(tu[0][0])}''').fetchall()
        self.label = QLabel(f"{res1[0][0]}, поздравляем вас с успешным прохождением {int(res1[0][1])} уровня!", self)
        self.label.adjustSize()
        label_main_x = (self.width() - self.label.width()) // 2
        self.label.move(label_main_x, 60)
        self.btn = QPushButton('Следующий уровень', self)
        self.btn.resize(250, 50)
        self.btn.move(130, 120)
        self.btn1 = QPushButton('Выйти', self)
        self.btn1.resize(250, 50)
        self.btn1.move(130, 190)
        self.btn.clicked.connect(self.new_game)
        self.btn1.clicked.connect(self.exeit)
        con.commit()
        con.close()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def exeit(self):
        self.close()

    def new_game(self):
        process = subprocess.Popen([sys.executable, "start_game.py"])
        self.close()


app = QApplication(sys.argv)
window = ImageOverlayApp()
window.resize(980, 940)
window.center()
window.show()
sys.exit(app.exec())
