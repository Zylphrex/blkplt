from collections import Counter
from functools import reduce
from multiprocessing import Pool
from analysis.filters import action_filter, rwbs_filter
from blk_entry import BlkEntry
from util import CSV, report


# A predicate that returns True if the entry is a complete action
complete = action_filter('C')

# A predicate that returns True if the entry is a write rwbs
write = rwbs_filter('W')

# A predicate that returns True if the entry is a read rwbs
read = rwbs_filter('R')


def write_filter_fn(entry):
    """
    A predicate that returns True for complete actions that are writes.
    """
    return complete(entry) and write(entry)


def read_filter_fn(entry):
    """
    A predicate that returns True for complete actions that are reads.
    """
    return complete(entry) and read(entry)


def all_filter_fn(entry):
    """
    A predicate that returns True for complete actions that are writes or reads.
    """
    return write_filter_fn(entry) or read_filter_fn(entry)


# The available filters
filters = {
    'W': write_filter_fn,  # WRITE
    'R': read_filter_fn,   # READ
    'A': all_filter_fn,    # ALL
}


def to_page_range(entry):
    """
    Contructs a range object from a single entry for the pages it accessed.

    Range has increments of 8 because page access in the traces are in multiples of 8.
    """
    parts = entry.payload.split(' ')
    sector = int(parts[0])
    try:
        blocks = int(parts[2])
    except IndexError:
        blocks = 1
    return range(sector, sector + blocks, 8)


def count_page_access(counter, arange):
    for i in arange:
        counter[i] += 1
    return counter


def reduce_counts_fn(counter, entry):
    _, count = entry
    counter[count] += 1
    return counter


def load_data(file_name, filter_fn):
    blk_entries = BlkEntry.from_file(file_name)
    blk_entries = filter(filter_fn, blk_entries)
    ranges  = map(to_page_range, blk_entries)
    return ranges


def to_csv(file_name, filter_type):
    ranges  = load_data(file_name, filters[filter_type])
    counter = reduce(count_page_access, ranges, Counter())
    csv = CSV(['page', 'frequency'])
    csv.rows = counter.items()
    return csv
