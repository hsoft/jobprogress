=============================================
:mod:`performer` - Sync GUI with threaded job
=============================================

.. module:: performer

Also, most of the time, we want to run our task in a separate thread so the GUI stays smooth. :class:`ThreadedJobPerformer` takes care of synchronizing the threaded task and the GUI.

.. class:: ThreadedJobPerformer()

This class provides an easy way to asynchronously start a job and track its progress. You would use it like this::

    tp = ThreadedJobPerformer()
    j = tp.create_job()
    tp.async_run(some_big_processing, args=(j, ))
    # Now, have the GUI in the main thread constantly check tp.last_progress and
    # tp.last_desc and update a progress dialog or something.
