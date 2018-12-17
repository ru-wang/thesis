#!/usr/bin/python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

x = np.arange(0.1, 4.0, 0.1)
s = x**2
raw = s
huber = (s <= 1.0) * s + (s > 1.0) * (2.0*pl.sqrt(s)-1.0)
cauchy = pl.log(1.0+s)

fig, ax = plt.subplots()
ax.set_xticks(np.arange(0.0, 5.0, 1.0))
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_xlabel('x')
ax.set_ylabel('x*x')
ax.plot(x, raw, label='Origin')
ax.plot(x, huber, label='Huber')
ax.plot(x, cauchy, label='Cauchy')

plt.legend()

plt.savefig('robust.png')
plt.show()
