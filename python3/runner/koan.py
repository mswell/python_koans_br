#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import re


# Starting a classname or attribute with an underscore normally implies Private scope.
# However, we are making an exception for __ and ___.

__all__ = ["__", "___", "____", "_____", "Koan"]

__ = "-=> ME PREENCHA! <=-"


class ___(Exception):
    pass

____ = "-=> TRUE OU FALSE? <=-"

_____ = 0


class Koan(unittest.TestCase):
    pass
