import numpy as np
import matplotlib.pyplot as plt 
from scipy import stats


class fit_linear:

    """

    parameters to initialize with
    -----------------------------------
    x: independent variable data
    y: dependent variable data
    confidence: desired percentage statistical confidence interval (default is 95%)
    
    attributes
    -----------------------------------
    x: independent variable data
    y: dependent variable data
    confidence: desired percentage statistical confidence interval (default is 95%)
    slope: slope
    intercept: intercept
    slope_error: +/- error of slope 
    intercept_error: +/- error of intercept 
    reg: regression object returned by scipy.stats.linregress()

    methods
    -----------------------------------
    plot(): Plots data and regression with confidence intervals
    -------
    plot: set to True to generate plot (default is False)
    fig_handl: figure handle - if figure already exists
    ax_handl: axes handle - if axes already exist
    save_as: name to save plot as (e.g. "plotName.png")

    additional info / resources
    -----------------------------------
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html

    """

    def __init__(self, 
            x, y, 
            confidence=95):

        self.x = x
        self.y = y
        self.confidence = confidence

        self.reg = stats.linregress(x, y)

        self.slope = self.reg.slope
        self.intercept = self.reg.intercept
        
        tinv = lambda p, df: abs(stats.t.ppf(p/2, df))  # Function to get t-score
        ts = tinv((1-(confidence/100)), len(x)-2)  # Use ^ to get t-score

        self.slope_error = ts*self.reg.stderr
        self.intercept_error = ts*self.reg.intercept_stderr

        
    def plot(self, 
            fig_handl=None, ax_handl=None, save_as=None):

        line_label = f'y = {self.reg.slope:.3f}x + {self.reg.intercept:.3f}'
        r_squared_label = f"$R^2$: {self.reg.rvalue**2:.2f}"
        slope_stats = f"slope ({self.confidence:.1f}%): {self.reg.slope:.3f} $\pm$ {self.slope_error:.4f}"
        intercept_stats = f"intercept ({self.confidence:.1f}%): {self.reg.intercept:.3f} $\pm$ {self.intercept_error:.4f}"  
        stats_label = line_label + "\n" + r_squared_label + "\n" + slope_stats + "\n" + intercept_stats

        xx = np.linspace(min(self.x), max(self.x), 100)
        yy = self.reg.intercept + self.reg.slope*xx
        yy_upper = yy + self.intercept_error
        yy_lower = yy - self.intercept_error

        if ax_handl == None:
            fig, ax = plt.subplots()
            fig_handl = fig
            ax_handl = ax

        ax_handl.scatter(self.x, self.y, marker='o', facecolor='g', edgecolor='b', alpha=0.5, label="data")
        ax_handl.plot(xx, yy, 'k-', linewidth=1, label="\nlinear fit: "+stats_label)
        ax_handl.plot(xx, yy_upper, 'r--', linewidth=1, label=f'{self.confidence:.1f}% confidence interval')
        ax_handl.plot(xx, yy_lower, 'r--', linewidth=1)
        ax_handl.set_xlabel('x')
        ax_handl.set_ylabel('y')
        ax_handl.legend()

        if save_as != None:
            try: 
                fig_handl.savefig(save_as)
            except AttributeError:
                print("ERROR saving plot. Please pass in fig_handl parameter.")

        if ax_handl == None:
            plt.show()

