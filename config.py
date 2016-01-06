#!/usr/bin/env python
import subprocess
import os
import json
import sys


# TODO: screensaver, hidpi, mouse config

class Config:
    def __init__(self):
        STOCK_BGS = 6
        BG = []
        MEDIADIR = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), 'media'))
        for i in range(1, STOCK_BGS):
            BG.append(os.path.abspath(os.path.join(MEDIADIR, 'wallpapers', 'bg' + str(i) + '.png')))

        self.ELEMENTS = {'Window Manager': [['xfwm4'],
                                            ['openbox'],
                                            ['blackbox'],
                                            ['compiz'],
                                            ['icewm'],
                                            ['bad_test'],
                                            ['fvwm'],
                                            ['gnome-shell']
                                            ],
                         'Launcher': [['albert'],
                                      ['gnome-do']
                                      ],
                         'Network': [['nm-applet']],
                         'Battery': [['ptbatterysystemtray'], ['/usr/bin/ptbatterysystemtray']],
                         'Dock': [['lxpanel'],
                                  ['pypanel'],
                                  ['cairo-dock'],
                                  ['xfce4-panel'],
                                  ['razor-panel'],
                                  ['mate-panel'],
                                  ['lxqt-panel'],

                                  ['fbpanel']],
                         'Background': [['display', '-window', 'root', BG[0]],
                                        ['display', '-window', 'root', BG[1]],
                                        ['display', '-window', 'root', BG[2]],
                                        ['display', '-window', 'root', BG[3]],
                                        ['display', '-window', 'root',BG[4]],
                                        ['xv', '-root', '-quit', BG[0]],
                                        ['xsetroot', '-grey'],
                                        ['hsetroot', '-solid', '#333333']
                                        ],
                         'Volume control': [['volumeicon']],
                         'Disable touchpad tapping': [['synclient', 'MaxTapTime=0']],
                         'Reverse scroll direction': [['xmodmap', '-e', '"pointer = 1 2 3 5 4"']]
                         }
        self.config = {'settings': {'MEDIADIR': MEDIADIR, 'THEME': 'Meta'},
                       'binaries': {}
                       }
        self.THEMES = ['Meta', 'Meta-hdpi', 'Clearlooks']

    def validate_binaries(self, binaries):
        valid_binaries = []
        FNULL = open(os.devnull, 'w')

        for binary in binaries:
            # ensure that we skip arguments
            if subprocess.call(['which', binary[0]], stdout=FNULL, stderr=FNULL) == 0:
                valid_binaries.append(binary)
        return valid_binaries

    def chooser(self, list_items):
        choice = 1
        list_items.append(None)
        for item in list_items:
            print choice, item
            choice += 1
        user_selection = int(raw_input('selection: '))
        user_selection -= 1
        if user_selection in range(0, len(list_items)):
            return list_items[user_selection]

    def save_config(self):
        print self.config
        homedir = os.path.expanduser('~')
        conffile = os.path.join(homedir, '.metade.conf')
        with open(conffile, 'w') as f:
            json.dump(self.config, f, indent=4)


    def wizard(self):
        for description, choices in self.ELEMENTS.iteritems():
            print 'Make a selection: ' + description
            print choices
            #print 'Autodetected the following from', ', '.join(choices), ':'
            choice = self.chooser(self.validate_binaries(choices))
            self.config['binaries'][description] = choice

        choice = self.chooser(self.THEMES)
        print choice, 'was chosen'
        self.config['settings']['THEME'] = choice


        # Add general stuff. Comment out if that's too fancy for you.
        # self.config['dbus'] = 'dbus-launch'
        # self.config['dpi'] = 'xrandr --dpi 200'

        self.save_config()



cf = Config()
cf.wizard()
