import matplotlib.pyplot as plt 
import pandas as pd
import os
from linear import fit_linear


os.chdir("pytools/statistics")
data = pd.read_csv("linear_data_example.csv")

# Use fit_linear class
fit_object = fit_linear(data['x'], data['y'], confidence=99.9)

# Quickest way to plot --------------------------\

fit_object.plot()

# Another way to plot and save ------------------\

# Create matplotlib figure
fig, ax = plt.subplots(figsize=(11, 7.5))

# Use plot() method
fit_object.plot(fig_handl=fig, ax_handl=ax, save_as="linear_example_plot_fit.png")

# Show matplotlib figure 
plt.show()
