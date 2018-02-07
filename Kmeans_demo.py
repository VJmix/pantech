import matplotlib
import numpy as np
import scipy
import imutils
import os
import subprocess
from PIL import Image
from imutils import contours
from sklearn.cluster import KMeans
from sklearn.cluster import spectral_clustering


# I want to put logo on top-left corner, So I create a ROI
roi = np.array([[1, 2], [1, 4], [1, 0],[4, 2], [4, 4], [4, 0]])
imgkmeans = KMeans(n_clusters=2, random_state=0);
imgkmeans.fit(roi);
label_values=imgkmeans.labels_;


print label_values
