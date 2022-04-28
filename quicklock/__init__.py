import os
import re
import json
import psutil
import logging
from pathlib import Path

log = logging.getLogger("quicklock")


def test_lock(resource_name: str, lock_file: os.PathLike):
    """
    Check if the process that locked the file is still running
    """
    if lock_file.exists():
        locked = False
        try:
            with open(lock_file, "r") as lock_handle:
                data = json.load(lock_handle)

            # Check if process is still running
            if psutil.pid_exists(data["pid"]):
                other_process = psutil.Process(data["pid"])
                if other_process.is_running() and other_process.name() == data["name"]:
                    locked = True

        # Something is wrong with the lockfile, just ignore it and create the lock below
        except Exception:
            pass

        # Resource was locked
        if locked:
            raise RuntimeError(
                'Resource <{}> is currently locked by <Process {}: "{}">'.format(
                    resource_name, other_process.pid, other_process.name()
                )
            )


def obtain_lock(resource_name: str, lock_file: os.PathLike):
    """
    Create the lock with the current process information
    """
    process = psutil.Process(os.getpid())
    with open(lock_file, "w") as lock_handle:
        json.dump({"name": process.name(), "pid": process.pid}, lock_handle)
        log.info(
            'Obtained exclusive lock on resource <{}> (this is <Process {}: "{}">)'.format(
                resource_name, process.pid, process.name()
            )
        )


def singleton(resource_name: str, dirname=".lock"):
    """
    Lock a resource name so that if this function is called again before the lock is
    released, a RuntimeError will be raised.

    Arguments:
    resource -- Name of the resource to lock
    dirname -- Base directory to store lock files, default is `pwd`/.lock
    """
    lock_root = Path(dirname)

    if not lock_root.exists():
        lock_root.mkdir()

    lock_name = re.sub(r"[^a-zA-Z0-9]+", "_", resource_name)
    lock_file = (lock_root / lock_name).with_suffix(".lock")

    test_lock(resource_name, lock_file)
    obtain_lock(resource_name, lock_file)


__all__ = ["singleton"]
