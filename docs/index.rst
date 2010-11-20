jobprogress -- Cross-toolkit UI progress tracking
=================================================

When doing complex processing that has to report progress indication to the user, things can get complex quick. Often, we don't know beforehand how many work unit our processing will have, because knowing it depends on another work unit for which the progress should also be reported to the user. One example of such situation is processing files after having collected them. When we start the process, we don't know how many files we'll collect, so it's hard to set a maximum value on our progress bar. ``jobprogress`` handles that.

Also, most of the time, we want to run our task in a separate thread so the GUI stays smooth. ``jobprogress`` takes care of synchronizing the threaded task and the GUI.

Contents:

.. toctree::
   :maxdepth: 2
   
   job
   performer
   qt