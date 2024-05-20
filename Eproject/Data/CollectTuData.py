from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd


path = r"D:\chromedriver-win64\chromedriver-win64\chromedriver.exe"
s = Service(path)
driver = webdriver.Chrome(service=s)
driver.get("https://www.tuiost.edu.np/notice")

tps= driver.find_elements(By.XPATH,r'//*[@id="notices"]/div/div/div/div/div/a/b')
lnks= driver.find_elements(By.XPATH,r'//*[@id="notices"]/div/div/div/div/div/a[@href]')
dts = driver.find_elements(By.XPATH,r'//*[@id="notices"]/div/div/div/div/div/small')

topics = []
links = []
dates = []

for data in tps:
    topics.append(data.text)

for data in dts:
     dates.append(data.text)

for data in lnks:
    link = data.get_attribute('href')
    links.append(link)


df=pd.DataFrame({'Date':dates,'Topic':topics,'Link':links})

df.to_csv('D:\E-Governance\Eproject\Tu_notice.csv',index=False)

print(df)