import os
import json

def wpscan(mdpe):
    os.system(f"wpscan -v -e vp ap vt --url {mdpe} -o wpscn -f json")
    
    print(f"Resultat WP trouvé :")
    with open('wpscn') as json_data:
        data = json.load(json_data)
        #print(data)

        ##theme
        themes = data['main_theme']
        print("Theme : ", themes['slug'])
        print("Location : ", themes['location'])
        print("Author : ", themes['author'])
        

    