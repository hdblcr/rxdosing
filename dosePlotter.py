from matplotlib import pyplot
import numpy as np
import math


def nextX(x, lamb, t=2):
    return x * math.exp(-1 * lamb * t)


def plotGraph(dose):
    '''
    Takes list of lists of dosages dispensed every 12 hours,
    maps them, and plots them
    '''
    # declare variables
    lamb = math.log(2) / 12  # time will be in terms of 12 hour intervals
    scene = []
    t = np.arange(0, 12*121*2, 12)

    # determine starting point for each new day
    for i in range(len(dose)):
        nextList = []
        for j in range(len(dose[i])):
            if (j == 0):
                nextList.append(dose[i][j])
            else:
                nextList.append(dose[i][j-1] + nextX(dose[i][j-1], lamb))
        scene.append(nextList)

    # Plot dosages
    pyplot.plot(t, np.asarray(scene[0]))
    pyplot.plot(t, np.asarray(scene[1]))
    pyplot.plot(t, np.asarray(scene[2]))
    pyplot.plot(t, np.asarray(scene[3]))
    pyplot.show()


def main():
    doseA = 60
    doseB = 40
    dose = []

    for i in range(4):
        dose.append([])
        for j in range(21):
            dose[i].append(doseA)
            dose[i].append(0)

    # regular daily doses, no change, 60 per 24 hours
    for i in range(100):
        dose[0].append(doseA)
        dose[0].append(0)

    # alternating high-low daily dose
    for i in range(50):
        dose[1].append(doseA)
        dose[1].append(0)
        dose[1].append(doseB)
        dose[1].append(0)

    for i in range(33):
        dose[2].append(doseA)
        dose[2].append(0)
        dose[2].append(doseB)
        dose[2].append(0)
        dose[2].append(doseB)
        dose[2].append(0)
    dose[2].append(doseA)
    dose[2].append(0)

    for i in range(20):
        dose[3].append(doseA)
        dose[3].append(0)
        dose[3].append(doseB)
        dose[3].append(0)
        dose[3].append(doseB)
        dose[3].append(0)
        dose[3].append(doseB)
        dose[3].append(0)
        dose[3].append(doseB)
        dose[3].append(0)

    plotGraph(dose)


if __name__ == '__main__':
    main()
