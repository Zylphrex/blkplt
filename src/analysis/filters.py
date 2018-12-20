LEGAL_ACTIONS = {
    'A',  # IO was remapped to a different device
    'B',  # IO bounced
    'C',  # IO completion
    'D',  # IO issued to driver
    'F',  # IO front merged with request on queue
    'G',  # Get request
    'I',  # IO inserted onto request queue
    'M',  # IO back merged with request on queue
    'P',  # Plug request
    'Q',  # IO handled by request queue code
    'S',  # Sleep request
    'T',  # Unplug due to timeout
    'U',  # Unplug request
    'X',  # Split
}

LEGAL_RWBS = {
    'D',  # discard
    'W',  # write
    'R',  # read
    'N',  # None of the above
    'F',  # FUA
    'A',  # readahead
    'S',  # sync
    'M',  # metadata
}


def action_filter(action):
    if action not in LEGAL_ACTIONS:
        raise ValueError('{} is not an valid action'.format(action))

    def filter_fn(entry):
        return entry.action == action

    return filter_fn


def rwbs_filter(rwbs):
    if rwbs not in LEGAL_RWBS:
        raise ValueError('{} is not an valid rwbs'.format(rwbs))

    def filter_fn(entry):
        return rwbs in entry.rwbs

    return filter_fn
