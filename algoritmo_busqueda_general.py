from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Ruta del driver de Chrome
chromedriver_path = "C:/chromedriver_win32/chromedriver.exe"

# Opciones del driver de Chrome
options = webdriver.ChromeOptions()

# Inicializar el driver de Chrome
driver = webdriver.Chrome(service_log_path='NUL', options=options)

# Navegar a la página de Google
driver.get("https://www.google.com/search?q=campaña+electoral+2023")

# Esperar a que cargue la página de resultados
driver.implicitly_wait(20)

# Obtener el contenido HTML de la página
html = driver.page_source

# Crear un objeto BeautifulSoup para analizar el HTML
soup = BeautifulSoup(html, "lxml")

# Encontrar los elementos de resultados (títulos y URLs)
results = soup.select("div.g")

# Guardar los resultados en un archivo de texto
with open("resultados.txt", "w", encoding="utf-8") as f:
    for result in results:
        title_element = result.select_one("h3")
        if title_element:
            title = title_element.get_text(strip=True) + "\n"
            f.write(title)
        url_element = result.select_one("a")
        if url_element:
            url = url_element["href"] + "\n"
            f.write(url)
        f.write("\n")

# Cerrar el navegador
driver.quit()
