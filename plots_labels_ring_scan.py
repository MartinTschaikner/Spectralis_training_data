"""

This file contains the following functions:

Plots ring_scan and corresponding labels for visual check.
"""

import numpy as np
import matplotlib.pyplot as plt


def label_ring_scan_plots(ring_scan_data, label_data, ilm_seg, rpe_seg, rnfl_seg):

    # plt.rc('text', usetex=True)
    # plt.rc('font', family='serif')

    noe = np.size(ring_scan_data, 1)
    num_rows = np.size(ring_scan_data, 0)

    fig, (ax1, ax2) = plt.subplots(ncols=2)
    ax1.plot(np.arange(0, noe), ilm_seg, color='green', linewidth=3.0)
    ax1.plot(np.arange(0, noe), rpe_seg, color='blue', linewidth=3.0)
    ax1.plot(np.arange(0, noe), rnfl_seg, color='red', linewidth=3.0)
    ax1.imshow(ring_scan_data, cmap='gray', vmin=0, vmax=255, extent=(0, noe, num_rows, 0))
    ax1.set_title('Spectralis APS ring scan', pad=22)
    ax1.title.set_size(25)
    ax1.set_xlabel('number of A scans [ ]', labelpad=18)
    ax1.set_ylabel('Z axis [ ]', labelpad=18)
    ax1.xaxis.label.set_size(20)
    ax1.yaxis.label.set_size(20)

    ax2.plot(np.arange(0, noe), ilm_seg, color='green', linewidth=1.0)
    ax2.plot(np.arange(0, noe), rpe_seg, color='blue', linewidth=1.0)
    ax2.plot(np.arange(0, noe), rnfl_seg, color='red', linewidth=1.0)
    ax2.imshow(label_data, cmap='gray', vmin=0, vmax=3, extent=(0, noe, num_rows, 0))
    ax2.set_title('Ring scan Label', pad=22)
    ax2.title.set_size(25)
    ax2.set_xlabel('number of A scans [ ]', labelpad=18)
    ax2.xaxis.label.set_size(20)
    ax2.yaxis.set_major_locator(plt.NullLocator())
    plt.show()

    return
