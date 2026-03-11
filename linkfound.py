import os
from bs4 import BeautifulSoup


xml_folder = "./"  

links_dict = {}
for filename in os.listdir(xml_folder):
    if filename.endswith(".xml"):
        xml_path = os.path.join(xml_folder, filename)
        
        with open(xml_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "lxml-xml")
            
            refs = soup.find_all("ref")
            links = [r.get("target") for r in refs if r.get("target")]
            
            links_dict[filename.replace(".xml","")] = links

for paper, links in links_dict.items():
    print(f"\n{paper}:")
    if links:
        for l in links:
            print(f" - {l}")
    else:
        print("No se encontraron links.")
import csv
with open("links_per_article.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Article", "Link"])
    for paper, links in links_dict.items():
        for link in links:
            writer.writerow([paper, link])

print("\n Links guardados en links_per_article.csv")