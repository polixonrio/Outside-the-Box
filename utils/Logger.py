import sys


# taken from https://stackoverflow.com/a/11325249
class Logger(object):
    def __init__(self, *files):
        self.files = files

    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush()

    def flush(self):
        for f in self.files:
            f.flush()

    @property
    def encoding(self):
        # Return the encoding of the first file (usually sys.stdout)
        return getattr(self.files[0], 'encoding', 'utf-8')

    def __getattr__(self, name):
        # Delegate any other attribute access to the first file (usually sys.stdout)
        return getattr(self.files[0], name)

    @staticmethod
    def start(file):
        f = open(file, "w")
        logger = Logger(sys.stdout, f)
        sys.stdout = logger
        return logger

    def stop(self):
        sys.stdout = self.files[0]
        self.files[1].close()
