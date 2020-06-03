import plotille as pt
import numpy as np

X = np.sort(np.random.normal(size=1000))

fig = pt.Figure()
fig.width = 60
fig.height = 30
fig.set_x_limits(min_=-3, max_=3)
fig.set_y_limits(min_=-1, max_=1)
fig.color_mode = 'byte'
fig.plot(X, np.sin(X), lc=200, label='square')

print(fig.show(legend=True))
