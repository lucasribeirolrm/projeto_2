import time
from selenium import webdriver

# Caminho para o executável do Chrome
chrome_path = "/home/lucasrm/dash/chrome-linux64/chrome"  # Substitua pelo caminho correto do seu Chrome

# Configurar o WebDriver para usar o Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_path
driver = webdriver.Chrome(options=chrome_options)

# Endereço de execução
url = "http://127.0.0.1:8080"  # Substitua pelo endereço correto da sua aplicação

# Teste da página inicial
driver.get(url)
time.sleep(10)
assert "Dash" in driver.title
assert "pagina inicial" in driver.page_source
print("Teste da página inicial concluído com sucesso.")

# Teste da página de formulário
driver.get(url + "/formulario")
time.sleep(10)
assert "Dashboard - Formulário" in driver.title
assert "Formulário" in driver.page_source
print("Teste da página de formulário concluído com sucesso.")

# Teste da página de gráficos
driver.get(url + "/graficos")
time.sleep(10)
assert "Dashboard - Gráficos" in driver.title
assert "Gráficos" in driver.page_source
print("Teste da página de gráficos concluído com sucesso.")

# Fechar o navegador
driver.quit()
