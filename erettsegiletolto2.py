from bs4 import BeautifulSoup as bs
import requests
import re
import os
import zipfile


mappagyoker = r"C:\Users\Zsolti\Desktop\mappák\érettségi\infó\emelt\\"


soup = bs(requests.get(r"https://www.informatikatanarok.hu/erettsegi-feladatok/emelt-szintu-informatika-erettsegi-feladatok-es-megoldasok").content, features="lxml")

feladatlapok = soup.find_all(name = "a", attrs={"href" : re.compile(r"media/uploads/Informatika_erettsegi/Emelt/e_\w+fl.pdf")})
forrasfajlok = soup.find_all(name= "a",text="Forrásfájlok")



for x in range(len(feladatlapok)):
    jelen_feladatlap = feladatlapok[x]
    jelen_forras = forrasfajlok[x]

    match = re.search(r"Emelt szintű informatika érettségi feladatlap (\d{4}) (.+)$" ,jelen_feladatlap.text)
    

    path = mappagyoker + match.group(1) + " " + match.group(2)
    try:
        os.mkdir(path)
    except FileExistsError:
        pass
    
    url = "https://www.informatikatanarok.hu/" + jelen_forras.get("href")
    zipforras = requests.get(url).content

    with open(path + r"\forrás.zip", "wb") as f:
        f.write(zipforras)
    
    z_ref = zipfile.ZipFile(path + r"\forrás.zip", "r")
    z_ref.extractall(path)
    z_ref.close()

    os.remove(path + r"\forrás.zip")


    url = "https://www.informatikatanarok.hu/" + jelen_feladatlap.get("href")
    pdfforras = requests.get(url).content

    with open(path + r"\feladatlap.pdf", "w+b") as f:
        f.write(pdfforras)