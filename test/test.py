#!/usr/bin/env python
# encoding: utf-8

import sys

sys.path.insert(0, '.')
sys.path.insert(0, '../')

from barber import barber

str = "e36bc283b3ae643d85ba28ae12d09f61b48dd3e9f7f816ad692d60de96d0df59dbc3ace23348ab1a6a1dcd0e9840b733"

print(barber.cut(str))