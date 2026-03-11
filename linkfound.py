import os
from bs4 import BeautifulSoup

xml_folder = "./"
output_file = "links_per_article.txt"

links_dict = {}

for filename in os.listdir(xml_folder):
    if filename.endswith(".xml"):
        xml_path = os.path.join(xml_folder, filename)
        
        with open(xml_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "lxml-xml")
            
            refs = soup.find_all("ref")
            links = [r.get("target") for r in refs if r.get("target") and r.get("target").startswith("http")]
            
            links_dict[filename.replace(".xml","")] = links

with open(output_file, "w", encoding="utf-8") as f:
    for paper, links in links_dict.items():
        f.write(f"{paper}:\n")
        if links:
            for link in links:
                f.write(f"{link}\n")
        else:
            f.write("No se encontraron links.\n")
        f.write("\n")

print(f"Todos los links válidos se han guardado en {output_file}")