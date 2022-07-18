import numpy as np
import matplotlib.pyplot as plt
finite_span = 5
v1 = np.array([2, 2]); v2 = np.array([1, 1])
for c1 in range(-finite_span, finite_span + 1, 1):
 for c2 in range(-finite_span, finite_span + 1, 1):
  v3 = c1*v1 + c2*v2
plt.plot([0, 0.001],[0, 0.001], c='white')
plt.arrow(0, 0, v3[0], v3[1], head_width = 0.5,
width = 0.05, ec ='green')
plt.xlim([-20, 20]); plt.ylim([-20, 20])
plt.show();

import numpy as np
import matplotlib.pyplot as plt
v1 = np.array([2, 2]); v2 = np.array([1, 2])
finite_span = 10
for c1 in range(-finite_span, finite_span+1, 1):
 for c2 in range(-finite_span, finite_span+1, 1):
  v3 = c1*v1 + c2*v2
plt.plot([0, 0.001],[0, 0.001], c='white')
plt.arrow(0, 0, v3[0], v3[1], head_width = 0.5,
width = 0.05, ec ='green')
plt.xlim([-20, 20]); plt.ylim([-20, 20])
plt.show();
