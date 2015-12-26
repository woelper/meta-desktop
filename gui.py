#!/usr/bin/env python

from PySide.QtCore import *
from PySide.QtGui import *
import sys


app = QApplication(sys.argv)

window = QTabWidget()
window.addTab()
layout = QVBoxLayout()
button = QPushButton('oi')
layout.addWidget(button)
window.setLayout(layout)


window.show()
# Enter Qt application main loop
app.exec_()
sys.exit()

"""
xmodmap -e "pointer = 1 2 3 5 4"
synclient MaxTapTime=0 # tap to click off
synclient MaxTapTime=180 # tap to click on

"""


"""
import random

def rename():
    names = ['Diggur','Marek','Dudu','Trump','Currywurst']
    button.setText(random.choice(names))

window = QtGui.QWidget()
layout = QtGui.QVBoxLayout()
button = QtGui.QPushButton('oi')
button.clicked.connect(rename)
layout.addWidget(button)
window.setLayout(layout)
window.show()
"""



