# Yahoo-Finance-Stock-Information
An API that pulls live stock information from Yahoo Finance, including the current price, afterhours price, previous close, and open.

## Routes
### /api/stocks/list?names= <br>
Argument: names <br>
Returns a list of stocks by stock code, separated with commas containing current price and afterhours price.

### /api/stocks/all <br>
Returns a list of all stock codes in the NASDAQ.

### /api/stocks?name= <br>
Argument: name <br>
Returns current price, afterhours price, previous close as well as open for a single stock.

### Example:
![alt text](https://user-images.githubusercontent.com/108997989/211698480-8589df39-51e4-4ab2-aaf1-26f55df3ef50.png)


