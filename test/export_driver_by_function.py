from time import sleep
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions


LINK = 'https://google.com.br'
LINK2 = 'https://bing.com.br'

def test_headless(product_name=None):
    options = EdgeOptions()
    #options.add_argument("--headless=false")

    driver = webdriver.Edge(options=options)
    driver.get(f'{LINK}')
    
    sleep(3)
    print('atapa 1')
    return driver




if __name__ == '__main__':
    driver = test_headless()
    
    driver.get(f'{LINK2}')
    
    sleep(3)
    print('atapa 2')
    driver.quit()