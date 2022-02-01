import numpy as np
from scipy.stats import norm 
import matplotlib.pyplot as plt 


def fit_normal(    
        np_array_of_data, 
        plot=False, save_as=" ", bins=25):

    """
    
    function
    -----------
    Fits a normal distribution to data 

    parameters
    -----------
    np_array_of_data: 1-D numpy array of data
    plot: whether or not to plot (False by default)
    save_as: name to save plot as (eg. "plotName.png")
    bins: number of bins to use in histogram when plotting the data 

    returns
    -----------
    mu: mean of normal fit
    std: standard deviation of normal fit

    """

    mu, std = norm.fit(np_array_of_data)

    if plot:

        plt.figure(figsize=(11, 8))
        
        plt.hist(np_array_of_data, bins=bins, density=True, alpha=0.3, label="data")
        xmin, xmax = plt.xlim()
        
        xx = np.linspace(xmin, xmax, 100)
        pdf = norm.pdf(xx, mu, std)
        plt.plot(xx, pdf, 'k-', linewidth=2, label="normal fit")

        plt.plot([mu, mu], [0, max(pdf)], 'k--', label="mean ($\mu$)")
        plt.plot([mu-std, mu-std], [0, max(pdf)], 'b--', label="$1\sigma$ (68.3%)")
        plt.plot([mu+std, mu+std], [0, max(pdf)], 'b--')
        plt.plot([mu-2*std, mu-2*std], [0, max(pdf)], 'g--', label="$2\sigma$ (95.4%)")
        plt.plot([mu+2*std, mu+2*std], [0, max(pdf)], 'g--')
        plt.plot([mu-3*std, mu-3*std], [0, max(pdf)], 'r--', label="$3\sigma$ (99.7%)")
        plt.plot([mu+3*std, mu+3*std], [0, max(pdf)], 'r--')

        plt.legend()
        title_str = "$\mu$ = " + f'{mu:.3f}' + ", $\sigma$ = " + f'{std:.3f}'
        plt.title(title_str)
        if save_as != " ":
            plt.savefig(save_as)
        plt.show()
        
    return mu, std
