**API Key**
The API has a unique identifier as an API key that gets passed into the API as an URL parameter access_key. This parameter serves as a unique identifying authentication with the Exchangerates API.

**Base URL:**

https://api.exchangeratesapi.io/v1/
Append your API Key: See an example of how to authenticate the Exchangerates API with the access_key parameter:

https://api.exchangeratesapi.io/v1/latest
    ? access_key = API_KEY

The delivered exchange rates with the API, are by default connected to the Euro. The data gets returned in a standard JSON format and easily can be reparsed in any programming language.

The api endpoint we are using for the code is the Exchangerates API's time series endpoint lets you query the API for daily historical rates between two dates of your choice, with a maximum time frame of 365 days(identified limitation).

**Requested parameters:**

Parameter	                Description
access_key	[required]         Your API Key.
start_date	[required]         The start date of your preferred timeframe.
end_date	[required]         The end date of your preferred timeframe.
base	    [optional]         Enter the three-letter currency code of your preferred base currency.
symbols	    [optional]         Enter a list of comma-separated currency codes to limit output currencies.


**API Response:**

```JSON
{
    "success": true,
    "timeseries": true,
    "start_date": "2012-05-01",
    "end_date": "2012-05-03",
    "base": "EUR",
    "rates": {
        "2012-05-01":{
          "USD": 1.322891,
          "AUD": 1.278047,
          "CAD": 1.302303
        },
        "2012-05-02": {
          "USD": 1.315066,
          "AUD": 1.274202,
          "CAD": 1.299083
        },
        "2012-05-03": {
          "USD": 1.314491,
          "AUD": 1.280135,
          "CAD": 1.296868
        },
        [...]
    }
}
```


The code consists of 2 functions:

    **fetch_exchange_rates**: The function provides the exchange rates using the above API

    **analyze_rates**: The function is to perform data analysis on the extracted exchange rates data and identify
                        the max, min and average rates for the 30 day period.