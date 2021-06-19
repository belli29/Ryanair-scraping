from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

def scrap_ryanair():
    location = "C:/Users/Acer/PycharmProjects/web-scraping/chromedriver.exe"  # driver location
    driver = webdriver.Chrome(location)
    home_url = "https://www.ryanair.com/"
    driver.get(home_url)
    page = BeautifulSoup(driver.page_source, 'html.parser')
    cookies_window = driver.find_element_by_class_name('cookie-popup-with-overlay__button')
    cookies_window.click()
    while True:
        pass




if __name__ == '__main__':
    scrap_ryanair()