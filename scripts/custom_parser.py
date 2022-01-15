import argparse
import sys

class CustomArgsParser(argparse.ArgumentParser):

    def error(self, message):
        self.usage = argparse.SUPPRESS
        self.print_usage(sys.stderr)
        self.exit(2, ('error: %s\n') % (message))