import os
import glob
import pandas as pd

pathDomestic = os.path.abspath(os.getcwd()) + "/data"
root = "./data"
data = glob.glob(os.path.join(root, "*.csv"))


predictData = pd.concat((pd.read_csv(f) for f in data))

predictData.to_csv("./predictData.csv", encoding = "utf_8_sig", index = False)