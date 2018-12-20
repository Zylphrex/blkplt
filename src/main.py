import argparse
import sys

from blk_entry import BlkEntry
from analysis.frequency import to_csv


def main():
    to_csv('/Users/tonyx/Documents/repos/blkplt/filtered.trace', 'W').write('asdf.csv')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--action', default='A',
            help='The desired action type. Can be W for write, R for read, or A or all.')
    parser.add_argument('-i', '--infile',
            help='The blkparse file to process. Uses stdin if not specified.')
    parser.add_argument('-o', '--outfile',
            help='The output file to write to. Uses stdout if not specified.')
    args = parser.parse_args()

    if args.action not in ('W', 'R', 'A'):
        raise ValueError('Invalid action type: {}'.format(args.action))
    action = args.action

    if args.infile:
        infile = open(args.infile)
    else:
        infile = sys.stdin

    if args.outfile:
        outfile = open(args.outfile, 'w')
    else:
        outfile = sys.stdout

    to_csv(infile, action).write(outfile)

