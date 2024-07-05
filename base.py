from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException
        ]
    )
    return driver, wait

#Forma correta de achar o XPATH
#//tag[@atributo='valor']
'''
# Como montar um XPATH
# De forma geral você vai montar um xpath da seguinte forma
//tag[@atributo="valor"]

# Ultra genérico(engloba todas tags da página)
//* 

# Ultra genérico + tag
//*[tag]

# apenas contem um parte do texto
//*[contains(text(),"Exemplo")] 
//*[contains(text(),"Exemplo") or contains( text(), "Dropdown" )]
//*[contains(text(),'Dropdown') and  contains(text(),'Bootstrap') ]

# Inicia com um texto
//*[starts-with(text(),"Exemplo")]
//*[starts-with(@class,"btn")]

# Buscando apenas por um texto spefícico
//*[text()="Exemplo Checkbox"] # Genérico, porém especificando o texto
//h4[text()="Exemplo Checkbox"] # Com tag e especificando o texto

# Buscando por um elemento específico usando tag e propriedade
//button[@id="dropdownMenuButton"] # tag com propriedade e valor
//section[@class="jumbotron"] # tag com propriedade e valor
//div[@class="form-check"] #tag com propriedade e valor

# Como encontrar filhos de cada elemento
# Encontra único filho
//div/fieldset
//div/fieldset/h4
# Encontrar filho, quando há multiplos filhos
# Find child when multiple elements
//thead/tr//th[2]
'''