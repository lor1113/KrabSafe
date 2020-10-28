import json
years = [2019]
months = ['aug']
master = []

def writer(target,tbw):
    with open(target,'w') as outfile:
        json.dump(tbw,outfile)


for year in years:
    for month in months:
        json_data = open(str(year)+month+'_noPVP.json').read()
        data = json.loads(json_data)
        listData = list(data.values())
        master.append(listData)

writer('Master_bounty.json',master)

