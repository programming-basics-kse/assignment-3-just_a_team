with open('Olympic Athletes - athlete_events.tsv', "rt") as file:
    next(file)
    for line in file:
        line = line[:-1]
        split = line.split('\t')
        print(split)