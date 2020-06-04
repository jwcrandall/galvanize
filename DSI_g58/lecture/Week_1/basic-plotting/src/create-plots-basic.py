#!/usr/bin/env python


import matplotlib.pyplot as plt
import numpy as np

#plt.plot([1,2,3,4])
#plt.ylabel('some numbers')
#plt.savefig('simple.png')


## simple example
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_ylabel('some numbers')
ax.plot([1,2,3,4])
plt.savefig('simple.png')


## simple lines




#######################################################################
## lines with markers
fig = plt.figure()


## the data
t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*np.pi*t)

## the top axes
ax1 = fig.add_subplot(3,1,1)
ax1.set_ylabel('volts')
ax1.set_title('a sine wave')

line1 = ax1.plot(t, s+5.0, color='blue', lw=2)
line2 = ax1.plot(t, s+2.5, color='red', lw=2)
line3 = ax1.plot(t, s, color='orange', lw=2)

## the middle axes
ax2 = fig.add_subplot(3,1,2)
ax2.set_ylabel('volts')
ax2.set_title('a sine wave')

line1 = ax2.plot(t, s+5.0, color='black', lw=2,linestyle="--")
line2 = ax2.plot(t, s+2.5, color='black', lw=2,linestyle="-.")
line3 = ax2.plot(t, s, color='#000000', lw=2,linestyle=":")

## the thrid axes
ax3 = fig.add_subplot(3,1,3)
ax3.set_ylabel('volts')
ax3.set_title('a sine wave')

line1 = ax3.plot(t,s+5.0, color='blue', marker="+")
line2 = ax3.plot(t,s+2.5, color='red', marker="o")
line3 = ax3.plot(t,s, color='orange', marker="^")

## adjust the space between plots
plt.subplots_adjust(wspace=0.2,hspace=.4)







## off subplots axis example
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.set_ylabel('volts')
ax1.set_title('a sine wave')

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*np.pi*t)
line, = ax1.plot(t, s, color='blue', lw=2)

ax2 = fig.add_axes([0.25, 0.1, 0.5, 0.3])
n, bins, patches = ax2.hist(np.random.randn(1000), 50,fc='yellow', edgecolor='blue')
ax2.set_xlabel('time (s)')
plt.savefig("off-subplots.png")
