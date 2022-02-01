from random import seed
from normal import * 
import numpy as np 
import os 


os.chdir("pytools/statistics")

np.random.seed(555)  # Ensures repeatable arrival at the same random data
data = np.random.normal(20, 5, size=500)  # Generate normally distributed random data
fit_normal(data, plot=True, save_as="normal_examples_plot_fit.png")  # Fit that data
