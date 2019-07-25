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


