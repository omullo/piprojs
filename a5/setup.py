#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 22:27:51 2018

@author: frank
"""

import cx_Freeze

executables = [cx_Freeze.Executable("a5_uno.py")]

cx_Freeze.setup(
    name="UNO Champ",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":[]}},
    executables = executables

    )