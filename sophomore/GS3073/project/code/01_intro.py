# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/12
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

# Printing a message and performing a simple addition
print("Writing code")
print(1 + 2)

# Initializing two rows for a matrix demonstration
row_1 = [1, 2, 1]
row_2 = [1, 1, 0]

# Creating a matrix using the rows
matrix_demo = [row_1, row_2]
print(matrix_demo)

# Subtracting elements of row_2 from row_1
for i in range(len(row_1)):
    row_1[i] = row_1[i] - row_2[i]

print(row_1)

# Performing matrix subtraction using NumPy arrays
import numpy as np

row_1_np = np.array([1, 2, 1])
row_2_np = np.array([1, 1, 0])

result_np = row_1_np - row_2_np
print(result_np)

# Creating a Flask web application
from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when the app is run

# Defining routes for the web application
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/cxcxc")
def hello_123():
    return "Enjoy your youth, everyone!"

# Running the Flask app if the script is executed directly
if __name__ == '__main__':
    app.run()
