import matplotlib.pyplot as plt
import csv
import os
from numpy import cumsum

views = []
clones = []
t = []
sum_views = []
sum_clones = []

dir = "report"
for file in sorted(os.listdir(dir)):
    if file.endswith(".csv"):
        with open(os.path.join(dir, file), 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            row1 = next(plots)
            row2 = next(plots)
            row3 = next(plots)
            row4 = next(plots)
            row5 = next(plots)
            views.append(int(row3[-1]))
            clones.append(int(row5[-1]))
            t.append(os.path.splitext(file)[0])
fig, ax = plt.subplots(4, sharex=True)
ax[0].plot(t, views, label='Views', color='b')
ax[0].set_title('Views')
ax[0].legend()

ax[1].plot(t, clones, label='Clones', color='#ffa500')
ax[1].set_title('Clones')
ax[1].legend()

ax[2].plot(t, cumsum(views), label='Cumulative Views', color='b')
ax[2].set_title('Cumulative Views')
ax[2].legend()

ax[3].set_title('Cumulative Clones')
ax[3].plot(t, cumsum(clones), label='Cumulative Clones', color='#ffa500')
ax[3].legend()

plt.legend()
plt.show()

