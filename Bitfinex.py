import urllib.request, json 
with urllib.request.urlopen("https://api.bitfinex.com/v2/tickers?symbols=ALL") as url:
    prices = json.loads(url.read().decode())
    data = {}
    data["USD"]=[]
    data["EUR"]=[]
    data["GBP"]=[]
    data["JPY"]=[]
    data["BTC"]=[]
    data["ETH"]=[]
    data["EOS"]=[]
    data["XLM"]=[]
    for var in prices:
        if var[0].endswith("USD") and var[0].startswith("t") :   
            data['USD'].append({  
            'COIN': var[0][1:-3],
            'PRICE': float(var[7])
            }) 
        elif var[0].endswith("EUR") and var[0].startswith("t") :  
            data['EUR'].append({  
            'COIN': var[0][1:-3],
            'PRICE': float(var[7])
            })  
        elif var[0].endswith("GBP") and var[0].startswith("t") :   
            data['GBP'].append({  
            'COIN': var[0][1:-3],
            'PRICE': float(var[7])
            }) 
        elif var[0].endswith("JPY") and var[0].startswith("t") :    
            data['JPY'].append({  
            'COIN': var[0][1:-3],
            'PRICE': float(var[7])
            })
        elif var[0].endswith("BTC") and var[0].startswith("t") : 
            data['BTC'].append({  
            'COIN': var[0][1:-3],
            'PRICE': float(var[7])
            })   
        elif var[0].endswith("ETH") and var[0].startswith("t") : 
            data['ETH'].append({  
            'COIN': var[0][1:-3],
            'PRICE': float(var[7])
            })   
        elif var[0].endswith("EOS") and var[0].startswith("t") :    
            data['EOS'].append({  
            'COIN': var[0][1:-3],
            'PRICE': float(var[7])
            })
        elif var[0].endswith("XLM") and var[0].startswith("t") :    
            data['XLM'].append({  
            'COIN': var[0][1:-3],
            'PRICE': float(var[7])
            })
    with open('bitfinex.json', 'w') as outfile:  
        json.dump(data, outfile )
