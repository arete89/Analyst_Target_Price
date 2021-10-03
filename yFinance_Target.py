import requests
import pandas as pd

tickers = ['AMT', 'LNG', 'MRK', 'LEVI', 'RIO']
targets = []

for item in tickers:
    lhs_url = 'https://query2.finance.yahoo.com/v10/finance/quoteSummary/'
    rhs_url = '?formatted=true&crumb=swg7qs5y9UP&lang=en-US&region=US&' \
              'modules=upgradeDowngradeHistory,recommendationTrend,' \
              'financialData,earningsHistory,earningsTrend,industryTrend&' \
              'corsDomain=finance.yahoo.com'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}
    url = lhs_url + item + rhs_url
    r = requests.get(url, headers=headers)
    result = r.json()['quoteSummary']['result'][0]
    target = result['financialData']['targetMeanPrice']['fmt']

    targets.append(target)

    print("--------------------------------------------")
    print("{} has an average target price of: ".format(item), target)
    # time.sleep(0.5)

dataframe = pd.DataFrame(list(zip(tickers, targets)), columns=['Company', 'Mean Target Price'])
dataframe = dataframe.set_index('Company')
dataframe.to_csv('Target_Price.csv')

print(dataframe)