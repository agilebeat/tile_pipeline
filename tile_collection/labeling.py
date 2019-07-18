"""
Require to have 'classifier.h5' file in working directory
"""

import os
import glob

from keras.models import load_model
from keras.preprocessing import image
import shutil
import numpy as np

###--- path of tile_collection,
#              Rail where railroad images will be saved and
#              Other where other images will be saved
tile_collection_dir = '/home/swilson/Documents/tile_collection/'
Rail_Img_dir = '/home/swilson/Documents/tile_collection/Rail/'
Other_Img_dir = '/home/swilson/Documents/tile_collection/Other/'


###---- list of tiles to be separated to 'Rail' and 'Other'


path_where_tiles_are = glob.glob(os.path.join(tile_collection_dir, '*.png'))

###--- load classifier and pass tiles to separate classes
classifier = load_model('classifier.h5')
classifier.compile(loss = 'categorical_crossentropy', optimizer = 'rmsprop', metrics=['accuracy'])

for raw_img in path_where_tiles_are:
    #-- image processing
    img_width, img_height = 256, 256
    img = image.load_img(raw_img, target_size=(img_width, img_height))
    img = image.img_to_array(img)/255.
    img = np.expand_dims(img, axis=0)

    pred = classifier.predict_classes(img)

    if pred[0] == 1:
        shutil.move(raw_img,  Rail_Img_dir)
    elif pred[0] == 0:
        shutil.move(raw_img, Other_Img_dir)



