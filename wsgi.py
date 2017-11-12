#!/user/bin/env python3

import sys

from os.path import abspath

from os.path import dirname

sys.path.insert(0, abspath(dir(__file__)))

import app


application = app.app