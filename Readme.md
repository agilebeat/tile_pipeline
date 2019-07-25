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


# How to use github

## Clone

To clone repository you have to run command:

`git clone <repository url>`

Comment:

At this point you don't have privilage to push back to the repository. If you have a new version of git 
when you run command `git push` it will ask you for username and password. If have old version it will fail.
However the fix is really easy. To fix it do:

1. Enter to the cloned folder (git has created `tile_pipeline` folder for you)
2. You should see all the files plus hidden folder .git (On linux hidden folders/files start with dot)
3. Open follwoing file for edit `.git/config`

```
[core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
[remote "origin"]
        url = https://github.com/agilebeat-inc/tile_pipeline.git
        fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
        remote = origin
        merge = refs/heads/master
```

Now in the remote section `[remote "origin"]` modify url part as follwing

```
[core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
[remote "origin"]
        url = https://<GIT USER NAME>@github.com/agilebeat-inc/tile_pipeline.git
        fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
        remote = origin
        merge = refs/heads/master

```

4. Save the changes (If you are using vim as editior just pres ESC+wq)
5. Run git push
