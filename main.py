from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
from selenium.webdriver.common.keys import Keys
import time

def scrap_ryanair():
    location = "C:/Users/Acer/PycharmProjects/web-scraping/chromedriver.exe"  # driver location
    driver = webdriver.Chrome(location)
    home_url = "https://www.ryanair.com/es/es"
    driver.get(home_url)
    page = BeautifulSoup(driver.page_source, 'html.parser')
    # accept cookies window
    cookies_window = driver.find_element_by_class_name('cookie-popup-with-overlay__button')
    cookies_window.click()

    # user inputs
    from_airport = "Berlin Brandenburg"
    to_airport = "Alicante"
    arrival = "10/2/25"
    departure = "13/2/29"

    # fill in fields
    fields = {'departure': from_airport, 'destination': to_airport, 'dates-from':arrival, 'dates-to':departure}

    # add user input departure and destination
    for field in fields:
        if field == 'dates-from':
            break
        # trigger displaying date fields
        element = driver.find_element_by_id("input-button__" + field)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(fields[field])
    # display date fields
    search_element = driver.find_element_by_class_name("flight-search-widget__start-search")
    search_element.click()
    while True:
        pass




if __name__ == '__main__':
    scrap_ryanair()