import csv
import json
json_data = open('Master_Bounty.json').read()
cleanRegionNames = []
data = json.loads(json_data)
regionNames = ['Derelik','The Forge','Vale of the Silent','Detorid',' Wicked Creek',' Cache',' Scalding Pass',' Insmother',' Tribute',' Great Wildlands',' Curse',' Malpais',' Catch',' Venal',' Lonetrek',' The Spire',' Tash-Murkon',' Outer Passage',' Stain',' Pure Blind',' Immensea',' Etherium Reach',' Molden Heath',' Geminate',' Heimatar',' Impass',' Sinq Laison',' The Citadel',' The Kalevala Expanse',' Deklein',' Devoid',' Everyshore',' The Bleak Lands',' Esoteria',' Oasa',' Syndicate',' Metropolis',' Domain',' Solitude',' Tenal',' Fade',' Providence',' Placid',' Khanid',' Querious',' Cloud Ring',' Kador',' Cobalt Edge',' Aridia',' Branch',' Feythabolis',' Outer Ring',' Fountain',' Paragon Soul',' Delve',' Tenerifis',' Omist',' Period Basis',' Essence',' Kor-Azor',' Perrigen Falls',' Genesis',' Verge Vendor',' Black Rise']

def compile():
    with open('Bounty_CSV.csv', mode = 'w', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,)
        for array in data:
            csv_writer.writerow(array)

def idSortedRegions():
    cleanRegionNames = []
    for each in regionNames:
        if each[0] == ' ':
            cleanRegionNames.append(each[1:])
        else:
            cleanRegionNames.append(each)

    with open('Regions.csv',mode = 'w', newline = '') as file:
        csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, )
        csv_writer.writerow(sorted(cleanRegionNames))



def writeSingle(target):
    with open(target,'r') as input:
        data = json.loads(input.read())
        with open('output.csv',mode = 'w',newline = '') as file:
            csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, )
            csv_writer.writerow(data.values())

compile()
