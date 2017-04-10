import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import time

date,bid,ask = np.loadtxt('GBPUSD1d.txt', unpack=True,
                        delimiter=',',
                        converters={0:mdates.strpdate2num('%Y%m%d%H%M%S')})

patternAR = []
performanceAR = []

def percentChange(startPoint, currentPoint):
    return ((float(currentPoint)-startPoint)/abs(startPoint))*100.00

def patternStorage():
    patStartTime = time.time()
    avgLine = ((bid+ask)/2)
    x = len(avgLine) - 30

    y = 11
    while y < x:
        pattern = []
        p01 = percentChange(avgLine[y-10], avgLine[y-9])
        p02 = percentChange(avgLine[y-10], avgLine[y-8])
        p03 = percentChange(avgLine[y-10], avgLine[y-7])
        p04 = percentChange(avgLine[y-10], avgLine[y-6])
        p05 = percentChange(avgLine[y-10], avgLine[y-5])
        p06 = percentChange(avgLine[y-10], avgLine[y-4])
        p07 = percentChange(avgLine[y-10], avgLine[y-3])
        p08 = percentChange(avgLine[y-10], avgLine[y-2])
        p09 = percentChange(avgLine[y-10], avgLine[y-1])
        p10 = percentChange(avgLine[y-10], avgLine[y])

        outcomeRange = avgLine[y+20:y+30]
        currentPoint = avgLine[y]

        try:
            avgOutcome = reduce(lambda x, y: x+y, outcomeRange) / len(outcomeRange)
        except Exception, e:
            print str(e)
            avgOutcome = 0

        futureOutcome = percentChange(currentPoint, avgOutcome)
        pattern.append(p01)
        pattern.append(p02)
        pattern.append(p03)
        pattern.append(p04)
        pattern.append(p05)
        pattern.append(p06)
        pattern.append(p07)
        pattern.append(p08)
        pattern.append(p09)
        pattern.append(p10)

        patternAR.append(pattern)
        performanceAR.append(futureOutcome)

        print currentPoint
        print '____'

        print p01, p02, p03, p04, p05, p06, p07, p08, p09, p10
        y+=1

    patEndTime = time.time()

    print len(patternAR)
    print len(performanceAR)
    print 'Pattern storage took ', patEndTime - patStartTime, ' seconds'

def graphRawFX():


    fig = plt.figure(figsize=(10,7))
    ax1 = plt.subplot2grid((40,40), (0,0), rowspan=40, colspan=40)

    ax1.plot(date, bid)
    ax1.plot(date, ask)
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax1_2 = ax1.twinx()
    ax1_2.fill_between(date, 0, (ask-bid), facecolor='g', alpha=.3)



    plt.subplots_adjust(bottom=.23)

    plt.grid(True)
    plt.show()

#graphRawFX()
patternStorage()
