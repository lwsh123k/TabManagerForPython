from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 避免程序运行结束后关闭浏览器！
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
# 指定Edge WebDriver的路径
edge_driver_path = './msedgedriver.exe'
driver = webdriver.Edge(options=options, service=webdriver.EdgeService(executable_path=edge_driver_path))

driver.get("http://www.python.org")
driver.switch_to.new_window()
driver.get("https://linkedin.com")
