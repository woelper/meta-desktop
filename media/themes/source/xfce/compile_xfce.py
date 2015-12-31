import os
import shutil
import glob

STATES = {0: ['-active', '-toggled-active'],
          1: ['-inactive', '-toggled-inactive'],
          2: ['-prelight'],
          3: ['-pressed', '-toggled-pressed'],
          }

TYPES = {1: {'types': ['close'], 'states': [0, 1, 2, 3]},
         2: {'types': ['maximize'], 'states': [0, 1, 2, 3]},
         3: {'types': ['menu'], 'states': [0, 1, 2, 3]},
         4: {'types': ['hide'], 'states': [0, 1, 2, 3]},
         5: {'types': ['title-1', 'title-2', 'title-3', 'title-4', 'title-5'], 'states': [0, 1]},
         6: {'types': ['bottom-left'], 'states': [0, 1]},
         7: {'types': ['bottom-right'], 'states': [0, 1]},
         8: {'types': ['bottom'], 'states': [0, 1]},
         9: {'types': ['left'], 'states': [0, 1]},
         10: {'types': ['right'], 'states': [0, 1]},
         }


for template in glob.glob('templates/template_*.png'):
    template_type = template.replace('.png', '').split('_')
    type = int(template_type[1])
    state = int(template_type[2])
    if type in TYPES:
        #final_type = TYPES[type]

        final_types = TYPES[type]['types']

        final_states = []
        if state in STATES:
            for st in TYPES[type]['states']:
                if st == state:
                    final_states = final_states + STATES[st]

        for tp in final_types:
            for st in final_states:
                dest = tp + st + '.png'
                print template, '>', dest
                shutil.copy(template, dest)
