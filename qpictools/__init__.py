#!/usr/bin/env python3
# -*- coding: utf-8 -*
"""Toolbox for analysing QuickPIC data

  QuickPIC Tools
 ================
  Analysis Package for QuickPIC Data
  By: Veronica Berglyd Olsen
      University of Oslo, Norway

"""

import logging as logger

__author__     = "Veronica Berglyd Olsen"
__copyright__  = "Copyright 2017, Veronica Berglyd Olsen"
__credits__    = ["Veronica Berglyd Olsen"]
__license__    = "GPLv3"
__version__    = "0.1.0"
__date__       = "2017"
__maintainer__ = "Veronica Berglyd Olsen"
__email__      = "v.k.b.olsen@cern.ch"
__status__     = "Development"

logger.basicConfig(
    format  = "[%(asctime)s] %(levelname)s: %(message)s",
    level   = logger.DEBUG,
    datefmt = "%H:%M:%S",
)

if __name__ == '__main__':
    print("QuickPIC Tools")
