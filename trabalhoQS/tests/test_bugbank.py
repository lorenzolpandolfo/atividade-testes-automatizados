import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from trabalhoQS.utils import *

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_login_invalido(browser):
    browser.get(URL_LOGIN_PAGE)
    browser.find_element(By.NAME, "email").send_keys("usuario@exemplo.com")
    browser.find_element(By.NAME, "password").send_keys("senha123")
    browser.find_element(By.XPATH, "//button[text()='Acessar']").click()
    assert "Usuário ou senha inválido" in browser.page_source

def test_cadastro_novo_usuario(browser):
    criar_usuario(browser)
    assert "foi criada com sucesso" in browser.page_source

def test_login_valido(browser):
    criar_usuario(browser)
    realizar_login(browser)
    assert "home" in browser.current_url


def test_logout(browser):
    criar_usuario(browser)
    realizar_login(browser)

    browser.find_element(By.ID, "btnExit").click()
    WebDriverWait(browser, 10).until(EC.url_matches(URL_LOGIN_PAGE))

    assert browser.current_url == URL_LOGIN_PAGE

def test_acessar_pagina_usuario_sem_estar_autenticado(browser):
    browser.get(URL_USER_PROFILE)
    WebDriverWait(browser, 10).until(EC.url_matches(URL_LOGIN_PAGE))
    assert browser.current_url == URL_LOGIN_PAGE

