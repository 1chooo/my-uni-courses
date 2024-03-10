# -*- coding: utf-8 -*-

from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import numpy as np


with open('./linu850.txt', 'r') as f:
    text = f.read()
    print(text)