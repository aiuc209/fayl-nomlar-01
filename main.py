import os
import datetime

fayl_nomi = []
for filename in os.listdir("."):
    if os.path.isfile(filename):
        timestamp = os.path.getctime(filename)
        sana = datetime.datetime.fromtimestamp(timestamp)
        fayl_nomi.append((filename, sana.strftime("%d.%m.%Y")))

for fayl in fayl_nomi:
    print(fayl[0], fayl[1])
