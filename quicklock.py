import os
import re
import json
import psutil
import logging
import traceback

log = logging.getLogger('quicklock')

def singleton(resource, dirname='.lock'):
    """
    Lock a resource name so that if this function is called again before the lock is
    released, a RuntimeError will be raised.

    Arguments:
    resource -- Name of the resource to lock
    dirname -- Base directory to store lock files, default is `pwd`/.lock
    """
    lock_root = os.path.realpath(dirname)

    if not os.path.exists(lock_root):
        os.mkdir(lock_root)

    lock_name = re.sub(r'[^a-zA-Z0-9]+', '_', resource)

    lock_file = os.path.join(lock_root, lock_name + '.lock')

    # Check if the process that locked the file is still running
    if os.path.exists(lock_file):
        locked = False
        try:
            with open(lock_file, 'r') as lock_handle:
                data = json.load(lock_handle)

            # Check if process is still running
            if psutil.pid_exists(data['pid']):
                other_process = psutil.Process(data['pid'])
                if other_process.is_running() and other_process.name() == data['name']:
                    locked = True

        # Something is wrong with the lockfile, just ignore it and create the lock below
        except Exception, exc:
            pass

        # Resource was locked
        if locked:
            raise RuntimeError('Resource <{}> is currently locked by <Process {}: "{}">'.format(resource, other_process.pid, other_process.name()))

    # Create the lock with the current process information
    process = psutil.Process(os.getpid())
    with open(lock_file, 'w') as lock_handle:
        json.dump({"name": process.name(), "pid": process.pid}, lock_handle)
        log.info('Obtained exclusive lock on resource <{}> (this is <Process {}: "{}">)'.format(resource, process.pid, process.name()))
