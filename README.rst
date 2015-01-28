quicklock
=========

A simple Python resource lock to ensure only one process at a time is
operating with a particular resource.

Singleton Usage
---------------

Singleton creates a file containing process information to ensure that
the process that created the lock is still alive. The default location
is in the ``.lock`` directory in the current working directory. If this
directory does not exist, ``singleton`` will create it automatically.

Simple usage:
^^^^^^^^^^^^^

.. code:: python

    from quicklock import singleton

    singleton('my-process') # This will ensure that only one of these is running at once
                            # The lock is released when the process that created the lock
                            # exits (successfully or quits unexpectedly)

    # Intensive processing here

Specifying the lock directory:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    from quicklock import singleton

    singleton('my-process', dirname='/var/lock') # Now all lock files will be written to
                                                 # /var/lock instead

    # Intensive processing here

Contributing
------------

Please feel free to create issues and submit pull requests. I want to
keep this library as a simple collection of useful locking-related
utilities.

License
-------

The license is MIT, see the attached ``LICENSE`` file for more
information.
