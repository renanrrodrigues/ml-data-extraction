from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions



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