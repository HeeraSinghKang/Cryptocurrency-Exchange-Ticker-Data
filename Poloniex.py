import urllib.request, json 
with urllib.request.urlopen("https://poloniex.com/public?command=returnTicker") as url:
    prices = json.loads(url.read().decode())
    data = {}
    data["BTC"]=[]
    data["USDT"]=[]
    data["XMR"]=[]
    data["ETH"]=[]
    data["USDC"]=[]
    for var in prices:
        if var.startswith("BTC") :   
            data['BTC'].append({  
            'COIN': var[4:],
            'PRICE': float(prices[var]['last'])
            }) 
        elif var.startswith("USDT") :   
            data['USDT'].append({  
            'COIN': var[5:],
            'PRICE': float(prices[var]['last'])
            })
        elif var.startswith("XMR") :   
            data['XMR'].append({  
            'COIN': var[4:],
            'PRICE': float(prices[var]['last'])
            }) 
        elif var.startswith("ETH") :   
            data['ETH'].append({  
            'COIN': var[4:],
            'PRICE': float(prices[var]['last'])
            })  
        elif var.startswith("USDC") :   
            data['USDC'].append({  
            'COIN': var[5:],
            'PRICE': float(prices[var]['last'])
            }) 
    
    with open('poloniex.json', 'w') as outfile:  
        json.dump(data, outfile)
