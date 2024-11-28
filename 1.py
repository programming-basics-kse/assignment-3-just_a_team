import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Analyze Olympic Games data.')
    parser.add_argument('file', help='Path to the input data file.')
    parser.add_argument('-medals', help='Country code or full name.')
    parser.add_argument('year', type=int, help='Olympic year.')
    parser.add_argument('-total', type=int, help='Year to calculate total medals for.')
    parser.add_argument('-output', help='Path to the output file.')
    return parser.parse_args()

args = parse_arguments()

if args.total and args.medals:
    print('You cannot use both -medals and -total at the same time.')

medals = []
total_medals = {}

with open('Olympic Athletes - athlete_events.tsv', 'rt') as file:
    next(file)
    for line in file:
        line = line[:-1]
        split = line.split('\t')
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

        if args.medals and NOC == args.medals and int(year) == args.year and medal != 'NA':
            medals.append({'Name': name, 'Sport': sport, 'Medal': medal})

        if args.total and int(year) == args.total and medal != 'NA':
            if NOC not in total_medals:
                total_medals[NOC] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
            total_medals[NOC][medal] += 1

lines = []

if args.medals:
    if medals:
        lines.append(f'Medalists for {args.medals} in {args.year}:')
        for medal in medals[:10]:
            lines.append(f'{medal["Name"]} - {medal["Sport"]} - {medal["Medal"]}')
    else:
        lines.append(f'No medalists found for {args.medals} in {args.year}.')

elif args.total:
    lines.append(f'Medal count for the {args.total} Olympics:')
    for noc, counts in total_medals.items():
        lines.append(f'{noc} - Gold: {counts["Gold"]} - Silver: {counts["Silver"]} - Bronze: {counts["Bronze"]}')

print('\n'.join(lines))

if args.output:
    with open(args.output, 'w') as outfile:
        outfile.write('\n'.join(lines))
        print(f'You saved the data in {args.output}')
