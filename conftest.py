import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def browser():
    # Simular configuração do navegador
    # Por exemplo, configurando opções do Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # Executar sem interface gráfica
    chrome_options.add_argument('--disable-gpu')  # Evitar erro ao rodar em headless mode

    # Criar instância do WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    yield driver  # Disponibilizar o WebDriver para os testes

    # Fechar o navegador ao final dos testes
    driver.quit()





#import pytest
#import time
#from selenium import webdriver

#@pytest.fixture(scope="module")
#def browser():
    # Caminho para o executável do Chrome
    #chrome_path = "/usr/bin/chromium-browser"  # Substitua pelo caminho correto do seu Chrome

    # Configurar o WebDriver para usar o Chrome
    #chrome_options = webdriver.ChromeOptions()
    #chrome_options.binary_location = chrome_path
    #driver = webdriver.Chrome(options=chrome_options)
    
    #yield driver
    
    # Fechar o navegador
    #driver.quit()


