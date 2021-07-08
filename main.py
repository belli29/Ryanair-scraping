from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
import time
import csv


def scrap_ryanair():
    location = "C:/Users/Acer/PycharmProjects/web-scraping/chromedriver.exe"  # driver location
    driver = webdriver.Chrome(location)

    # user inputs
    from_validation = False
    to_validation = False
    ryanair_airports = {
        'BCN': 'Barcelona el Prat',
        'BGY': 'Orio Al Serio',

    }


    # IATA validation function
    def validate_airport(user_choice):
        try:
            ryanair_airports[user_choice]
            valid = True
        except KeyError :
            valid = False
        return valid


    # date format validation function
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

    # from airport validation loop
    while not from_validation:
        from_ = input('Where do you want to fly from ? '
                      '\n Please specify IATA code: ').upper()
        from_validation = validate_airport(from_)

    # to airport validation loop
    while not to_validation:
        to_ = input('Where do you want to fly to ? '
                    '\n Please specify IATA code: ').upper()
        to_validation = validate_airport(to_)
    # departure date validation loop
    departure = input('Where do you want to fly from ? \n Use this format yyyy-mm-dd')
    validate_departure_date(departure)

    #compose the url with validate user imput
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