# money converter 
currency=["usd,euro,pound"]
currency2=int(input("enter the currency you want to convert"))
eurotopkr=326.54
usdtopkr=280.4
poundtopkr=373.83
usdintopkr=usdtopkr*currency2
poundintopkr=poundtopkr*currency2
eurointopkr=eurotopkr*currency2
print("the conversion rate is",usdintopkr , eurointopkr,poundintopkr)
 

USD_TO_EUR = 0.93
USD_TO_GBP = 0.79
EUR_TO_USD = 1.08
EUR_TO_GBP = 0.85
GBP_TO_USD = 1.27
GBP_TO_EUR = 1.18

def convert(amount, from_currency, to_currency):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    # If the currencies are the same, return the amount unchanged
    if from_currency == to_currency:
        return amount

    # Conversion table 
    rates = {
        ("USD", "EUR"): USD_TO_EUR,
        ("USD", "GBP"): USD_TO_GBP,
        ("EUR", "USD"): EUR_TO_USD,
        ("EUR", "GBP"): EUR_TO_GBP,
        ("GBP", "USD"): GBP_TO_USD,
        ("GBP", "EUR"): GBP_TO_EUR,
    }

    try:
        rate = rates[(from_currency, to_currency)]
        return amount * rate
    except KeyError:
        print("Invalid currency selection.")
        return None

# --- Main Program ---
print("Currency Converter (USD, GBP, EUR)")
amount = float(input("Enter amount: "))
from_curr = input("Convert FROM (USD/GBP/EUR): ")
to_curr = input("Convert TO (USD/GBP/EUR): ")

result = convert(amount, from_curr, to_curr)

if result is not None:
    print(f"{amount} {from_curr.upper()} = {result:.2f} {to_curr.upper()}")


usd=int(input("enter usd "))
pkr=278
print(usd*pkr)

def usd_to_pkr():
    print(usd*pkr)

euro=int(input("enter euro "))
pkr2= 326
print(euro*pkr2)

gbp=int(input("enter gbp"))
pkr3= 373
print(gbp*pkr3)

if usd == ("amount entered in",):
    print= usd ("usd is equals to "), (usd*pkr)