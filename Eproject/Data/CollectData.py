from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


path = r"D:\chromedriver-win64\chromedriver-win64\chromedriver.exe"
s = Service(path)
driver = webdriver.Chrome(service=s)
driver.get("https://moest.gov.np/category/7")

dt= driver.find_elements(By.XPATH,r'//*[@id="example"]/tbody/tr/td[1]')
tps= driver.find_elements(By.XPATH,r'//*[@id="example"]/tbody/tr/td[2]')
lnks = driver.find_elements(By.XPATH,r'//*[@id="example"]/tbody/tr/td[2]/a[@href]')
dates = []
topics = []
links = []
for data in dt[:20]:
    dates.append(data.text)

for data in tps[:20]:
    topics.append(data.text)

for data in lnks[:20]:
    link = data.get_attribute('href')
    driver.execute_script("window.open(arguments[0]);", link)
    driver.switch_to.window(driver.window_handles[1])
    # links.append(link)
    try:
        lPdf = driver.find_element(By.XPATH,r"/html/body/main/div/section[3]/div/div/div/div/div[1]/div/table/tbody/tr/td[3]/a[1]")
        #  pdf_element = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '.pdf')]"))
        
        # pdf_link = pdf_element.get_attribute('href')
        pdf = lPdf.get_attribute('href')  
        links.append(pdf)                       
    except:  
        print(f"PDF link not found for row ")
        continue

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)

df=pd.DataFrame({'Date':dates,'Topic':topics,'Link':links})

df.to_csv('D:\E-Governance\Eproject\schlr_notice.csv',index=False)

print(df)


