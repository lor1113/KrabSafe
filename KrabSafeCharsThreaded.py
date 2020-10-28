import requests
import json
import time
import random
from multiprocessing import Pool
from requests_html import HTMLSession
from itertools import cycle

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
factions = [500012, 500025, 500010, 500019, 500011, 500020, 500021]
regions = [10000001, 10000002, 10000003, 10000005, 10000006, 10000007, 10000008, 10000009, 10000010, 10000011, 10000012, 10000013, 10000014, 10000015,
           10000016, 10000018, 10000020, 10000021, 10000022, 10000023, 10000025, 10000027, 10000028, 10000029, 10000030, 10000031, 10000032, 10000033,
           10000034, 10000035, 10000036, 10000037, 10000038, 10000039, 10000040, 10000041, 10000042, 10000043, 10000044, 10000045, 10000046, 10000047,
           10000048, 10000049, 10000050, 10000051, 10000052, 10000053, 10000054, 10000055, 10000056, 10000057, 10000058, 10000059, 10000060, 10000061,
           10000062, 10000063, 10000064, 10000065, 10000066, 10000067, 10000068, 10000069]
headers = {'Accept-Encoding': 'gzip', 'User-Agent': 'Discord : Neuro#8416'}
miningShips = {463: "groupID", 543: "groupID", 32880: "shipTypeID", 1283: "groupID", 941: "groupID", 883: "groupID"}
transportShips = {902: "groupID", 513: "groupID", 380: "groupID", 28: "groupID", 1202: "groupID"}
rattingShips = {659: "groupID", 547: "groupID", 900: "groupID", 17918: "shipTypeID", 626: "shipTypeID", 645: "shipTypeID", 24700: "shipTypeID",
                17843: "shipTypeID", 12005: "shipTypeID", 17715: "shipTypeID", 33820: "shipTypeID", 17736: "shipTypeID"}

def get_proxies():
    session = HTMLSession()
    url = 'https://free-proxy-list.net/'
    data = session.get(url)
    proxies = []
    proxy = ""
    switch = 0
    for each in data.html.find("table > tbody > tr > td"):
        if switch == 1:
            proxy = proxy + ":" + each.text
            proxies.append(proxy)
            switch = 0
        else:
            if "." in each.text:
                proxy = each.text
                switch = 1
    return proxies

proxies = get_proxies()
random.shuffle(proxies)
proxy_pool = cycle(proxies)

def writer(target, tbw):
    with open(target, 'w') as outfile:
        json.dump(tbw, outfile)


def scrape(year, month, id, type, out,mining):
    for region in regions:
        sum = []
        page = 1
        block = 1
        cycle = 0
        url = "https://zkillboard.com/api/losses/" + str(type) + "/" + str(id) + "/regionID/" + str(region) + "/year/" + str(year) + "/month/" + str(
            month) + "/page/" + str(page) + "/npc/0/"
        while block == 1:
            try:
                response = requests.get(url, headers=headers)
                r = response.json()
                block = 0
            except:
                time.sleep(0.2)
                block = 1
                cycle = cycle + 1
        if mining:
            for each in r:
                sum.extend(parse2(each))
        else:
            for each in r:
                sum.extend(parse2(each))
        while len(r) == 200:
            print("LOOP")
            print(url)
            page = page + 1
            block = 1
            cycle = 0
            url = "https://zkillboard.com/api/losses/" + str(type) + "/" + str(id) + "/regionID/" + str(region) + "/year/" + str(
                year) + "/month/" + str(month) + "/page/" + str(page) + "/npc/0/"
            time.sleep(0.2)
            while block == 1:
                try:
                    response = requests.get(url, headers=headers)
                    r = response.json()
                    block = 0
                except:
                    time.sleep(0.2)
                    block = 1
                    cycle = cycle + 1
            if mining:
                for each in r:
                    sum.extend(parse2(each))
            else:
                for each in r:
                    sum.extend(parse2(each))
        if region in out.keys():
            out[region].extend(sum)
        else:
            out[region] = sum
    return out


def parse(kill):
    data = [kill["killmail_id"], kill['zkb']["hash"], kill["zkb"]["totalValue"]]
    url = "https://esi.evetech.net/latest/killmails/" + str(data[0]) + "/" + str(data[1]) + "/?datasource=tranquility"
    sum = []
    block0 = 1
    block1 = 1
    cycle = 0
    while block0 == 1:
        while block1 == 1:
            try:
                response = requests.get(url, headers=headers)
                r = response.json()
                block1 = 0
            except:
                time.sleep(0.2)
                block1 = 1
                cycle = cycle + 1
        if cycle > 10:
            print("Giving up on this one, Chief.")
            block1 = 0
            block0 = 0
        try:
            for each in r["attackers"]:
                try:
                    if each["faction_id"] in factions:
                        let = 1
                except:
                    pass
            block0 = 0
        except:
            time.sleep(0.1)
            block1 = 1
            cycle = cycle + 1
    if let == 1:
        for each in r["attackers"]:
            try:
                sum.append(each["character_id"])
            except:
                pass
    return sum

def parse2(kill):
    data = [kill["killmail_id"], kill['zkb']["hash"], kill["zkb"]["totalValue"]]
    url = "https://esi.evetech.net/latest/killmails/" + str(data[0]) + "/" + str(data[1]) + "/?datasource=tranquility"
    sum = []
    block0 = 1
    block1 = 1
    cycle = 0
    while block0 == 1:
        while block1 == 1:
            try:
                response = requests.get(url, headers=headers)
                r = response.json()
                block1 = 0
            except:
                time.sleep(0.2)
                block1 = 1
                cycle = cycle + 1
        if cycle > 0:
            print("ESI Failed " + str(cycle) + " times")
            if cycle > 10:
                print("Giving up on this one, Chief.")
                block1 = 0
                block0 = 0
        try:
            for each in r["attackers"]:
                try:
                    sum.append(each["character_id"])
                except:
                    pass
            block0 = 0
        except:
            time.sleep(0.1)
            block1 = 1
            cycle = cycle + 1
    if cycle > 0:
        print("ESI failed " + str(cycle) + " times")
    return sum

def main(start, end, mining):
    out = {}
    p = Pool(50)
    process = []
    if mining:
        ships = miningShips
        tail = "MiningChars"
    else:
        ships = rattingShips
        tail = "SuperRattingChars"
    years = list(range(start[0], end[0] + 1))
    if len(start) == 2:
        waste = months.index(start[1])
    else:
        waste = 0
    if len(end) == 2:
        stop = months.index(end[1])
        loop = 1
    else:
        stop = 12
        loop = 1
    for year in years:
        for month in months:
            if loop == 1:
                if year == years[-1]:
                    if months.index(month) == stop:
                        loop = 0
                if waste > 0:
                    waste = waste - 1
                else:
                    process.append([ships, year, month, tail,mining])
    print([[year[1],year[2]] for year in process])
    p.map(inter,process)

def inter(data):
    ships = data[0]
    year = data[1]
    month = data[2]
    tail = data[3]
    mining = data[4]
    out = {}
    for key, item in ships.items():
        print(key)
        out = scrape(year, months.index(month) + 1, key, item, out,mining)
    writer(str(year) + month + tail + ".json", out)
    print("MONTH FINISHED")
    print([year,month])


if __name__ == "__main__":
    main([2017], [2020,"jan"], False)