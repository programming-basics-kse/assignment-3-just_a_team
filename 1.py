import argparse
import pycountry

def parse_arguments():
    parser = argparse.ArgumentParser(description='Analyze Olympic Games data.')
    parser.add_argument('file', help='Path to the input data file.')
    parser.add_argument('-medals', help='Country code or full name.')
    parser.add_argument('-year', type=int, help='Olympic year.')
    parser.add_argument('-total', type=int, help='Year to calculate total medals for.')
    parser.add_argument('-overall', nargs='+', help='Displays for each of the entered countries the year in which it won the most medals and their number.')
    parser.add_argument('-output', help='Path to the output file.')
    return parser.parse_args()

args = parse_arguments()

specifiedArgs = [args.total, args.medals, args.overall]
existArgs = 0
for a in specifiedArgs:
    if a is not None:
        existArgs += 1

if existArgs > 1:
    if existArgs > 1:
        print('You can use only one command (-total, -overall, -medals) at the same time.')
    exit()

medals = []
total_medals = {}
overall_medals = {}

with open(args.file, 'rt') as file:
    next(file)
    for line in file:
        line = line[:-1]
        line = line.strip()
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
        countryName = pycountry.countries.get(name=team)
        countryNameAlpha3 = countryName.alpha_3 if countryName else None

        if (team == args.medals or countryNameAlpha3 == args.medals) and int(year) == args.year and medal != 'NA':
            medals.append({'Name': name, 'Sport': sport, 'Medal': medal})

        if args.total and int(year) == args.total and medal != 'NA':
            if team not in total_medals:
                total_medals[team] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
            total_medals[team][medal] += 1

        if args.overall and medal != 'NA':
            if team not in overall_medals:
                overall_medals[team]= { }

            if year not in overall_medals[team]:
                overall_medals[team][year] = {'Medals': 1}
            else:
                overall_medals[team][year]['Medals'] += 1

lines = []

if args.medals:
    if not args.year:
        print("Year is required parameter!")
    elif medals:
        lines.append(f'Medalists for {args.medals} in {args.year}:')
        for medal in medals[:10]:
            lines.append(f'{medal["Name"]} - {medal["Sport"]} - {medal["Medal"]}')
    else:
        lines.append(f'No medalists found for {args.medals} in {args.year}.')

elif args.total:
    lines.append(f'Medal count for the {args.total} Olympics:')
    for noc, counts in total_medals.items():
        lines.append(f'{noc} - Gold: {counts["Gold"]} - Silver: {counts["Silver"]} - Bronze: {counts["Bronze"]}')
elif args.overall:
    lines.append(f'The largest number of medals for the {args.overall} Olympics: ')

    for c in args.overall:
        searchId = c

        if searchId not in overall_medals:
            countryName = pycountry.countries.get(name=searchId)

            if countryName:
                searchId = countryName.alpha_3
                if searchId not in overall_medals:
                    lines.append(f"Country {searchId} not found.")
                    continue
            else:
                lines.append(f"Country {searchId} not found.")
                continue

        maxMedals = 0
        year = 0

        for y in overall_medals[searchId]:
            if int(overall_medals[searchId][y]['Medals']) > maxMedals:
                maxMedals = int(overall_medals[searchId][y]['Medals'])
                year = y

        lines.append(f'{searchId} - {year} - {maxMedals}')

print('\n'.join(lines))

if args.output:
    with open(args.output, 'w') as outfile:
        outfile.write('\n'.join(lines))
        print(f'You saved the data in {args.output}')
                year = y

        lines.append(f'{searchId} - {year} - {maxMedals}')

print('\n'.join(lines))
