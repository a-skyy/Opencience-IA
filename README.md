# Opencience-IA
Tareas relacionadas con la asignatura de Artificial Intelligence And Open Science In Research Software Engineering

INSTRUCCIONES DE USO
Resultados:
- Keyword cloud de abstracts
- Número de figuras por artículo
- Lista de links por paper

1. CLONAR EL REPOSITORIO

git clone https://github.com/a-skyy/Opencience-IA

2. CREAR ENTORNO DE PYTHON

Crear entorno virtual:
python3 -m venv venv

Activar entorno:
source venv/bin/activate

3. INSTALAR DEPENDENCIAS

Instalar librerías necesarias:
pip install beautifulsoup4
pip install lxml
pip install wordcloud
pip install matplotlib

4. EJECUTAR GROBID

Ir a Google Colab:
Ejecutar Ejecutadoencolab.py


5. PROCESAR LOS PDF CON GROBID

Despues de darle los pdfs a Ejecutandoencolab.py descarga los XML respectivos

6. EJECUTAR LOS SCRIPTS DEL PROYECTO

Volver al directorio principal del proyecto:
Los scripts utilizarán los XML generados por Grobid.
Guardarlos los XML en la carpeta data/ borrando los datos previos en esa carpeta.

6.1 GENERAR KEYWORD CLOUD

python keywordcloud.py
Resultado:
keyword_cloud.png

6.2 GENERAR VISUALIZACIÓN DE FIGURAS

python figurearticle.py
Resultado:
figures_per_article.png

6.3 EXTRAER LINKS DE LOS ARTÍCULOS

python linkfound.py
Resultado:
links_per_article.txt


7. RESULTADOS GENERADOS

El proyecto producirá los siguientes archivos en la misma carpeta de los scripts:
keyword_cloud.png
figures_per_article.png
links_per_article.txt



Estos archivos contienen los resultados finales del análisis.
Badge Zenodo
10.5281/zenodo.18964163
