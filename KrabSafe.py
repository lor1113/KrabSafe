import requests
import json
groupids = [883,463,941,1283,101,543]
regions = [10000001,10000002,10000003,10000004,10000005,10000006,10000007,10000008,10000009,10000010,10000011,10000012,10000013,10000014,10000015,10000016,10000017,10000018,10000019,10000020,10000021,10000022,10000023,10000025,10000027,10000028,10000029,10000030,10000031,10000032,10000033,10000034,10000035,10000036,10000037,10000038,10000039,10000040,10000041,10000042,10000043,10000044,10000045,10000046,10000047,10000048,10000049,10000050,10000051,10000052,10000053,10000054,10000055,10000056,10000057,10000058,10000059,10000060,10000061,10000062,10000063,10000064,10000065,10000066,10000067,10000068,10000069]
regionv = [0,0]
years = [2019]
months = ['aug']
regionNames = ['Derelik','The Forge',' Vale of the Silent',' UUA-F',' Detorid',' Wicked Creek',' Cache',' Scalding Pass',' Insmother',' Tribute',' Great Wildlands',' Curse',' Malpais',' Catch',' Venal',' Lonetrek',' JHZ-F',' The Spire',' A-A',' Tash-Murkon',' Outer Passage',' Stain',' Pure Blind',' Immensea',' Etherium Reach',' Molden Heath',' Geminate',' Heimatar',' Impass',' Sinq Laison',' The Citadel',' The Kalevala Expanse',' Deklein',' Devoid',' Everyshore',' The Bleak Lands',' Esoteria',' Oasa',' Syndicate',' Metropolis',' Domain',' Solitude',' Tenal',' Fade',' Providence',' Placid',' Khanid',' Querious',' Cloud Ring',' Kador',' Cobalt Edge',' Aridia',' Branch',' Feythabolis',' Outer Ring',' Fountain',' Paragon Soul',' Delve',' Tenerifis',' Omist',' Period Basis',' Essence',' Kor-Azor',' Perrigen Falls',' Genesis',' Verge Vendor',' Black Rise']
headers = {'Accept-Encoding': 'gzip','User-Agent': '/u/Lorzonic'}
regionvalues = []
value = 0

def writer(target,tbw):
    with open(target,'w') as outfile:
        json.dump(tbw,outfile)

for year in years:
    for idx,month in enumerate(months):
        for region in regions:
            print(region)
            for group in groupids:
                print(group)
                response = requests.get('https://zkillboard.com/api/losses/groupID/' + str(group) + '/regionID/' + str(
                    region) + '/year/'+ str(year) +'/month/'+ str(idx+8) +'/npc/0/', headers=headers)
                try:
                    r = response.json()
                    for each in r:
                        if each['zkb']['awox'] == False:
                            value = value + each['zkb']['totalValue']
                    regionv.append(value)
                    value = 0
                except:
                    print("ZKILL FUCKED UP")
            regionvalues.append(sum(regionv))
            regionv = []
        mydict = dict(zip(regionNames, regionvalues))
        print(mydict)
        writer(str(year)+month + '.json', mydict)
        regionvalues = []














