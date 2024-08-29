import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def plot_distribution(dist, params, name):
    x = np.linspace(dist.ppf(0.01, *params), dist.ppf(0.99, *params), 100)
    y = dist.pdf(x, *params)
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'r-', lw=2, alpha=0.6, label=name)
    plt.title(f'{name} Distribution')
    plt.xlabel('Value')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'/app/output/{name.lower().replace(" ", "_")}.png')
    plt.close()

# Normal distribution
plot_distribution(stats.norm, (), 'Normal')

# Student's t-distribution
plot_distribution(stats.t, (10,), 'Student t')

# Chi-squared distribution
plot_distribution(stats.chi2, (5,), 'Chi-squared')

# F-distribution
plot_distribution(stats.f, (5, 30), 'F')

# Exponential distribution
plot_distribution(stats.expon, (), 'Exponential')

print("Plots have been generated and saved in the output directory.")
