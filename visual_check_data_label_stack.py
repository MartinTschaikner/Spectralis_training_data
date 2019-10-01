import numpy as np
from viewer_data_label import plot_data_label

# load data to visualize
real_ring_scan = np.load('ring_scan_stack/ring_scan_stack.npy')
real_ring_scan_label = np.load('ring_scan_stack/ring_scan_label_stack.npy')
aug_ring_scan = np.load('aug_ring_scan_stack/aug_ring_scan_stack.npy')
aug_ring_scan_label = np.load('aug_ring_scan_stack/aug_ring_scan_label_stack.npy')

test_stack = np.load(r'ring_scan_stack_test/ring_scan_stack.npy')
test_stack_label = np.load(r'ring_scan_stack_test/ring_scan_label_stack.npy')

plot_data_label(test_stack[:, :, :, 0], test_stack_label[:, :, :, 0])
