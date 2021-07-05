from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
import time
import csv
from selenium.webdriver.common.keys import Keys

def scrap_ryanair():
    location = "C:/Users/Acer/PycharmProjects/web-scraping/chromedriver.exe"  # driver location
    driver = webdriver.Chrome(location)

    # user inputs
    from_ = input('Where do you want to fly from ?')
    to_ = input('Where do you want to fly to ?')
    departure = input('When do you want to fly to ? \n Use this format yyyy-mm-dd')

    def validate_departure_date(date_departure):
        validation = True
        while validation:
            try:
                datetime.datetime.strptime(date_departure, '%Y-%m-%d')
                validation = False
            except ValueError:
                date_departure = input('Incorrect data format, should be YYYY-MM-DD \n'
                                  'Where do you want to fly to ?')
                continue
        return date_departure

    validate_departure_date(departure)

    def compose_url(from_,to_,departure):
        home_url = "https://www.ryanair.com/en/en/"
        url = f"{home_url}trip/flights/select?adults=1&teens=0&children=0&infants=0&dateOut={departure}&dateIn=&isConnectedFlight=false&isReturn=false&discount=0&promoCode=&originIata={from_}&destinationIata={to_}&tpAdults=1&tpTeens=0&tpChildren=0&tpInfants=0&tpStartDate={departure}&tpEndDate=&tpDiscount=0&tpPromoCode=&tpOriginIata={from_}&tpDestinationIata={to_}"
        return url

    # get the desired url
    driver.get(compose_url(from_, to_, departure))
    # close cookies popup window
    driver.find_element_by_class_name('cookie-popup-with-overlay__button').click()
    # parse the page
    results_page = BeautifulSoup(driver.page_source, 'html.parser')
    # find dates and fares
    fares = {}
    results =results_page.findAll('carousel-item', attrs = {'class' : 'ng-star-inserted'})
    for result in results:
        # find price
        price_integer = result.find('span', attrs = {'class': 'price__integers'})
        price_decimals = result.find('span', attrs = {'class': 'price__decimals'})
        price = price_integer.text.strip() + '.' + price_decimals.text.strip()
        # find date
        date_day = result.find('span', attrs ={'class': 'date-item__day-of-month'})
        date_month = result.find('span', attrs ={'class': 'date-item__month'})
        date = date_day.text.strip() + ' ' + date_month.text.strip()
        # add entry
        fares[date] = price
    print(fares)
    while True:
        pass

if __name__ == '__main__':
    scrap_ryanair()