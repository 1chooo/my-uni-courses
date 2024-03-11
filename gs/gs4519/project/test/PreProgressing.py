import os
import glob
import pandas as pd


# Get the root from the computer. Then read the file.
pathDomestic = os.path.abspath(os.getcwd()) + "../data"
root = pathDomestic
data = glob.glob(os.path.join(root, "*.csv"))


# Integrate all file in one csv file.
dataFrame = pd.concat((pd.read_csv(file) for file in data))
dataFrame.to_csv("./20years_data.csv", encoding = "utf_8_sig", index = False) 