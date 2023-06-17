from time import sleep
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions


LINK = 'https://google.com.br'
LINK2 = 'https://bing.com.br'

# class TestHeadless:

class DriverEdge:
    def __init__(self):
        self.options = EdgeOptions()
        #self.options.add_argument("--headless=false")
        self.driver = webdriver.Edge(options=self.options)
    
    # get driver
    def get_driver(self):
        return self.driver
    
    # quit driver
    def quit_driver(self):
        self.driver.quit()
    



def test_headless(driver, link=None):
    driver.get(f'{link}')


if __name__ == '__main__':
    driver = DriverEdge().get_driver() # objeto driver
    test_headless(driver, link=LINK)
    sleep(3)
    print('atapa 2')
    test_headless(driver, link=LINK2)
    sleep(3)
    driver.quit()