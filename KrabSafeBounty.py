import requests
import json
allmonths = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
banned = [155,90,5]
esi_is_bad = 0
unknown = 0
aAll = []
output = []
attack =''
assumed_pve = 0
vAll = 0
flagListing = [0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 56, 57, 61, 62, 63, 64, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 115, 116, 117, 118, 119, 120, 121, 122, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 176, 177]
#shipids = [28665,28659,28661,28710,23917,22852,23919,23913,23757,23915,24483,23911,17918,12005,24700,645]
shipids = [23757,23915,24483,23911]
regions = [10000001,10000002,10000003,10000005,10000006,10000007,10000008,10000009,10000010,10000011,10000012,10000013,10000014,10000015,10000016,10000018,10000020,10000021,10000022,10000023,10000025,10000027,10000028,10000029,10000030,10000031,10000032,10000033,10000034,10000035,10000036,10000037,10000038,10000039,10000040,10000041,10000042,10000043,10000044,10000045,10000046,10000047,10000048,10000049,10000050,10000051,10000052,10000053,10000054,10000055,10000056,10000057,10000058,10000059,10000060,10000061,10000062,10000063,10000064,10000065,10000066,10000067,10000068,10000069]
regionv = [0,0]
pvp = 0
pve = 0
modules = []
faulty_links = []
years = [2019]
months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
banlist = [527,526,4025,4027,14262,14264,14266,14268,14270,17500,17559,28514,41038,41054,41055,41056,41040,41057,40696,41059,41058,448,5439,5443,5445,14252,14254,14256,14258,14260,15887,15893,21512,28518,41061,447,3242,3244,5399,5403,5405,14242,14244,14246,14248,14250,15889,15891,21510,28516,41062,40659,40664,40660,40661,40662,40663,40636,12271,12269,14168,14170,15798,15804,37628,37629,37630,37631,16475,16477,23819]
regionNames = ['Derelik','The Forge',' Vale of the Silent',' Detorid',' Wicked Creek',' Cache',' Scalding Pass',' Insmother',' Tribute',' Great Wildlands',' Curse',' Malpais',' Catch',' Venal',' Lonetrek',' The Spire',' Tash-Murkon',' Outer Passage',' Stain',' Pure Blind',' Immensea',' Etherium Reach',' Molden Heath',' Geminate',' Heimatar',' Impass',' Sinq Laison',' The Citadel',' The Kalevala Expanse',' Deklein',' Devoid',' Everyshore',' The Bleak Lands',' Esoteria',' Oasa',' Syndicate',' Metropolis',' Domain',' Solitude',' Tenal',' Fade',' Providence',' Placid',' Khanid',' Querious',' Cloud Ring',' Kador',' Cobalt Edge',' Aridia',' Branch',' Feythabolis',' Outer Ring',' Fountain',' Paragon Soul',' Delve',' Tenerifis',' Omist',' Period Basis',' Essence',' Kor-Azor',' Perrigen Falls',' Genesis',' Verge Vendor',' Black Rise']
headers = {'Accept-Encoding': 'gzip','User-Agent': 'Ya boi Neuro'}
regionvalues = []
value = 0

def writer(target,tbw):
    with open(target,'w') as outfile:
        json.dump(tbw,outfile)

for year in years:
    for month in months:
        print(str(year) + ' ' + str(month))
        for region in regions:
            print(region)
            for ship in shipids:
                print(str(ship))
                try:
                    response = requests.get('https://zkillboard.com/api/losses/shipTypeID/' + str(ship) + '/regionID/' + str(region) + '/year/'+ str(year) +'/month/'+ str(allmonths.index(month)+1) +'/npc/0/', headers=headers)
                    r = response.json()
                except:
                    print('https://zkillboard.com/api/losses/shipTypeID/' + str(ship) + '/regionID/' + str(region) + '/year/'+ str(year) +'/month/'+ str(allmonths.index(month)) +'/npc/0/')
                    print('ZKILL FUCKED UP')
                    esi_is_bad = esi_is_bad + 1
                    print('FUCKUP COUNTER: ' + str(esi_is_bad))
                    unknown = unknown + 1
                for each in r:
                    if each['zkb']['awox'] == False:
                        try:
                            ESI = requests.get('https://esi.evetech.net/latest/killmails/'+str(each['killmail_id'])+'/'+each['zkb']['hash']+'/')
                            E = ESI.json()
                        except:
                            print('ESI FUCKED UP')
                            assumed_pve = assumed_pve + 1
                            print('FUCKUP COUNTER: ' + str(assumed_pve))
                            value = (0.833 * each['zkb']['totalValue'])
                            regionv.append(value)
                            value = 0

                        id = each['killmail_id']
                        flags = []
                        try:
                            vAll = [E['victim']['alliance_id']]
                        except:
                            vAll = -1
                        for attack in E['attackers']:
                            try:
                                yeet = attack   ['alliance_id']
                                aAll.append(yeet)
                            except KeyError:
                                pass
                        if vAll not in aAll:
                            for item in E['victim']['items']:
                                if item['flag'] not in banned:
                                    modules.append(item)
                            if all(item['item_type_id'] not in banlist for item in modules):
                                value = each['zkb']['totalValue']
                                regionv.append(value)
                                value = 0
                                pve = pve + 1
                                modules = []
                            else:
                                pvp = pvp +1
                                modules = []
                        else:
                            print('AWOX TIME')
                            print('https://zkilboard.com/kill/'+str(id))
            print('Sum = '+ str(sum(regionv)))
            regionvalues.append(sum(regionv))
            regionv = []
        mydict = dict(zip(regionNames, regionvalues))
        print(mydict)
        print('PVP = '+str(pvp))
        print('PVE = '+str(pve))
        print('Crashed, assmed PVE = '+str(assumed_pve))
        print('Zkill bad, crashed = ' + str(unknown))
        pvp = 0
        output.append(pve)
        pve = 0
        unknown = 0
        assumed_pve = 0
        print(str(year) + month + '_noPvP.json')
        #writer(str(year) + month + '_noPvP.json', mydict)
        regionvalues = []
print(output)













