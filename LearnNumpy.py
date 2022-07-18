import numpy as np
import matplotlib.pyplot as plt
plt.rc_context({
'axes.edgecolor':'black', 'xtick.color':'black',
'ytick.color':'black', 'figure.facecolor':'white'});
plt.plot([2, 2.001],[1, 1.001], c='white')
plt.plot([8.999, 9],[3.999, 4], c='white')
vi = 5
vj = 0
plt.arrow(3, 2, vi, vj, head_width = 0.2, width = 0.05, ec ='green')
plt.show();
