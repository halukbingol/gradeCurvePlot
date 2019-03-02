# plots curve of overall grades of students
# Haluk O. Bingol 2019
# source:

import statistics as stat
import numpy as np
import matplotlib.pyplot as plt
import math


#
#
def average(lst):
    """
    Find the mean value of a list

    eg
        average([1., 2., 6.])   # => 3.

    If the list is empty, return 0.
    """
    if lst:
        return sum(lst) / len(lst)
    else:
        return 0.


def make_weighted_sum_fn(weights):
    """
    Given a list of weights, return a function which
      calculates a final weighted score
    """
    weights = list(weights)
    len_ = len(weights)

    def weighted_sum_fn(values):
        values = list(values)
        assert len(values) == len_
        return sum(w * v for w, v in zip(weights, values))

    return weighted_sum_fn


def getBin(data):
    dataMin = math.ceil(min(data))
    dataMax = math.floor(max(data))
    number = dataMax - dataMin + 1
    bin = np.linspace(dataMin,
                      dataMax,
                      number)
    return bin


# Generated data set
def GenerateDataset(N, min, max):
    import random as rd

    lst = []
    #
    return [1, 2, 3]
    #
    for i in range(N):
        x = rd.randint(min, max)
        x = rd.rand
        lst.append(x)
    return (lst)

    #
    #


def plotCurve(data):
    f = plt.figure()

    # set the mean and the variance:
    mu = np.mean(data)
    sigma = np.std(data, ddof=1)


    # @HB should not be manual
    # print(np.siz)
    dataCount = 114
    dataMin = math.floor(min(data)) - 1
    dataMax = math.ceil(max(data)) + 1
    binNOF = dataMax - dataMin + 1
    # bins = np.linspace(dataMin,
    #                    dataMax,
    #                    binNOF)
    binSize = 101
    bins = np.linspace(0,
                       100,
                       binSize)
    #
    print('min:', dataMin, 'max:', dataMax, 'binNOF:', binNOF)

    # sigma and mu
    mu = stat.mean(grades)
    sigma = stat.stdev(grades)
    sig2m = math.floor(mu - 2 * sigma)
    sig1m = math.floor(mu - 1 * sigma)
    sig0m = math.floor(mu)
    sig1p = math.floor(mu + 1 * sigma)
    sig2p = math.floor(mu + 2 * sigma)
    sigY = 6
    sigX = -5
    alpha = 0.5
    plt.text(sig2m + sigX, sigY,  '$-2\sigma=$' + "%2.1f" % (mu - 2 * sigma), color='r', alpha=alpha)
    plt.text(sig1m + sigX, sigY,  '$-\sigma=$' + "%2.1f" % (mu - 1 * sigma), color='r', alpha=alpha)
    plt.text(sig0m + sigX, sigY,  '$\mu=$' + "%2.1f" % (mu - 0 * sigma), color='r', alpha=alpha)
    plt.text(sig1p + sigX, sigY,  '$\sigma=$' + "%2.1f" % (mu + 1 * sigma), color='r', alpha=alpha)
    plt.text(sig2p + sigX, sigY,  '$2\sigma=$' + "%2.1f" % (mu + 2 * sigma), color='r', alpha=alpha)
    plt.axvline(x=sig2m, color='r', alpha=alpha)
    plt.axvline(x=sig1m, color='r', alpha=alpha)
    plt.axvline(x=sig0m, color='r', alpha=alpha)
    plt.axvline(x=sig1p, color='r', alpha=alpha)
    plt.axvline(x=sig2p, color='r', alpha=alpha)
    plt.plot(bins, dataCount * 1 / (sigma * np.sqrt(2 * np.pi)) *
             np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)),
             linewidth=2, color='r', alpha=alpha)

    # data
    plt.hist(data, bins=bins, histtype='bar', rwidth=0.8, alpha=0.8)


    # plot
    plt.title('Curve of cmpe220')
    plt.xlabel('overall grades')
    plt.ylabel('number of students')
    # plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.xlim([0, binSize+1])
    plt.show()

    f.savefig("cmpe220-2018-3-curve.pdf", bbox_inches='tight')
    # ---- plotCurve


grades = np.array(
    [91.9922161172161, 91.2628205128205, 89.8754578754579, 88.3342490842491, 86.5549450549451, 85.9757326007326,
     85.6895604395604, 84.3928571428571, 83.6891025641026, 82.5563186813187, 81.0668498168498, 80.9835164835165,
     79.9848901098901, 80.5645604395605, 76.6771978021978, 76.4862637362637, 76.4642857142857, 75.2174908424908,
     74.4555860805861, 74.404304029304, 74.0270146520147, 71.6836080586081, 69.7069597069597, 69.6712454212454,
     69.0260989010989, 68.7055860805861, 68.3003663003663, 68.1547619047619, 67.7193223443223, 67.3429487179487,
     66.9125457875458, 66.7385531135531, 66.6552197802198, 66.3772893772894, 66.3768315018315, 66.3360805860806,
     65.2701465201465, 64.4162087912088, 64.2032967032967, 63.9532967032967, 63.2614468864469, 66.1593406593407,
     63.1034798534799, 62.6217948717949, 62.5682234432234, 62.0549450549451, 61.4606227106227, 61.0064102564103,
     60.9418498168498, 60.2614468864469, 59.6314102564103, 59.0924908424908, 58.9377289377289, 58.6849816849817,
     58.3763736263736, 57.831043956044, 57.5302197802198, 56.342032967033, 55.4812271062271, 54.8269230769231,
     54.3754578754579, 54.3507326007326, 53.6547619047619, 53.6277472527473, 53.5764652014652, 53.46336996337,
     52.5860805860806, 52.3470695970696, 51.7797619047619, 51.4377289377289, 51.3827838827839, 51.1804029304029,
     51.0526556776557, 50.6369047619048, 55.4977106227106, 49.6149267399267, 49.3878205128205, 49.3690476190476,
     49.1172161172161, 48.8108974358974, 48.4583333333333, 48.4207875457875, 47.4629120879121, 47.2335164835165,
     46.6923076923077, 44.742673992674, 44.4207875457875, 43.9935897435897, 43.5430402930403, 43.4326923076923,
     42.5421245421245, 41.8827838827839, 40.5723443223443, 40.4880952380952, 40.0425824175824, 38.1872710622711,
     37.9922161172161, 37.3782051282051, 35.4578754578755, 34.0755494505494, 33.4056776556777, 33.047619047619,
     32.8379120879121, 31.724358974359, 31.4230769230769, 31.2664835164835, 29.6217948717949, 28.2747252747253,
     26.3104395604396, 22.6607142857143, 16.7957875457875, 16.0064102564103, 13.5, 13.4624542124542 ])
bins = np.linspace(1,
                   100,
                   101)

# gradeNumber = GenerateDataset(5, 1, 10)
# bins = np.linspace(dataMin,
#                    dataMax,
#                    binNOF)
# print(grades)

mu = stat.mean(grades)
sigma = stat.stdev(grades)
median_low = stat.median_low(grades)
# mode = stat.mode(gradeNumber)
print('mu:\t\t', mu)
print('sigma:\t\t', sigma)
print('median_low:', median_low)
# print('mode:', mode)


# bins = getBin(gradeNumber)
# print('bins:', bins)

# data = 2 * bins
# print('data:', data)

plotCurve(grades)

# # x = np.linspace(0, 2, 100)
#
# # plt.plot(x, x, label='linear')
# # plt.plot(x, x ** 2, label='quadratic')
# # plt.plot(x, x ** 3, label='cubic')
# plt.hist(x,biny)
#
# plt.xlabel('bins')
# plt.ylabel('frequency')
#
# plt.title('Curve')
#
# plt.legend()
#
# plt.show()


# plotCurve([1])
