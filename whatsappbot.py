# Importar as libs
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
# Navegar até wpp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com')
time.sleep(12)
# definir contatos e grupos e mensagem a ser enviado
contatos = ['Grupo', 'Contato1', 'Contato2']
mensagem = 'Olá sou um bot criado pelo João, este é um teste simples!'
# Buscar contatos/grupos
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
    time.sleep(5)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_mensagem[1].click()
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)
for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
# Campo de pesquisa 'copyable-text selectable-text'
# Campo de texto 'copyable-text selectable-text'
# Enviar mensagens para o contato/grupo

