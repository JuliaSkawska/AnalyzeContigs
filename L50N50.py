def analysefile(inputfile, fullvalue):
    secvalue = 0
    i = 0
    print('{:*^50}'.format('Results:'))
    print(f'Total contig length: {fullvalue}')
    print(f'Amount of contigs: {len(inputfile)}')
    value = fullvalue * 0.5
    for elem in inputfile:
        secvalue += elem
        i += 1
        if secvalue > value:
            print(f'N50: {elem}')
            print(f'L50: {i}')
            print('{:*^50}'.format(''))
            break

def readfile():
    filepath = input("Please include the path to the file you want to analyse: ")
    try:
        with open(filepath, 'r') as file:
            next(file)  # Skip the first line
            res = []
            value = 0
            for lines in file:
                temp = lines.split("\t")
                if 'LN:' in temp[2]:
                    hold = temp[2]
                    res.append(int(hold[3:]))
                    value += (int(hold[3:]))
            res.sort(reverse=True)
            return res, value
    except FileNotFoundError:
        raise FileNotFoundError(f"No file found at the provided path: {filepath}")

analysefile(*readfile())

