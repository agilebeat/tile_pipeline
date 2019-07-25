# Update model procedure

1. Checkout the tile_pipeline repository (if you don't have it already)
2. Delete file `classifier.h5` from the prject (rel. path  `tile_collection/classifier.h5`)
3. Copy new classifierDDMM.h5 file to the `tile_collection` as classifier.h5
4. Run 
   `git add tile_collection/classifier.h5`
5. Run commit:
   `git commit -m "MODEL UPDATE: model version"`
6. Run push:
   `git push`

### To run the process just run docker

1. Start the agilebeat docker container

`docker run -v /Users/mdwulit/.aws:/root/.aws -v <PATH TO THE TILE_PIPELINE PROJECT>tile_pipeline:/notebooks -p 8888:8888 docker_image_id`


### Comments

1. Do not check in the tiles by themselves
2. Check the updated archive.txt file so that others don't process the same files.

#### If you have used this project before and model has not been updated yet

1. Just navigate to the tile_pipeline preject
2. Run git pull
3. Run docker (previous section) and off you go
