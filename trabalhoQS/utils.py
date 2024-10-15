from selenium.webdriver.common.by import By

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
