import urllib.request, json 
with urllib.request.urlopen("https://www.binance.com/api/v3/ticker/price") as url:
    prices = json.loads(url.read().decode())
    data = {}
    data["BTC"]=[]
    data["USDC"]=[]
    data["PAX"]=[]
    data["TUSD"]=[]
    data["BNB"]=[]
    data["ETH"]=[]
    data["USDT"]=[]
    data["XRP"]=[]
    for var in prices:
        if var['symbol'].endswith("BTC") :   
            data['BTC'].append({  
            'COIN': var['symbol'][:-3],
            'PRICE': float(var['price'])
            }) 
        elif var['symbol'].endswith("USDC") :  
            data['USDC'].append({  
            'COIN': var['symbol'][:-4],
            'PRICE': float(var['price'])
            })  
        elif var['symbol'].endswith("PAX") :   
            data['PAX'].append({  
            'COIN': var['symbol'][:-3],
            'PRICE': float(var['price'])
            }) 
        elif var['symbol'].endswith("TUSD") :    
            data['TUSD'].append({  
            'COIN': var['symbol'][:-4],
            'PRICE': float(var['price'])
            })
        elif var['symbol'].endswith("BNB") : 
            data['BNB'].append({  
            'COIN': var['symbol'][:-3],
            'PRICE': float(var['price'])
            })   
        elif var['symbol'].endswith("ETH") : 
            data['ETH'].append({  
            'COIN': var['symbol'][:-3],
            'PRICE': float(var['price'])
            })   
        elif var['symbol'].endswith("USDT") :    
            data['USDT'].append({  
            'COIN': var['symbol'][:-4],
            'PRICE': float(var['price'])
            })
        elif var['symbol'].endswith("XRP") :    
            data['XRP'].append({  
            'COIN': var['symbol'][:-3],
            'PRICE': float(var['price'])
            })
    with open('binance.json', 'w') as outfile:  
        json.dump(data, outfile)
