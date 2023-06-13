from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains
from create_database import inserir_produtos, deletar_produtos



class Web:
    def __init__(self):
        self.site = 'https://www.magazineluiza.com.br/'
        self.map = {
            'marca': {
                'xpath': '/html/body/div[2]/div/main/section[1]/div[2]/header/div/div[3]/nav/ul/li[7]/div[2]/div/div/div[1]/ul/li[$$]/a'
            },
            'modelo': {
                'xpath': '/html/body/div[2]/div/main/section[4]/div[2]/div/ul/li[$$]/a/div[3]/h2'
            },
            'preco_promo': {
                'xpath': '/html/body/div[2]/div/main/section[4]/div[2]/div/ul/li[$$]/a/div[3]/div[2]/div/p[2]'
            },
            'preco': {
                'xpath': '/html/body/div[2]/div/main/section[4]/div[2]/div/ul/li[$$]/a/div[3]/div/div/p[1]'
            }
        }

    def webscraping(self):
        deletar_produtos()
        self.driver = webdriver.Chrome()
        self.id = 0
        self.driver.get(self.site)
        sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/a[1]").click()
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div/main/section[1]/div[2]/header/div/div[2]/div[4]/div[2]/div/div").click()
        sleep(2)
        self.driver.refresh()
        for i in range(1, 6):
            sleep(2)
            informatica = self.driver.find_element(By.XPATH,
                                                   "/html/body/div[2]/div/main/section[1]/div[2]/header/div/div[3]/nav/ul/li[7]/div[1]")
            ActionChains(self.driver).move_to_element(informatica).perform()
            sleep(2)

            if i == 1:
                self.marca = self.driver.find_element(By.XPATH, self.map['marca']['xpath'].replace('$$', f'{i}')).text
                print(self.marca)
                self.driver.find_element(By.XPATH, self.map['marca']['xpath'].replace('$$', f'{i}')).click()
                sleep(2)
                self.abrir()
            else:
                self.marca = self.driver.find_element(By.XPATH,
                                                      self.map['marca']['xpath'].replace('$$', f'{i + 2}')).text
                print(self.marca)
                self.driver.find_element(By.XPATH, self.map['marca']['xpath'].replace('$$', f'{i + 2}')).click()
                sleep(2)
                self.abrir()
            sleep(2)

    def abrir(self):
        sleep(5)
        for i in range(1, 11):
            try:
                self.id = self.id + 1
                print(self.id, end=": ")
                print(self.marca, end=" - ")
                self.modelo = self.driver.find_element(By.XPATH, self.map['modelo']['xpath'].replace('$$', f"{i}")).text
                print(self.modelo, end=" - ")
                preco = self.driver.find_element(By.XPATH, self.map['preco_promo']['xpath'].replace('$$', f"{i}")).text
                print(preco, end=" - ")
                print()
            except:
                preco = self.driver.find_element(By.XPATH, self.map['preco']['xpath'].replace('$$', f"{i}")).text
                print(preco, end=" - ")
                print()
            inserir_produtos(self.id, self.modelo.replace("'", "”"), preco, self.marca)
        self.driver.back()