#pylint: disable-all

from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
from anki.hooks import wrap

from aqt.utils import showInfo

import os
import random

mw.showdogs = {}
mw.showdogs['card_count'] = 0
mw.showdogs['interval'] = 10

class DogDialog(QDialog):

    def keyPressEvent(self, event):

        # why does it have to be hex? nobody knows.
        # 0x20 == spacebar
        if event.key() == 0x20:
            self.close()


def showDog():
    # mw.showdogs['card_count'] = mw.showdogs['card_count'] + 1
    # if mw.showdogs['card_count'] % mw.showdogs['interval'] != 0:
    #     return

    dialog = DogDialog(mw)

    layout = QVBoxLayout(dialog)
    dialog.setLayout(layout)

    dogs_dir = os.path.join(mw.pm.addonFolder(), 'showdogs')

    image_path = random.choice(os.listdir(dogs_dir))
    data = open(os.path.join(dogs_dir, image_path), 'r').read()

    image = QImage()
    image.loadFromData(data)

    label = QLabel()
    myPixmap = QPixmap(os.path.join(dogs_dir, image_path))
    myScaledPixmap = myPixmap.scaled(label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
    label.setPixmap(myScaledPixmap)
    label.show()
    layout.addWidget(label)

    dialog.exec_()

mw.reviewer.nextCard = wrap(mw.reviewer.nextCard, showDog)
