import matplotlib.pyplot as plt 
import pandas as pd
import os
from linear import fit_linear


os.chdir("pytools/statistics")
data = pd.read_csv("linear_data_example.csv")

fit_object = fit_linear(data['x'], data['y'], confidence=99.9)

fig, ax = plt.subplots(figsize=(11, 7.5))

fit_object.plot(fig_handl=fig, ax_handl=ax, save_as="linear_example_plot_fit.png")

plt.show()
