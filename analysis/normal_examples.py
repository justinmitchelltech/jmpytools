from random import seed
from normal import * 
import numpy as np 
import os 


os.chdir("jmpytools/analysis")

np.random.seed(0)  # Ensures repeatable arrival at the same random data
data = np.random.normal(20, 5, size=500)  # Generate normally distributed random data
fit_normal(data, plot=True, save_as="normal_example-plot.png")  # Fit that data
