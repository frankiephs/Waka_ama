# extract the data
f = open("waka_ama_res/WakaNats2017/001-Heat 1-01.lif", "r")

race = {'header' : f.readline(),
        'body' : f.readline()}
print(race)