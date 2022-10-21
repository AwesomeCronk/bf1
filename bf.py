import argparse, sys, time

parser = argparse.ArgumentParser('BrainFuck')
parser.add_argument(
    'source',
    help='Where to source bf code from'
)
parser.add_argument(
    '-f',
    '--file',
    help='Treat input as file path',
    action='store_true'
)
parser.add_argument(
    '-d',
    '--data-length',
    help='How much data to give the bf interpreter',
    type=int,
    default=30000
)

if __name__ == '__main__':
    args = parser.parse_args(sys.argv[1:])
    if args.file:
        with open(args.source, 'rb') as sourceFile:
            program = sourceFile.read()
    else:
        program = args.source.encode()

    counter = 0
    pointer = 0
    depth = 0
    data = [0] * args.data_length
    print('Data initialized to length {}'.format(args.data_length))

    while True:
        try: char = program[counter]
        except: print('End of program'); exit()
        try: charStr = int.to_bytes(char, 1, 'big').decode()
        except: charStr = ''
        print(counter, char, charStr)

        if char == 43:      # +
            data[pointer] = (data[pointer] + 1) % 256
            counter += 1

        elif char == 45:    # -
            data[pointer] = (data[pointer] - 1) % 256
            counter += 1

        elif char == 44:    # ,
            badInput = True
            while badInput:
                try: data[pointer] = int('0x' + input('Enter input: '), base=16) % 256; badInput = False
                except: pass
                counter += 1

        elif char == 46:    # .
            print('Output: {:02X}'.format(data[pointer]))
            counter += 1

        elif char == 60:    # <
            pointer = (pointer - 1) % args.data_length
            counter += 1

        elif char == 62:    # >
            pointer = (pointer + 1) % args.data_length
            counter += 1

        elif char == 91:    # [
            depth += 1
            if data[pointer] == 0:
                targetDepth = depth - 1
                print(targetDepth)
                while depth != targetDepth or program[counter] != 93:
                    counter += 1
                    print('[', counter, depth)
                    if program[counter] == 91: depth += 1
                    elif program[counter] == 93: depth -= 1
            else:
                counter += 1

        elif char == 93:    # ]
            depth -= 1
            if data[pointer] != 0:
                targetDepth = depth
                print(targetDepth)
                while depth != targetDepth or program[counter] != 91:
                    counter -= 1
                    print(']', counter, depth)
                    if program[counter] == 91: depth += 1
                    elif program[counter] == 93: depth -= 1
            else:
                counter += 1
        
        else:
            counter += 1
        time.sleep(0.2)
