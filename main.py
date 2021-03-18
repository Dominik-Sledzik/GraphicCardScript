import winsound
import time
from selenium import webdriver

soundDur = 4000
soundFreq = 440
#This is your path to the chromedriver on your PC
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.x-kom.pl/szukaj?q=3070&f%5Bgroups%5D%5B5%5D=1&sort_by=accuracy_desc&f%5Bcategories%5D%5B345%5D=1")

"""It's working kind of simple, after getting specific to specific website it checks for three things. Name of the product(graphic card), price and availability.
 saves those three values into variables then it saves those values into two-dimensional array and alerts you with sound if any card is available. """
while 1:
    cardName = driver.find_elements_by_class_name('sc-1yu46qn-11')
    cardPrices = driver.find_elements_by_class_name('hNZEsQ')
    cardAvailable = driver.find_elements_by_class_name('geHfky')

    cards = []
    for i in range(len(cardName)):
        currentCardName = cardName[i].get_attribute("title")[23:-9]
        currentCardPrice = cardPrices[i].get_attribute("innerHTML")
        currentCardAvailable = cardAvailable[i].is_enabled()
        cards.append([currentCardName, currentCardPrice, currentCardAvailable])
        if currentCardAvailable:
            print(f'{currentCardName} is Available for {currentCardPrice} !!!')
            winsound.Beep(soundFreq,soundDur)
    
    time.sleep(300)
    driver.refresh()