from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# create_database import inserir_jogos



class Web:
    def __init__(self):
        self.site = 'https://www.amazon.com.br/b/ref=BrandfarmShoveler_2?pf_rd_r=627FVJNM32K95S2YX7EN&pf_rd_p=9b065bcc-48ad-481d-9a0c-300261eb155b&pf_rd_m=A1ZZFT5FULY4LN&pf_rd_s=merchandised-search-5&pf_rd_t=&pf_rd_i=16339926011&ie=UTF8&node=16364755011'
        self.map = {
            'marca': {
                'xpath': '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[31]/ul/li[$$]/span/a/span'
            },
            'modelo': {
                'xpath': '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[$$]/div/div/div/div/div[&]/div[1]/h2/a/span'
            },
            'preco': {
                'xpath': '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[$$]/div/div/div/div/div[&]/div[3]/div/a[1]/span/span[2]'
            }
        }
        self.driver = webdriver.Chrome()
        self.id = 0
        self.driver.get(self.site)
        sleep(2)

        for i in range(1, 5):
            self.marca = self.driver.find_element(By.XPATH, self.map['marca']['xpath'].replace('$$', f'{i}')).text
            if i == 1:
                print(self.marca)
                self.driver.find_element(By.XPATH, self.map['marca']['xpath'].replace('$$', f'{i}')).click()
                sleep(2)
                self.abrir()
            else:
                self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[4]/ul/li/span/a/span[2]")
                self.driver.find_element(By.XPATH, self.map['marca']['xpath'].replace('$$', f'{i}')).click()
                self.abrir()
            self.abrir()
            sleep(2)

    def abrir(self):
        for i in range(1, 10):
            try:
                if i == 1:
                    self.id = self.id + 1
                    print(self.id, end=": ")
                    print(self.marca, end=" - ")
                    modelo = self.driver.find_element(By.XPATH, self.map['modelo']['xpath'].replace('$$', f"{i}").replace("&", "3")).text
                    print(modelo, end=" - ")
                    preco = self.driver.find_element(By.XPATH, self.map['preco']['xpath'].replace('$$', f"{i}").replace("&", "3")).text
                    print(preco, end=" - ")
                    print()
                else:
                    self.id = self.id + 1
                    print(self.id, end=": ")
                    print(self.marca, end=" - ")
                    modelo = self.driver.find_element(By.XPATH, self.map['modelo']['xpath'].replace('$$', f"{i}").replace("&", "2")).text
                    print(modelo, end=" - ")
                    preco = self.driver.find_element(By.XPATH, self.map['preco']['xpath'].replace('$$', f"{i}").replace("&", "2")).text
                    print(preco, end=" - ")
                    print()
            except:
                pass


if __name__ == "__main__":
    w = Web()
