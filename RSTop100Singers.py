from selenium import webdriver
import pandas as pd


DRIVER_PATH = 'C:/Projects/Selenium/chromedriver/chromedriver.exe'
driver1 = webdriver.Chrome(executable_path=DRIVER_PATH)
driver2 = webdriver.Chrome(executable_path=DRIVER_PATH)

#open link with singers 51-100
driver1.get('https://www.rollingstone.com/music/music-lists/100-greatest-singers-of-all-time-147019/')
singers1 = driver1.find_elements_by_xpath('//h2[@class="c-gallery-vertical-album__title"]')

#open link with singers 1-50
driver2.get('https://www.rollingstone.com/music/music-lists/100-greatest-singers-of-all-time-147019/bonnie-raitt-6-48420/')
singers2 = driver2.find_elements_by_xpath('//h2[@class="c-gallery-vertical-album__title"]')

singer_list = []

#combine both lists and get text
singers = singers1 + singers2
for s in range(len(singers)):
    singer_list.append(singers[s].text)

driver1.close()
driver2.close()

#reverse list so it goes from 1 to 100
singer_list.reverse()

#create dataframe with index starting at 1
singerDF = pd.DataFrame({
'Singer': singer_list,
})
singerDF.index +=1

#save to CSV file
singerDF.to_csv('RSTop100Singers.csv')


