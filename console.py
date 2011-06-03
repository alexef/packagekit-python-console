#!/usr/bin/env python

import sys
from gi.repository import PackageKitGlib as packagekit

def progress_cb(status, type, data=None):
    pass

def main(args):
    if len(args) < 2:
        print 'Usage: %s [search|] ' % args[0]
        return -1

    client = packagekit.Client()
    if args[1] == 'search':
        if len(args) < 3:
            print "Nothing to search"
            return -1
        result = client.search_names(0, args[2], None, progress_cb, None)
        pkgs = result.get_details_array()
        print pkgs
    else:
        print "Unknown command: ", args[1]
if __name__ == "__main__":
    sys.exit(main(sys.argv))
