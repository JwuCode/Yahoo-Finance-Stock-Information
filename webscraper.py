from bs4 import BeautifulSoup
import requests

def currentStockPrices(stock, index=0):
    print('starting search on '+ stock)
    url = 'https://ca.finance.yahoo.com/quote/' + stock + '?p=' + stock + '&.tsrc=fin-srch'
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' }
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'lxml')
    currentPrice = soup.find("fin-streamer", {"class": "Fw(b) Fz(36px) Mb(-4px) D(ib)"})
    try:
        currentPriceText = currentPrice.get_text()
    except:
        currentPriceText = "nonefound"
    try:
        afterhoursPrice = soup.find("fin-streamer", {"class": "C($primaryColor) Fz(24px) Fw(b)"})
        afterhoursPriceText = afterhoursPrice.get_text()
    except:
        afterhoursPriceText = "none"
    return(currentPriceText, afterhoursPriceText, index)


def findStockIndex(stocks, query):
    low = 0
    high = len(stocks) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if stocks[mid] < query:
            low = mid + 1
        elif stocks[mid] > query:
            high = mid - 1
        else:
            return mid
    return -1
