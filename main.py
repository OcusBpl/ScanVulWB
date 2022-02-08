import os
import whatwb as ww
import gobster as gb

#mdpe = input("Entrez l'url' : ")
mdpe = "https://guardea.com"

#Lancement detection web
ww.whtwb(mdpe)

#Lancement Enumeration
gb.gobstr(mdpe)

os.system(f"rm dataww.xml")
os.system(f"rm wpscn")