from sys import stderr


class BlkEntry(object):
    FORMATTER = '{major:3d},{minor:<3d} {cpu:2d} {seq:8d} {time:14.9f} {pid:5d} {action:>2} {rwbs:>3} {payload}'

    def __init__(self, major, minor, cpu, seq, time, pid, action, rwbs, payload):
        self.major = major
        self.minor = minor
        self.cpu = cpu
        self.seq = seq
        self.time = time
        self.pid = pid
        self.action = action.strip()
        self.rwbs = rwbs.strip()
        self.payload = payload.strip()

    def __repr__(self):
        """
        prints the entry in the the same representation as the default blkparse output.
        """
        return BlkEntry.FORMATTER.format(**self.__dict__)

    @staticmethod
    def parse(line):
        major = int(line[0:3])
        minor = int(line[4:7])
        cpu = int(line[8:10])
        seq = int(line[11:19])
        time = float(line[20:35])
        pid = int(line[36:41])
        action = line[42:44]
        rwbs = line[45:48]
        payload = line[49:]
        return BlkEntry(major,
                        minor,
                        cpu,
                        seq,
                        time,
                        pid,
                        action,
                        rwbs,
                        payload)


    @staticmethod
    def from_file(f):
        with f:
            for line in f:
                try:
                    yield BlkEntry.parse(line)
                except ValueError:
                    print('Parse Error (Unexpected Format):\n\t{}'.format(line), file=stderr)
