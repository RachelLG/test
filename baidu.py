from selenium import webdriver
driver = webdriver.Firefox()

driver.get("https://www.baidu.com/")

driver.find_element_by_id("kw").send_keys("selenium")
#driver.find_element_by_xpath("/html/body/div/div/div/div/div/form/span/input").send_keys("selenium")
#driver.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")
driver.find_element_by_id("su").click()