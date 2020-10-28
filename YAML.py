import yaml
yeet = []
target = 'invFlags.yaml'
with open (target,'r') as file:
    E = yaml.load(file)
    for each in E:
        yeet.append(each['flagID'])

    print(yeet)