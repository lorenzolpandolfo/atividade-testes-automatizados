from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL_LOGIN_PAGE = "https://bugbank.netlify.app/"
URL_USER_PROFILE = URL_LOGIN_PAGE + "home"

CORRECT_USER_NAME = "André da Silva"
CORRECT_USER_EMAIL = "usuariofalso123@email.com"
CORRECT_USER_PASSWORD = "senha123"

def criar_usuario(browser):
    browser.get("https://bugbank.netlify.app/")
    browser.find_element(By.XPATH, "//button[text()='Registrar']").click()
    browser.find_element(By.NAME, "name").send_keys(CORRECT_USER_NAME)
    browser.find_element(By.XPATH, "(//input[@name='email'])[2]").send_keys(CORRECT_USER_EMAIL)
    browser.find_element(By.XPATH, "(//input[@name='password'])[2]").send_keys(CORRECT_USER_PASSWORD)
    browser.find_element(By.NAME, "passwordConfirmation").send_keys(CORRECT_USER_PASSWORD)
    browser.find_element(By.XPATH, "//button[text()='Cadastrar']").click()


def realizar_login(browser, email = CORRECT_USER_EMAIL, password = CORRECT_USER_PASSWORD):
    browser.get("https://bugbank.netlify.app/")
    browser.find_element(By.NAME, "email").send_keys(email)
    browser.find_element(By.NAME, "password").send_keys(password)
    browser.find_element(By.XPATH, "//button[text()='Acessar']").click()
    WebDriverWait(browser, 10).until(EC.url_contains("home"))
