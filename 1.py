import argparse
with open('Olympic Athletes - athlete_events.tsv', "rt") as file:
    next(file)
    for line in file:
        line = line[:-1]
        split = line.split('\t')
        print(split)
        ID = split[0]
        name = split[1]
        sex = split[2]
        age = split[3]
        height = split[4]
        weight = split[5]
        team = split[6]
        NOC = split[7]
        games = split[8]
        year = split[9]
        season = split[10]
        city = split[11]
        sport = split[12]
        event = split[13]
        medal = split[14]

parser = argparse.ArgumentParser(description='Olympic athlets for last 120 years.')
parser.add_argument('')