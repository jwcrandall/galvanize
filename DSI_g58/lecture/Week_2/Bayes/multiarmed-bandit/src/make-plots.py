#!/usr/bin/env python

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
plt.style.use('bmh')

## make gamma plot
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)
gamma = stats.gamma

parameters = [(1, 0.5), (9, 2), (3, 0.5), (7, 0.5)]
x = np.linspace(0.001 ,20, 150)
for alpha, beta in parameters:
    y = gamma.pdf(x, alpha, scale=1./beta)
    lines = plt.plot(x, y, label = "(%.1f,%.1f)"%(alpha,beta), lw = 3)
    ax.fill_between(x, 0, y, alpha = 0.2, color = lines[0].get_color())
    ax.autoscale(tight=True)
    
ax.legend(title=r"$\alpha, \beta$ - parameters");
plt.savefig("gamma-priors.png",dpi=400)


## make beta plot
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)

params = [(2, 5), (1, 1), (0.5, 0.5), (5, 5), (20, 4), (5, 1)]

x = np.linspace(0.01, .99, 100)
beta = stats.beta
for a, b in params:
    y = beta.pdf(x, a, b)
    lines = plt.plot(x, y, label = "(%.1f,%.1f)"%(a,b), lw = 3)
    ax.fill_between(x, 0, y, alpha = 0.2, color = lines[0].get_color())
    ax.autoscale(tight=True)
ax.set_ylim(0)
ax.legend(loc = 'upper left', title="(a,b)-parameters");
plt.savefig("beta-priors.png",dpi=400)
