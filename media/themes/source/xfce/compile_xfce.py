import os
import shutil

XFCE = {3: 'close',
        6: 'maximize',
        9: 'menu',
        12: 'hide'
        }

title_states = ['-active', '-inactive']
button_states = ['-active', '-inactive', '-pressed', '-toggled-pressed', '-toggled-inactive', '-toggled-active']


for frame, name in XFCE.iteritems():
    for state in button_states:
        for i in range(frame-3, frame):
            print i+1, name, state
            shutil.copy('templates/' + str(i+1)+'.png', name + state + '.png')

for i in range(1, 6):
    print i
    shutil.copy('templates/title_1.png', 'title-' + str(i) + '-active.png')
    shutil.copy('templates/title_2.png', 'title-' + str(i) + '-inactive.png')