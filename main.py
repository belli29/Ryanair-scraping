from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
from selenium.webdriver.common.keys import Keys
import time

def scrap_ryanair():
    location = "C:/Users/Acer/PycharmProjects/web-scraping/chromedriver.exe"  # driver location
    driver = webdriver.Chrome(location)

    # user inputs
    from_ = "BCN"
    to_ = "BGY"
    departure = "2021-06-22"
    arrival = "2021-06-24"

    def compose_url(from_,to_,arrival,departure):
        home_url = "https://www.ryanair.com/en/en/"
        url = f"{home_url}trip/flights/select?adults=1&teens=0&children=0&infants=0&dateOut={departure}&dateIn={arrival}&isConnectedFlight=false&isReturn=true&discount=0&promoCode=&originIata={from_}&destinationIata={to_}&tpAdults=1&tpTeens=0&tpChildren=0&tpInfants=0&tpStartDate={departure}&tpEndDate={arrival}&tpDiscount=0&tpPromoCode=&tpOriginIata={from_}&tpDestinationIata={to_}"
        return url

    driver.get(compose_url(from_, to_, arrival, departure))

    while True:
        pass




if __name__ == '__main__':
    scrap_ryanair()