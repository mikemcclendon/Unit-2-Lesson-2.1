import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt
import collections
import matplotlib.pyplot as plt

testlist = [1, 4, 5, 6, 9, 9, 9]
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

ctest = collections.Counter(testlist)
cx = collections.Counter(x)

count_sum_test = sum(ctest.values())
count_sum_x = sum(cx.values())


for k,v in ctest.iteritems():
  print("In testlist the frequency of number " + str(k) + " is " + str(float(v) / count_sum_test))
  
for k,v in cx.iteritems():
  print("In x the frequency of number " + str(k) + " is " + str(float(v) / count_sum_x))
 
fig = plt.figure()
fig.suptitle('testlist Boxplot', fontsize=14, fontweight='bold')
plt.boxplot(testlist)
plt.savefig("testlistbox.png")

fig = plt.figure()
fig.suptitle('X Boxplot', fontsize=14, fontweight='bold')
plt.boxplot(x)
plt.savefig("xbox.png")

fig = plt.figure()
fig.suptitle('testlist Histogram', fontsize=14, fontweight='bold')
plt.hist(testlist, histtype='bar')
plt.savefig("testlisthist.png")

fig = plt.figure()
fig.suptitle('X Histogram', fontsize=14, fontweight='bold')
plt.hist(x, histtype='bar')
plt.savefig("xhist.png")


fig = plt.figure()
fig.suptitle('testlist', fontsize=14, fontweight='bold')
graph1 = stats.probplot(testlist, dist="norm", plot=plt)
plt.savefig("testlistprobplot.png")

fig = plt.figure()
fig.suptitle('X', fontsize=14, fontweight='bold')
graph2 = stats.probplot(x, dist="norm", plot=plt)
plt.savefig("xprobplot.png")


plt.show()
