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
            views.append(sum([int(i) for i in row2[1:]]))
            clones.append(sum([int(i) for i in row4[1:]]))
            t.append(os.path.splitext(file)[0])

fig, ax = plt.subplots(2, sharex=True)
ax[0].plot(t, views, label='Views')
ax[0].set(xlabel='number of', ylabel='week')
ax[0].set_title('Views and Clones')
ax[0].plot(t, clones, label='Clones')
ax[0].legend()

ax[1].set(xlabel='number of', ylabel='week')
ax[1].plot(t, cumsum(views), label='Cumulative Views')
ax[1].set_title('Cumulative Views and Clones')
ax[1].plot(t, cumsum(clones), label='Cumulative Clones')


plt.legend()
plt.show()

