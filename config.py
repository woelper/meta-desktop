#!/usr/bin/env python
import subprocess
import os
import json

class Config:
    def __init__(self):
        self.ELEMENTS = {'Window Manager': ['xfwm4', 'bad_test', 'fvwm', 'gnome-shell'],
                         'Launcher': ['albert', 'gnome-do'],
                         'Dock': ['cairo-dock','xfce4-panel','pypanel', 'mate-panel', 'lxqt-panel', 'lxpanel', 'fbpanel'],
                         'Background': ['xsetroot', 'hsetroot']
                         }
        self.config = {}

    def validate_binaries(self, binaries):
        valid_binaries = []
        for binary in binaries:
            if subprocess.call(['which', binary]) == 0:
                valid_binaries.append(binary)
        return valid_binaries

    def chooser(self, list_items):
        choice = 1
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
        conffile = os.path.join(homedir,'.metade.conf')
        with open(conffile,'w') as f:
            json.dump(self.config, f, indent=4)


    def wizard(self):
        for description, choices in self.ELEMENTS.iteritems():
            print description
            choice = self.chooser(self.validate_binaries(choices))
            self.config[description] = choice


        self.save_config()



cf = Config()
cf.wizard()
