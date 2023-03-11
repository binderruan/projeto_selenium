#Baixar o webdriver https://chromedriver.chromium.org/downloads
#pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1980,1020")
options.add_argument("--log-level=3")
#options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
login_url = 'https://quilombo.sc.gov.br/'

driver.get(login_url)
driver.implicitly_wait(10)


print('Passo 1: Fecha pop-up')

try:
    #Clica na janela de pop-up do IPTU
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="popmake-81771"]/button'))).click()
except:
    driver.quit()
    print('Erro ao fechar  pop-up do IPTU')
    quit()

print('Passo 2: Simular o mouse passando no menu Governo ')
try:

    # Simular o mouse passando no menu Governo
    action = ActionChains(driver)
    menu = driver.find_element(By.ID, "menu-item-15577")
    driver.implicitly_wait(20)
    action.move_to_element(menu).perform()

except:
    driver.quit()
    print('Erro ao passar o mouse em  Governo')
    quit()

print('Passo 3: Simular o mouse passando no menu Transparencia')
try:

    # Simular o mouse passando no menu transparencia
    action = ActionChains(driver)
    menu = driver.find_element(By.ID, "menu-item-2647")
    driver.implicitly_wait(20)
    action.move_to_element(menu).perform()

except:
    driver.quit()
    print('Erro ao passar o mouse em  Transparencia')
    quit()

print('Passo 4: Simular o mouse passando no menu Município \nPasso 5: Click em inicio')
try:

    # Simular o mouse passando no menu Municipio
    action = ActionChains(driver)
    menu = driver.find_element(By.ID, "menu-item-2558")
    driver.implicitly_wait(20)
    action.move_to_element(menu).perform()


    # Simular o click em  inicio
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'menu-item-1234'))).click()


except:
    driver.quit()
    print('Erro ao passar o mouse em  municipio e dar click em inicio')
    quit()

print('Passo 6: Busca o conteudo de informaçoes municipais')
try:
    elemento = driver.find_element(By.XPATH,'//*[@id="text-7"]/div[1]/table')
    conteudo_html = elemento.get_attribute('outerHTML')
    soup = BeautifulSoup(conteudo_html, 'html.parser')
    tabela = soup.find(name='table')
    print(tabela)

    #Salva como html
    with open('informacoes.html', 'w') as arquivo:
        arquivo.write(str(tabela))
    arquivo.close()

    #Salva como csv
    try:
        with open('informacoes.csv', 'w') as arquivo:
            for row in soup.find_all('tr'):
                line = ''
                for col in row.find_all('td'):
                    line = line + col.text.lstrip("\n").rstrip("\n") +';'
                arquivo.write(line+'\n')
        arquivo.close
    except:
        print('Erro ao salvar arquivo csv')
     
except:
    driver.quit()
    print('Erro ao acessar a tabela de informacoes municipais')
    quit()

driver.quit()
print('Atividade realizada com sucesso!')
