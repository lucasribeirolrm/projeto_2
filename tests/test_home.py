def test_home_page(browser):
    browser.get('http://127.0.0.1:8081')
    assert browser.title == 'Dash'
    print("Teste da página inicial concluído com sucesso.")


#import time

#def test_home_page(browser):
    #url = "http://127.0.0.1:8080"  # Substitua pelo endereço correto da sua aplicação
    #browser.get(url)
    #time.sleep(5)
    #assert browser.title == "Dash"
    #print("Teste da página inicial concluído com sucesso.")
