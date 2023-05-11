from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# ruta del driver de chrome
chromedriver_path = "C:/chromedriver_win32/chromedriver.exe"

# opciones del driver de chrome
options = webdriver.ChromeOptions()
#options.add_argument("--incognito")

# inicializar el driver de chrome
driver = webdriver.Chrome(service_log_path='NUL', options=options)

# navegar a la página de google al apartado noticias con las palabras clave
driver.get("https://www.google.com/search?q=futbol+para+personas+con+discapacidad&tbm=nws")

# encontrar el campo de búsqueda y escribir la consulta
##search_input = driver.find_element(by="name", value="q")
##search_input.send_keys("OpenAI")
##search_input.send_keys(Keys.RETURN)

# esperar a que cargue la página de resultados
driver.implicitly_wait(20)

# obtener los resultados y guardarlos en un archivo de texto
#results = driver.find_elements(by="xpath", value="//div[@class='g']/div/div[@class='rc']/div[@class='r']/a/h3")
results = driver.find_element(By.ID, "rso") 
deepResults = results.find_elements(By.TAG_NAME, "a")
with open("resultados.txt", "w") as f:
    for result in deepResults:
        f.write(result.find_element(By.CSS_SELECTOR, " div > div:nth-child(2) > div:nth-child(2)").text + "\n")
        #f.write(result.text + "\n")
        f.write(result.get_attribute("href") + "\n"+ "\n")

# cerrar el navegador
driver.quit()
