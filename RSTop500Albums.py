from selenium import webdriver
import pandas as pd


DRIVER_PATH = 'C:/Projects/Selenium/chromedriver/chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

linkEndings = ["", "linda-mccartney-and-paul-ram-1062783/", "the-go-gos-beauty-and-the-beat-1062833/",
               "stevie-wonder-music-of-my-mind-2-1062883/", "shania-twain-come-on-over-1062933/",
               "whitney-houston-whitney-houston-2-1062984/", "sade-diamond-life-1063033/",
               "bruce-springsteen-nebraska-3-1063083/", "the-band-music-from-big-pink-2-1063133/",
               "jay-z-the-blueprint-3-1063183/"]


main_text = []
sub_text = []
#accesses each page of 50 albums
for l in linkEndings:
    main = []
    sub = []
    link = "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/" + l
    driver.get(link)
    main += driver.find_elements_by_xpath('//h2[@class="c-gallery-vertical-album__title"]')
    sub += driver.find_elements_by_xpath('//div[@class="c-gallery-vertical-album__subtitle"]')
    for i in range(len(main)):
        main_text.append(main[i].text)
        sub_text.append(sub[i].text)
driver.close()

titles = []
artists = []
#splits title and artist
for j in main_text:
    s = j.split(", ")
    titles.append(s[1])
    artists.append(s[0])

labels = []
years = []
#splits label and year
for k in sub_text:
    s = k.split(", ")
    labels.append(s[0])
    years.append(s[1])

#reverses lists so they go from 1 to 500
titles.reverse()
artists.reverse()
labels.reverse()
years.reverse()

#create dataframe with index starting at 1
albumDF = pd.DataFrame({
'Album': titles,
'Artist(s)': artists,
'Release Year': years,
'Label' : labels,
})
albumDF.index +=1

#save to CSV file
albumDF.to_csv('RSTop500Albums.csv')
