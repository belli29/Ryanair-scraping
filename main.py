from bs4 import BeautifulSoup
from selenium import webdriver
import datetime


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

    # from airport validation loop
    from_ = input('Where do you want to fly from ? '
                  '\n Please specify IATA code: ')
    while not from_.upper() in ryanair_airports.__iter__():
        from_ = input('Wrong IATA code\n'
                      'please specify where you want to fly from: ')
    # to airport validation loop
    to_ = input('Where do you want to fly to ? '
                  '\n Please specify IATA code: ')
    while not to_.upper() in ryanair_airports.__iter__():
        to_ = input('Wrong IATA code\n'
                      'Please specify where you want to fly to: ')
    # departure destination loop
    departure =input('When do you want to fly?\n'
                     'Use format YYYY-MM-DD: ')
    while True:
        try:
            datetime.datetime.strptime(departure, '%Y-%m-%d')
            break
        except:
            departure = input('Wrong format\n'
                              'Please use format YYYY-MM-DD: ')

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
    cheapest_day = min(fares, key=fares.get)
    selected_day = list(fares.keys())[2]
    print(f'On {selected_day} the cheapest flight from {ryanair_airports[from_.upper()]} to {ryanair_airports[to_.upper()]} costs Eur {fares[selected_day]}')
    if (cheapest_day != selected_day) and (fares[cheapest_day] != fares[selected_day]):
        print(f'Hey, there is actually a cheaper flight on {cheapest_day} at Eur {fares[cheapest_day]}')
    else:
        print('In nearby days no cheaper rate can be found')

if __name__ == '__main__':
    scrap_ryanair()