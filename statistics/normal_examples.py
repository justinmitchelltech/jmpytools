from random import seed
from normal import * 
from scipy.stats import norm 
import os 


os.chdir("pytools/statistics")

data = norm.rvs(20, 5, size=500)  # Generate normally distributed random data
fit_normal(data, plot=True, save_as="normal_examples_plot_fit.png")  # Fit that data
