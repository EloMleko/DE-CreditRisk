import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import data.creds as creds

z = creds.path

with open(z + '\CreditRisk\data\german_data_numeric.csv', 'r+') as file:
    x = file.read()
