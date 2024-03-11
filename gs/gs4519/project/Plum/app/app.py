# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/26
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.6
'''

from Plum.Model.Train import train
from Plum.gui.Launch import build_ui

def start_gradio():
    confusion, accuracy, recall, precision, proba = train()
    build_ui(confusion, accuracy, recall, precision, proba)
