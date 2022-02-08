import os

def gobstr(mdpe):
    os.system(f"gobuster dir -u {mdpe} -w /usr/share/wordlists/dirb/common.txt")
    

    