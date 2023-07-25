from bs4 import BeautifulSoup
from loguru import logger
from pathlib import Path
import subprocess
import os

Downloads = Path.home()/"Downloads"

if not os.path.exists(Downloads/"smh"):
    os.makedirs(Downloads/"smh")

def error_log(record):
    with open(str(Downloads/ 'smh/error.log'), 'a', encoding='utf-8') as f:
        f.write(str(record))

logger.add(error_log, level='ERROR')

try:
    with open(str(Downloads / 'following.html'), 'r') as f:
        content = f.read()
        soup = BeautifulSoup(content, 'lxml')
        wing = soup("a")
    with open(str(Downloads / 'followers.html'), 'r') as f:
        content = f.read()
        Soup = BeautifulSoup(content, 'lxml')
        wers = Soup("a")    
    diffs = [wing_element for wing_element in wing if wing_element not in wers]
    with open(str(Downloads/'smh/smh.html'), "w") as f:
        f.write(f"<html><head><link rel=\"preload\" href=\"https://i.imgur.com/y6Bl6aL.jpeg\" as \"image\" /><link rel=\"preload\" href=\"https://i.imgur.com/Y6GiTI2.png\" as \"image\" /><link rel=\"preconnect\" href=\"https://fonts.googleapis.com\"><link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin><link href=\"https://fonts.googleapis.com/css2?family=Abril+Fatface&family=Open+Sans:wght@400;800&display=swap\" rel=\"stylesheet\"><style>*{{font-family: 'Open Sans', sans-serif;}} body{{background: rgb(109, 52, 103);background-image: url(\"https://i.imgur.com/y6Bl6aL.jpeg\");background-size:contain;}} .container {{max-width: 100%;display:grid;grid-template-columns: repeat(auto-fit, minmax(300px,1fr));padding:1em;gap:1em;}} div:not(.container,.logo,.head1,.header) {{padding: 2em;border-radius: 25px;text-align: center;background: linear-gradient(to right bottom, rgba(0, 0, 0, 0.6), rgb(0, 0, 0,0.8));overflow-x: hidden;white-space: nowrap;text-overflow: ellipsis;}} a{{font-size: 2em;text-decoration: none;color:white;}} .header{{display:flex; justify-content:space-around;}} .head1 p{{color:white;font-family: 'Abril Fatface', cursive;font-size: 5em;padding-right:10vw;}}.logo{{padding-top: 10vh;}}</style></head><body><div class=\"header\"><div class=\"logo\"><a target=\"_blank\" href=\"https://ulasahmetkirac.com\"><img src=\"https://i.imgur.com/Y6GiTI2.png\" width=\"450vw\" height=\"100vh\"></a></div><div class=\"head1 \"><p>shakin' my head.</p></div></div><div class=\"container\">")
        for diff in diffs:
            f.write("<div><a href=\"%s\"> %s </a></div>" % (diff.get("href"), diff.contents[0]))
        f.write("</div></body></html>\n")
    subprocess.call(['open', str(Downloads/'smh/smh.html')])

except:
    logger.exception("Exception occurred")
