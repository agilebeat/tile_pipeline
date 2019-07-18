# -*- coding: utf-8 -*-



"""
working directory must be the folder where images are downloaded from S3
initiall, create 'archive.txt' file with empty in the working directory
"""
import os
os.chdir('/home/wilson/Documents/new_tiles')

working_dir = '/home/wilson/Documents/new_tiles'
tile_collection_dir = '/home/wilson/Documents/tile_collection'



def tile_collect(working_dir, tile_collection_dir):
    """
    Parameters:
    - working_dir: directory path where images are downloaded from S3
    - tile_collection_dir: path where images will be saved for trining model
    Do not make tile_collection directory in the currrent working dir.
    Output & result : 
    - print the number of downloaded images from S3
    - print the number of updated images for training model
    - updated files are moving to tile_collection_dir
    - delete downloaded images from S3 
    """
    import os
    os.chdir(working_dir)
    
###--- change tile names using Z,X,Y (e.g) 18_1234_6789.png
    Z = [z for z in os.listdir('.') if os.path.isfile(z)==False]
    path = os.getcwd()
    
    for level in Z:
        for X in os.listdir(level):
            for Y in os.listdir(level + '/' + X):   
                os.rename(os.path.join(path,level,X,Y), 
                      os.path.join(path, level, X, level + '_' + X + '_' + Y))
                
                
###--- build list of collected tile names (save as a set)
    current_tiles = []
    for level in Z:
        for X in os.listdir(level):
            for Y in os.listdir(level + '/' + X):
                current_tiles.append(Y)
                 
    current_tiles = set(current_tiles)
    num_downloaded_img = len(current_tiles)

 
###--- Load archive.txt and compare to new_tiles    
    archive = set(line.strip() for line in open('archive.txt'))   # open as set   
    new_tiles =  current_tiles.difference(archive)       # only new tiles
#    print('the number of updated images: {}'.format(len(new_tiles))
    num_updated_img = len(new_tiles)


###--- Move new tiles to 'tile_collection' directory
    import shutil

    for level in Z:
        for X in os.listdir(level):
           for Y in os.listdir(level + '/' + X):
               if Y in new_tiles:
                   path_ZXY = os.path.join(path, level, X, Y)               
                   shutil.move(path_ZXY, tile_collection_dir)
                
###---  update archive.txt

    updated_archive = archive.union(new_tiles)

    with open('archive.txt', 'w') as archive:
        for file in list(updated_archive):
            print(file, file = archive)
            
###---  empty current directory 
    for level_dir in Z:
        path_level_dir = os.path.join(path, level_dir)            
        shutil.rmtree(path_level_dir, ignore_errors=True)
    
    a = print('the number of downloaded images: {}'.format(num_downloaded_img))
    b = print('the number of updated images: {}'.format(num_updated_img))     
    
    return a, b
    




tile_collect(working_dir, tile_collection_dir)

    




 






