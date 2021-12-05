import requests
import json
with open('save/exchangelist.txt') as file:
    exchangelist=json.load(file)
with open('save/seachcoin.txt') as file:
    seachcoin=json.load(file)
with open('save/seachexchange.txt') as file:
    seachexchange=json.load(file)
with open('save/check.txt') as file:
    coinlist=json.load(file)
with open('save/coin.txt') as file:
    coin=json.load(file)
def ceate():
    y= {"btc":{"binance": 2, "bitkub": 1},"ada":{"binance": 16}}
    with open('coin.txt', 'w') as file:
        json.dump(y,file)

def ceatecoin(coina):
    global coinlist,coin
    coinlist.append(coina)
    with open('save/check.txt', 'w') as file:
        json.dump(coinlist,file)
    coin.update({coina:{}})
    with open('save/coin.txt', 'w') as file:
        json.dump(coin,file)


def getpriceeach(coina,exchange):
    global coin
    coina=coina.lower()
    exchange=exchange.lower()
    link = "https://api.coingecko.com/api/v3/exchanges/" + exchange + "/tickers"
    link = requests.get(link).text
    t = json.loads(link)
    return t['tickers'][coin[coina][exchange]]['converted_last']['usd']


def seachcoinfn(coin):
    coin=coin.lower()
    sum=0
    seachlist=[]
    for i in coin:
        sum+=ord(i)-97
    for i in seachcoin:
        if i['num']>sum-26 and i['num']<sum+26:
            listcheck=[]
            sume=0
            for j in coin:
                if j not in listcheck:
                    sume+=min(i['name'].count(j),coin.count(j))
                    listcheck.append(j)
            seachlist.append({'name':i['name'],'sume':sume/len(i['name'])})
    seachlist.sort(key=lambda d: d['sume'],reverse=True)
    return seachlist[:10]

def seachexchangefn(exchange):
    exchange=exchange.lower()
    sum=0
    seachlist=[]
    for i in exchange:
        if i != '_':
            a = ord(i)
            if a < 58:
                a = 0
            else:
                a = a - 97
            sum += a
    for i in seachexchange:
        if i['num']>sum-52 and i['num']<sum+52:
            listcheck=[]
            sume=0

            for j in exchange:
                if j not in listcheck:
                    sume+=min(i['name'].count(j),exchange.count(j))
                    listcheck.append(j)
            seachlist.append({'name':i['name'],'sume':sume/len(i['name'])})
    seachlist.sort(key=lambda d: d['sume'],reverse=True)
    return seachlist[:10]

def addmyexchange(exchange):
    exchange=exchange.lower()
    if exchange not in exchangelist:
        exchangelist.append(exchange)
        with open('save/exchangelist.txt', 'w') as file:
            json.dump(exchangelist,file)

    link = "https://api.coingecko.com/api/v3/exchanges/" + exchange + "/tickers"
    link = requests.get(link).text
    t = json.loads(link)
    for name in coinlist:
        dictlist = coin[name]
        for i in range(len(t["tickers"])):
            if t["tickers"][i]['base'] == name.upper() and (t["tickers"][i]['target'] == "USDT" or t["tickers"][i]['target'] == "THB"):
                dictlist.update({exchange: i})
    with open('save/coin.txt', "w") as file:
        json.dump(coin,file)

def addandupdatecoin(coina):
    global coinlist,coin
    coina = coina.lower()
    if coina not in coinlist:
        ceatecoin(coina)
    copy={}
    for exchange in exchangelist:
        link="https://api.coingecko.com/api/v3/exchanges/"+exchange+"/tickers"
        link = requests.get(link).text
        t = json.loads(link)
        for i in range(len(t["tickers"])):
            if t["tickers"][i]['base']==coina.upper() and (t["tickers"][i]['target']=="USDT"or t["tickers"][i]['target']=="THB"):
                copy.update({exchange:i})
    coin[coina]=copy
    with open('save/coin.txt', "w") as file:
        json.dump(coin,file)
