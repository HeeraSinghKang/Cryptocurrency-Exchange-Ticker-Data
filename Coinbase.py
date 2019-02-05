import urllib.request, json 
with urllib.request.urlopen("https://api.coinbase.com/v2/exchange-rates") as url:
    prices = json.loads(url.read().decode())
    prices=json.dumps(prices)
    prices=prices[38:-2]
    prices=json.loads(prices)
    print (prices)
    data = {}
    data["USD"]=[]
    for coin,price in prices.items():
        price=float(str(price))
        if price == 0 :
            data['USD'].append({  
            "COIN":str(coin) , "PRICE": price
            })
        else :
            data['USD'].append({  
            "COIN":str(coin) , "PRICE": 1/price
            }) 
    with open('coinbase.json', 'w') as outfile:  
        json.dump(data, outfile)
