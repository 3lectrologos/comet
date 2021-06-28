import output
import pickle
import numpy as np


with open('delta.pcl', 'rb') as fin:
    delta = pickle.load(fin)

    deltas, realDist, exp, std = delta
    print('deltas =', deltas)
    print('realDist =', realDist)
    logY = np.log10(np.array(realDist))
    logX = np.log10(np.array(deltas))
    print(logX)
    print(logY)
    print('exp =', exp)
    print('std =', std)
    import matplotlib.pylab as plt
    plt.plot(logX, logY, 'bo')
    #plt.show()

    output.choose_delta(*delta)
