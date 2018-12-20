import csv


def report(label, n):
    def decorator(fn):
        x = { 'i': 0 }
        def wrapper(*args, **kwargs):
            if x['i'] % n == 0:
                print('{} {}'.format(label, x['i']))
            x['i'] += 1
            return fn(*args, **kwargs)
        return wrapper
    return decorator


class CSV(object):
    def __init__(self, headers):
        self.headers = headers
        self.rows = []

    def write(self, f):
        with f:
            writer = csv.DictWriter(f, self.headers)
            writer.writeheader()
            for row in self.rows:
                writer.writerow(dict(zip(self.headers, row)))

