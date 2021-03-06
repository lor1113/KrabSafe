import json
import csv

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
regions = {"10000001":"Derelik", "10000002":"The Forge", "10000003":"Vale of the Silent", "10000005":"Detorid", "10000006":"Wicked Creek", "10000007":"Cache", "10000008":"Scalding Pass", "10000009":"Insmother", "10000010":"Tribute", "10000011":"Great Wildlands", "10000012":"Curse", "10000013":"Malpais", "10000014":"Catch", "10000015":"Venal",
           "10000016":"Lonetrek", "10000018":"The Spire", "10000020":"Tash-Murkon", "10000021":"Outer Passage","10000022":"Stain", "10000023":"Pure Blind", "10000025":"Immensea", "10000027":"Etherium Reach", "10000028":"Molden Heath", "10000029":"Geminate", "10000030":"Heimatar", "10000031":"Impass", "10000032":"Sinq Laison", "10000033":"The Citadel",
           "10000034":"The Kalevala Expanse", "10000035":"Deklein", "10000036":"Devoid", "10000037":"Everyshore", "10000038":"The Bleak Lands", "10000039":"Esoteria", "10000040":"Oasa", "10000041":"Syndicate", "10000042":"Metropolis", "10000043":"Domain", "10000044":"Solitude", "10000045":"Tenal", "10000046":"Fade", "10000047":"Providence",
           "10000048":"Placid", "10000049":"Khanid", "10000050":"Querious", "10000051":"Cloud Ring", "10000052":"Kador", "10000053":"Cobalt Edge", "10000054":"Aridia", "10000055":"Branch", "10000056":"Feythabolis", "10000057":"Outer Ring", "10000058":"Fountain", "10000059":"Paragon Soul", "10000060":"Delve", "10000061":"Tenerifis",
           "10000062":"Omist", "10000063":"Period Basis", "10000064":"Essence", "10000065":"Kor-Azor", "10000066":"Perrigen Falls", "10000067":"Genesis", "10000068":"Verge Vendor", "10000069":"Black Rise"}

def main(start, end, mining):
    csvfile = open("output.csv","w",newline = "")
    spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    if mining:
        tail = "Mining"
    else:
        tail = "RattingDrones"
    names = sorted(list(regions.values()))
    spamwriter.writerow(["Date"] + names)
    print(names)
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
                    name = str(year) + str(month)+tail+".json"
                    out = [None] * 64
                    json_data = open(name).read()
                    data = json.loads(json_data)
                    for key,val in data.items():
                        out[names.index(regions[key])] = val
                    time = [str(year) + " " + month]
                    spamwriter.writerow(time + out)

        else:
            pass


main([2017,"may"], [2020,"jan"],False)
