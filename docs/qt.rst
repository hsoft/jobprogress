=============================================
:mod:`qt` - Show job progress in Qt
=============================================

.. module:: qt

This module contains :class:`Progress`, which is a subclass of ``QProgressDialog`` and :class:`performer.ThreadedJobPerformer`. With it, you can easily run a :class:`Job`-driven task for which the progress is shown to the user (under the Qt toolkit). To use it, just create a :class:`Job` instance and call ``run``, like this::

    prog = Progress(None)
    j = prog.create_job()
    prog.run('my_jobid', 'Title of the progress dialog', async_task, args=(j, ))

This will start ``async_task`` threaded, giving it the job ``j`` as an argument. When the task is complete, it will emit the signal ``finished(str)`` with the argument being the job id you gave it (so you can easily identify which of your job has been completed.

See ``demos/qtdemos.py`` for an example usage.