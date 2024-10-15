import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils import *

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_login_invalido(browser):
    browser.get("https://bugbank.netlify.app/")
    browser.find_element(By.NAME, "email").send_keys("usuario@exemplo.com")
    browser.find_element(By.NAME, "password").send_keys("senha123")
    browser.find_element(By.XPATH, "//button[text()='Acessar']").click()
    assert "Usuário ou senha inválido" in browser.page_source

def test_cadastro_novo_usuario(browser):
    criar_usuario(browser)
    assert "foi criada com sucesso" in browser.page_source

def test_login_valido(browser):
    criar_usuario(browser)
    browser.get("https://bugbank.netlify.app/")
    browser.find_element(By.NAME, "email").send_keys(CORRECT_USER_EMAIL)
    browser.find_element(By.NAME, "password").send_keys(CORRECT_USER_PASSWORD)
    browser.find_element(By.XPATH, "//button[text()='Acessar']").click()
    WebDriverWait(browser, 10).until(EC.url_contains("home"))
    assert "home" in browser.current_url
