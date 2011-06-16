#!/usr/bin/env python

import sys
from gi.repository import PackageKitGlib as packagekit

def progress_cb(status, typ, data=None):
    if status.get_property('package'):
        print "Pachet ", status.get_property('package'), status.get_property('package-id')
        if status.get_property('package'):
            print status.get_property('package').get_name()
    print typ, status.get_property('package')

def main(args):
    if len(args) < 2:
        print 'Usage: %s [search|] ' % args[0]
        return -1

    client = packagekit.Client()
    if args[1] == 'search':
        if len(args) < 3:
            print "Nothing to search"
            return -1
        result = client.search_names(0, [args[2],], None, progress_cb, None)
        pkgs = result.get_package_array()
        for p in pkgs:
            print p.get_name()
    elif args[1] == 'install':
        client.install_packages(False, [args[2],], None, progress_cb, None)
    elif args[1] == 'remove':
        client.remove_packages([args[2],],
                                False, # allow_deps
                                False, # autoremove
                                None,  # cancelable
                                progress_cb,
                                None
        )
    else:
        print "Unknown command: ", args[1]
if __name__ == "__main__":
    sys.exit(main(sys.argv))
