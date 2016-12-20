#!/bin/python

import argparse
import operator
import itertools
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

COLORS = {
    'Pending': '#ffb624',
    'ContainerCreating': '#ebeb00',
    'Running': '#50c878',
    'Terminating': '#a366ff',
    'Error': '#cc0000',
}

def main():
    parser = argparse.ArgumentParser(prog='pod-stats')
    parser.add_argument('data', nargs='+')
    args = parser.parse_args()

    source = args.data[0]
    data = np.genfromtxt(source, dtype=None, delimiter=',',
                         skip_header=1, skip_footer=0,
                         names=['time', 'name', 'status'])
    categories = list(set(x[2] for x in data))
    categories.sort()

    processed = []
    t = []
    base_time = data[0][0]

    for k, g in itertools.groupby(data, key=operator.itemgetter(0)):
        r = dict((c, 0) for c in categories)
        for x in g:
            r[x[2]] += 1

        v = [r[c] for c in categories]
        processed.append(v)
        t.append(k - base_time)

    figure = plt.figure()
    plot = figure.add_subplot(111)

    colors = [COLORS[c] for c in categories]

    plot.stackplot(t, np.transpose(processed), colors=colors)

    if len(args.data) > 1:
        y = []
        x = []
        with open(args.data[1]) as fd:
            cnt = fd.read()
        for i, p in enumerate(cnt.strip().split('\n')):
            x.append(int(p) / 1000.0 - base_time)
            y.append(i)
        plot.plot(x, y, 'b.')

    plot.grid(True)
    plot.set_xlabel('time, s')
    plot.set_ylabel('pods')

    ax = figure.gca()
    ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))

    # add legend
    patches = [mpatches.Patch(color=c) for c in colors]
    texts = categories

    if len(args.data) > 1:
        patches.append(mpatches.Patch(color='blue'))
        texts.append('Pod report')

    legend = plot.legend(patches, texts, loc='right', shadow=True)

    for label in legend.get_texts():
        label.set_fontsize('small')

    plt.show()
    figure.savefig('figure.svg')

if __name__ == '__main__':
    main()
