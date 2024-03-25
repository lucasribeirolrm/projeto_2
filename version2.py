import pytest
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

@pytest.fixture(scope="module")
def browser():
    # Configurar o WebDriver para usar o Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_path
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_home_page(browser):
    browser.get(url)
    time.sleep(5)
    assert browser.title == "Dash"
    print("Teste da página inicial concluído com sucesso.")

def test_formulario_page(browser):
    browser.get(url + "/formulario")
    time.sleep(5)
    assert browser.title == "Dash"
    print("Teste da página de formulário concluído com sucesso.")

def test_graficos_page(browser):
    browser.get(url + "/graficos")
    time.sleep(5)
    assert browser.title == "Dashboard - Gráficos"
    print("Teste da página de gráficos concluído com sucesso.")
