from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as condicao_esperada
from base import iniciar_driver
from senha import senha, email
from time import sleep as s
import random
driver, wait = iniciar_driver()
#Entrar no insta
driver.get('https://instagram.com')
entrar_facebook = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[5]/button/span[2]')))
s(random.randint(1, 10))
entrar_facebook.click()
#Colocar email

campo_email_facebook = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//*[@id="email"]')))
campo_email_facebook.send_keys(email())
s(random.randint(1,5))
#colocar senha
campo_senha_facebook = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//*[@id="pass"]')))
campo_senha_facebook.send_keys(senha())
s(random.randint(1,5))
#Entrar no insta
botao_entrar = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//*[@id="loginbutton"]')))
botao_entrar.click()

s(15)
driver.get('https://www.instagram.com/direct/t/111288093597180')
s(15)

video = driver.find_elements('xpath', '//*[@class="x1277o0a"]')
s(10)
passar_mouse = ActionChains(driver)
passar_mouse.move_to_element(video[0]).perform()
s(5)
reagir = driver.find_element('xpath', '')
reagir.click()
input('')


