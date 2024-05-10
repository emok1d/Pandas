import pandas as pd

music = [
    ['LiL PEEP', 'Star Shopping'],
    ['Deftones', 'Change'],
    ['Crystal Castles', 'Empathy'],
    ['Basement', 'Covet'],
    ['Enique', 'Pillow']
        ]

entries = ['artist', 'track']

playlist = pd.DataFrame(data=music, columns=entries)
print(playlist)