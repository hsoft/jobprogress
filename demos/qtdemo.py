# Created By: Virgil Dupras
# Created On: 2010-11-19
# Copyright 2010 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "BSD" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/bsd_license

# To run this demo, you need PyQt.

import sys
import time

from PyQt4.QtCore import QCoreApplication
from PyQt4.QtGui import QApplication

from jobprogress.qt import Progress

def work(seconds=1):
    time.sleep(seconds)

def perform(j):
    TASKS = [ # (task_proportion, work units)
        (2, 5), # Slower than expected
        (5, 3), # Faster than expected
        (3, 15), # Much slower
    ]
    proportions = [prop for prop, _ in TASKS]
    j = j.start_subjob(proportions)
    for index, (_, work_units) in enumerate(TASKS):
        j.start_job(work_units, 'Starting task #{}'.format(index))
        for _ in range(work_units):
            work()
            j.add_progress()

def main(argv):
    app = QApplication(argv)
    prog = Progress(None)
    j = prog.create_job()
    prog.run('my_jobid', 'Demo Progress dialog in Qt', perform, (j, ))
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
