import pytest
import time
from selenium import webdriver

@pytest.fixture(scope="module")
def browser():
    # Caminho para o executável do Chrome
    chrome_path = "/home/lucasrm/dash/chrome-linux64/chrome"  # Substitua pelo caminho correto do seu Chrome

    # Configurar o WebDriver para usar o Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_path
    driver = webdriver.Chrome(options=chrome_options)
    
    yield driver
    
    # Fechar o navegador
    driver.quit()


