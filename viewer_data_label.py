import matplotlib.pyplot as plt


# Mouse scroll event.
def mouse_scroll(event):
    fig = event.canvas.figure
    ax = fig.axes
    if event.button == 'down':
        next_slice(ax)
    elif event.button == 'up':
        next_slice_up(ax)
    fig.canvas.draw()


# Next slice func.
def next_slice(ax):
    volume_data = ax[0].volume
    volume_label = ax[1].volume
    ax[0].index = (ax[0].index + 1) % volume_data.shape[0]
    img1.set_array(volume_data[ax[0].index, :, :])
    img2.set_array(volume_label[ax[0].index, :, :])
    ax[0].text(12, 40, str(ax[0].index), bbox={'facecolor': 'orange', 'pad': 10})


# Next slice func.
def next_slice_up(ax):
    volume = ax[0].volume
    volume_label = ax[1].volume
    if ax[0].index >= 1:
        ax[0].index = (ax[0].index - 1) % volume.shape[0]
        img1.set_array(volume[ax[0].index, :, :])
        img2.set_array(volume_label[ax[0].index, :, :])
        ax[0].text(12, 40, str(ax[0].index), bbox={'facecolor': 'orange', 'pad': 10})


def plot_data_label(volume_data, volume_label):
    global img1, img2
    fig, ax = plt.subplots(ncols=2)

    ax[0].volume = volume_data
    ax[0].index = 1
    fig.canvas.mpl_connect('scroll_event', mouse_scroll)

    img1 = ax[0].imshow(volume_data[ax[0].index, :, :], cmap='gray', vmin=0, vmax=255)
    ax[0].set_title('Ring scan', pad=22)
    ax[0].title.set_size(25)
    ax[0].set_ylabel('Z axis [ ]', labelpad=18)
    ax[0].yaxis.label.set_size(20)
    ax[0].set_xlabel('number of A scans [ ]', labelpad=18)
    ax[0].xaxis.label.set_size(20)

    ax[1].volume = volume_label
    img2 = ax[1].imshow(volume_label[ax[0].index, :, :], cmap='gray', vmin=0, vmax=3)
    ax[1].set_title('Ring scan Label', pad=22)
    ax[1].title.set_size(25)
    ax[1].set_xlabel('number of A scans [ ]', labelpad=18)
    ax[1].xaxis.label.set_size(20)
    ax[1].yaxis.set_major_locator(plt.NullLocator())

    plt.show()
