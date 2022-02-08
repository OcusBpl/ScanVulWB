import os
from lxml import etree
import wpscn as wp

def whtwb(mdpe):
    os.system(f"whatweb -v -a 1 {mdpe} --log-xml dataww.xml")

    doc = etree.parse('dataww.xml')
    for uris in doc.xpath("target/uri"):
        print(f"URL du site : {uris.text}")

    for ip in doc.xpath("target/plugin[name='IP']/string"):
        print(f"IP du site : {ip.text}")

    print(f"Plugins trouvé :")
    for plugins in doc.xpath("target/plugin/name"):
        #print(f"-{plugins.text}")
        if plugins.text == "WordPress":
            print(f"Votre site est sur Wordpress, nous allons lancé un WPScan")
            wp.wpscan(mdpe)