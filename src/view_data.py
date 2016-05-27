import sys
from util import get_cached_data
import matplotlib.pyplot as plt
import numpy as np

def main():
    '''
    TODO: explain this
    '''
    path_to_data = sys.argv[-1]
    data_type = sys.argv[-2]
    if data_type == '-spec':
        ids, sets, specs, fs, ts = get_cached_data(path_to_data)
        for ident, set_name, spec in zip(ids, sets, specs):
            plt.pcolormesh(ts[:spec.shape[1]], fs[:spec.shape[0]], spec)
            plt.ylabel('Frequency [Hz]')
            plt.xlabel('Time [sec]')

            maxlabel = 'max: ' + str(np.max(spec))
            meanlabel = 'mean: ' + str(np.mean(spec))

            plt.title(','.join([ident, set_name, maxlabel, meanlabel]))
            plt.show()

    else:
        print('only works for spectrograms at the moment')


if __name__ == '__main__':
    main()
