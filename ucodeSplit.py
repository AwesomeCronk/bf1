import argparse

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'infile',
        type=str
    )
    parser.add_argument(
        'outfilea',
        type=str
    )
    parser.add_argument(
        'outfileb',
        type=str
    )
    return parser.parse_args()

if __name__ == '__main__':
    args = getArgs()
    with open(args.infile, 'rb') as infile:
        inBin = infile.read()

    outLen = len(inBin) // 2
    outBinA = b''
    outBinB = b''

    print('Splitting {} byte-by-byte to get {} and {}, each at length {}'.format(args.infile, args.outfilea, args.outfileb, outLen))

    for i in range(outLen):
        outBinA = outBinA + inBin[i * 2].to_bytes(1, 'big')
        outBinB = outBinB + inBin[(i * 2) + 1].to_bytes(1, 'big')

    with open(args.outfilea, 'wb') as outfileA:
        outfileA.write(outBinA)

    with open(args.outfileb, 'wb') as outfileB:
        outfileB.write(outBinB)
