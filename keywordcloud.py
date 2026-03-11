import os
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


xml_folder = "./" 

output_image = "keyword_cloud.png"

abstracts = []

for filename in os.listdir(xml_folder):
    if filename.endswith(".xml"):
        xml_path = os.path.join(xml_folder, filename)
        
        with open(xml_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "lxml-xml")  
            
            abstract_tags = soup.find_all("abstract")
            
            for ab_tag in abstract_tags:
                text = ab_tag.get_text(separator=" ", strip=True)
                if text:
                    abstracts.append(text)


text = " ".join(abstracts)

if not text.strip():
    print("No se encontraron abstracts válidos en los XML.")
    text = "No abstracts found"

stopwords = set(STOPWORDS)
stopwords.update(["the", "and", "of", "in", "a", "to", "de", "la", "el"])

wordcloud = WordCloud(
    width=1200,
    height=600,
    background_color="white",
    stopwords=stopwords,
    colormap="viridis"
).generate(text)

plt.figure(figsize=(15, 7))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.tight_layout()
plt.show()

wordcloud.to_file(output_image)
print(f" Word cloud guardada como {output_image}")