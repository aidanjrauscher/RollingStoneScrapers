from selenium import webdriver
import pandas as pd


DRIVER_PATH = 'C:/Projects/Selenium/chromedriver/chromedriver.exe'
driver1 = webdriver.Chrome(executable_path=DRIVER_PATH)
driver2 = webdriver.Chrome(executable_path=DRIVER_PATH)

#open link with artist 51-100
driver1.get('https://www.rollingstone.com/music/music-lists/100-greatest-artists-147446/')
artists1 = driver1.find_elements_by_xpath('//h2[@class="c-gallery-vertical-album__title"]')

#open link with artist 1-50
driver2.get('https://www.rollingstone.com/music/music-lists/100-greatest-artists-147446/the-band-2-88489/')
artists2 = driver2.find_elements_by_xpath('//h2[@class="c-gallery-vertical-album__title"]')

artist_list = []

#combine both lists and get text
artists = artists1+artists2
for a in range(len(artists)):
    artist_list.append(artists[a].text)

driver1.close()
driver2.close()

#reverse list so it goes from 1 to 100
artist_list.reverse()

#create dataframe with index starting at 1
artistDF = pd.DataFrame({
'Artist': artist_list,
})
artistDF.index +=1

#save to CSV file
artistDF.to_csv('RSTop100Artists.csv')


