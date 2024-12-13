import requests

def convert_currency(amount, from_currency, to_currency, api_key="your_exchange_rate_api_key"):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        rates = response.json()['conversion_rates']
        if to_currency in rates:
            converted_amount = amount * rates[to_currency]
            print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            print("Currency not found.")
    else:
        print("API request failed.")

convert_currency(100, "USD", "EUR")
