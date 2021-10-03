import requests
import pandas as pd

tickers = ['AMT', 'LNG', 'MRK', 'LEVI', 'RIO']
#ticker can be any stock in your portfolio, or whatever you've been following lately
targets = []

for item in tickers:
    lhs_url = 'https://query2.finance.yahoo.com/v10/finance/quoteSummary/'
    rhs_url = '?formatted=true&crumb=swg7qs5y9UP&lang=en-US&region=US&' \
              'modules=upgradeDowngradeHistory,recommendationTrend,' \
              'financialData,earningsHistory,earningsTrend,industryTrend&' \
              'corsDomain=finance.yahoo.com'

    headers = {
        'User-Agent': ''}
    #Add your own user agent address - Just google it on your browser.
    url = lhs_url + item + rhs_url
    r = requests.get(url, headers=headers)
    result = r.json()['quoteSummary']['result'][0]
    target = result['financialData']['targetMeanPrice']['fmt']
    #If you want the median version, then replace 'targetMeanPrice' with 'targetMedianPrice'
    targets.append(target)

    print("--------------------------------------------")
    print("{} has an average target price of: ".format(item), target)

dataframe = pd.DataFrame(list(zip(tickers, targets)), columns=['Company', 'Mean Target Price'])
dataframe = dataframe.set_index('Company')
dataframe.to_csv('Target_Price.csv')
#to_excel in order to save it as a .xlsx file
print(dataframe)
