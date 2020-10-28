import json
import csv
from functools import reduce

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
regions = {"10000001":"Derelik", "10000002":"The Forge", "10000003":"Vale of the Silent", "10000005":"Detorid", "10000006":"Wicked Creek", "10000007":"Cache", "10000008":"Scalding Pass", "10000009":"Insmother", "10000010":"Tribute", "10000011":"Great Wildlands", "10000012":"Curse", "10000013":"Malpais", "10000014":"Catch", "10000015":"Venal",
           "10000016":"Lonetrek", "10000018":"The Spire", "10000020":"Tash-Murkon", "10000021":"Outer Passage","10000022":"Stain", "10000023":"Pure Blind", "10000025":"Immensea", "10000027":"Etherium Reach", "10000028":"Molden Heath", "10000029":"Geminate", "10000030":"Heimatar", "10000031":"Impass", "10000032":"Sinq Laison", "10000033":"The Citadel",
           "10000034":"The Kalevala Expanse", "10000035":"Deklein", "10000036":"Devoid", "10000037":"Everyshore", "10000038":"The Bleak Lands", "10000039":"Esoteria", "10000040":"Oasa", "10000041":"Syndicate", "10000042":"Metropolis", "10000043":"Domain", "10000044":"Solitude", "10000045":"Tenal", "10000046":"Fade", "10000047":"Providence",
           "10000048":"Placid", "10000049":"Khanid", "10000050":"Querious", "10000051":"Cloud Ring", "10000052":"Kador", "10000053":"Cobalt Edge", "10000054":"Aridia", "10000055":"Branch", "10000056":"Feythabolis", "10000057":"Outer Ring", "10000058":"Fountain", "10000059":"Paragon Soul", "10000060":"Delve", "10000061":"Tenerifis",
           "10000062":"Omist", "10000063":"Period Basis", "10000064":"Essence", "10000065":"Kor-Azor", "10000066":"Perrigen Falls", "10000067":"Genesis", "10000068":"Verge Vendor", "10000069":"Black Rise"}

def flattener(left, right):
    try:
        res = reduce(flattener, right, left)
    except TypeError:
        left.append(right)
        res = left
    return res


def flatten(seq):
    return reduce(flattener, seq, [])

def writer(target, tbw):
    with open(target, 'w') as outfile:
        json.dump(tbw, outfile)

def main(start, end):
    tail1 = "SuperRattingChars"
    tail2 = False
    tail3 = False
    csvfile = open("outputCombined.csv","w",newline = "")
    spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    names = sorted(list(regions.values()))
    print(names)
    inter = []
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
                    name = str(year) + str(month)+tail1+".json"
                    json_data = open(name).read()
                    data1 = json.loads(json_data)
                    if tail2:
                        name = str(year) + str(month)+tail2+".json"
                        json_data = open(name).read()
                        data2 = json.loads(json_data)#
                    if tail3:
                        name = str(year) + str(month)+tail3+".json"
                        json_data = open(name).read()
                        data3 = json.loads(json_data)
                    final = []
                    for key,val in data1.items():
                        flat = flatten(val)
                        list1 = list(set(flat))
                        final.extend(list1)
                        if tail2:
                            val2 = data2[key]
                            flat = flatten(val2)
                            list2 = list(set(flat))
                            final.extend(list2)
                        if tail3:
                            val3 = data3[key]
                            flat = flatten(val3)
                            list3 = list(set(flat))
                            final.extend(list3)
                        final = list(set(final))
                    spamwriter.writerow([str(year) + str(month), len(final)])
                    inter.extend(final)
                    inter = list(set(inter))

        else:
            pass
    print(inter)
    print(len(inter))
    writer("inter.json",inter)


main([2017], [2020,"jan"])
