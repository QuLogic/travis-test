# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from tempfile import NamedTemporaryFile
import threading
import time
import numpy as np

# Tests for race conditions. Reading n_threads (currently 30) times
# the same waveform file in parallel and compare the results which must
# be all the same.
data = np.arange(0, 500)

# create waveform file with given format and byte order
with NamedTemporaryFile() as tf:
    outfile = tf.name
    data.tofile(outfile)
    n_threads = 30
    streams = []

    def testFunction(streams):
        st = np.fromfile(outfile, dtype=data.dtype)
        streams.append(st)

    # Read the ten files at one and save the output in the just
    # created class.
    for _i in range(n_threads):
        thread = threading.Thread(target=testFunction,
                                  args=(streams,))
        thread.start()

    # Loop until all threads are finished.
    start = time.time()
    while True:
        if threading.activeCount() == 1:
            break
        # Avoid infinite loop and leave after 120 seconds
        # such a long time is needed for debugging with valgrind
        elif time.time() - start >= 120:  # pragma: no cover
            msg = 'Not all threads finished!'
            raise Warning(msg)

    # Compare all values which should be identical and clean up
    # files
    for thedata in streams:
       np.testing.assert_array_equal(data, thedata)

