import numpy as np
from skimage import io
from skimage import morphology
import matplotlib.pyplot as plt

io.use_plugin('matplotlib')

# test image from Matlab bwmorph('skel') demo
bw = io.imread('circles.png') > 0

sk0 = morphology.skeletonize(bw)
sk1 = morphology.medial_axis(bw).astype(np.uint8)

f, (ax0, ax1) = plt.subplots(1, 2)

ax0.imshow(bw + sk0, cmap=plt.cm.gray, interpolation='nearest')
ax0.set_title('Skeletonize')

ax1.imshow(bw + sk1, cmap=plt.cm.gray, interpolation='nearest')
ax1.set_title('Medial axis')

plt.show()
