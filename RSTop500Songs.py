from selenium import webdriver
import pandas as pd


DRIVER_PATH = 'C:/Projects/Selenium/chromedriver/chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

linkEndings = ["", "bob-marley-and-the-wailers-i-shot-the-sheriff-161581/",
               "the-four-tops-baby-i-need-your-loving-170636/", "jimmy-cliff-the-harder-they-come-35805/",
               "led-zeppelin-black-dog-50226/", "sly-and-the-family-stone-hot-fun-in-the-summertime-56860/",
               "elvis-presley-dont-be-cruel-55974/", "the-everly-brothers-cathys-clown-63263/",
               "gnarls-barkley-crazy-40673/", "smokey-robinson-and-the-miracles-the-tracks-of-my-tears-56465/"]



main_text = []
#accesses each page of 50 albums
for l in linkEndings:
    main = []
    link = "https://www.rollingstone.com/music/music-lists/500-greatest-songs-of-all-time-151127/" + l
    driver.get(link)
    main += driver.find_elements_by_xpath('//h2[@class="c-gallery-vertical-album__title"]')
    for i in range(len(main)):
        main_text.append(main[i].text)
driver.close()

titles = []
artists = []
#splits title and artist
for j in main_text:
    s = j.split(", ")
    titles.append(s[1])
    artists.append(s[0])


#reverses lists so they go from 1 to 500
titles.reverse()
artists.reverse()


#create dataframe with index starting at 1
songDF = pd.DataFrame({
'Song': titles,
'Artist(s)': artists,
})
songDF.index +=1

#save to CSV file
songDF.to_csv('RSTop500Songs.csv')



