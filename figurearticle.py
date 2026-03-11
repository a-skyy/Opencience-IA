
import os
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


xml_folder = "./data/"  

article_names = []
figures_count = []


for filename in os.listdir(xml_folder):
    if filename.endswith(".xml"):
        xml_path = os.path.join(xml_folder, filename)
        
        with open(xml_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "lxml-xml")
            
            figs = soup.find_all("figure")
            
            figures_count.append(len(figs))
            article_names.append(filename.replace(".xml", ""))  

plt.figure(figsize=(12,6))
plt.bar(range(len(article_names)), figures_count, color='skyblue')
plt.xticks(range(len(article_names)), article_names, rotation=45, ha='right')
plt.ylabel("Número de figuras")
plt.xlabel("Artículo")
plt.title("Número de figuras por artículo")
plt.tight_layout()
plt.show()

plt.savefig("figures_per_article.png")
print(" Gráfico guardado como figures_per_article.png")