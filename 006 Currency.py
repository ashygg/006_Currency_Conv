intro = """Welcome to a simple currency converter!
This converter is based on data gathered on July 9, 2023.
As this is a project, please utilize a more updated converter for your needs.
This converter utilizes USD (United States Dollar) as the base currency. (It must be an input.)
The currencies available for conversion are:
"""
print(intro)

currencies = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'NZD', 'CNY', 'HKD', 'SGD', 'INR', 'MXN']
print(currencies)

from_convert = input("What currency would you like to convert from?: ").upper()
to_convert = input("What currency would you like to convert to?: ").upper()
amount = float(input("Enter the amount you would like to convert: "))

if not (from_convert in currencies):
    print("Please choose a currency listed or re-check your inputs.")
if not (to_convert in currencies):
    print("Please choose a currency listed or re-check your inputs.")

# conversions start here
if from_convert == 'USD' and to_convert == 'EUR':
    USDEUR_conv = amount / 1.0970
    print("The converted amount is: "+str(USDEUR_conv))

if from_convert == 'EUR' and to_convert == 'USD':
    EURUSD_conv = amount * 1.0970
    print("The converted amount is: "+str(EURUSD_conv))

if from_convert == 'USD' and to_convert == 'JPY':
    USDJPY_conv = amount * 142.0830
    print("The converted amount is: "+str(USDJPY_conv))

if from_convert == 'JPY' and to_convert == 'USD':
    JPYUSD_conv = amount / 142.0830
    print("The converted amount is: "+str(JPYUSD_conv))

if from_convert == 'USD' and to_convert == 'GBP':
    USDGBP_conv = amount / 1.2838
    print("The converted amount is: "+str(USDGBP_conv))

if from_convert == 'GBP' and to_convert == 'USD':
    GBPUSD_conv = amount * 1.2838
    print("The converted amount is: "+str(GBPUSD_conv))

if from_convert == 'USD' and to_convert == 'AUD':
    USDAUD_conv = amount / 0.6691
    print("The converted amount is: "+str(USDAUD_conv))

if from_convert == 'AUD' and to_convert == 'USD':
    AUDUSD_conv = amount * 0.6691
    print("The converted amount is: "+str(AUDUSD_conv))

if from_convert == 'USD' and to_convert == 'NZD':
    USDNZD_conv = amount / 0.6213
    print("The converted amount is: "+str(USDNZD_conv))

if from_convert == 'NZD' and to_convert == 'USD':
    NZDUSD_conv = amount * 0.6213
    print("The converted amount is: "+str(NZDUSD_conv))

if from_convert == 'USD' and to_convert == 'CNY':
    USDCNY_conv = amount * 7.2203
    print("The converted amount is: "+str(USDCNY_conv))

if from_convert == 'CNY' and to_convert == 'USD':
    CNYUSD_conv = amount / 7.2203
    print("The converted amount is: "+str(CNYUSD_conv))

if from_convert == 'USD' and to_convert == 'HKD':
    USDHKD_conv = amount * 7.8266
    print("The converted amount is: "+str(USDHKD_conv))

if from_convert == 'HKD' and to_convert == 'USD':
    HKDUSD_conv = amount / 7.8266
    print("The converted amount is: "+str(HKDUSD_conv))

if from_convert == 'USD' and to_convert == 'SGD':
    USDSGD_conv = amount * 1.3462
    print("The converted amount is: "+str(USDSGD_conv))

if from_convert == 'SGD' and to_convert == 'USD':
    SGDUSD_conv = amount / 1.3462
    print("The converted amount is: "+str(SGDUSD_conv))

if from_convert == 'USD' and to_convert == 'INR':
    USDINR_conv = amount * 82.5770
    print("The converted amount is: "+str(USDINR_conv))

if from_convert == 'INR' and to_convert == 'USD':
    INRUSD_conv = amount / 82.5770
    print("The converted amount is: "+str(INRUSD_conv))

if from_convert == 'USD' and to_convert == 'MXN':
    USDMXN_conv = amount * 17.1100
    print("The converted amount is: "+str(USDMXN_conv))

if from_convert == 'MXN' and to_convert == 'USD':
    MXNUSD_conv = amount / 17.1100
    print("The converted amount is: "+str(MXNUSD_conv))