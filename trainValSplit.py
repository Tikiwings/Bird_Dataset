import shutil
import os

BASEPATH    = os.getcwd() + "/ourSpec"
TRAINPATH   = BASEPATH + "/train/"
VALPATH     = BASEPATH + "/val/"

splitRatio = 0.2

#print(BASEPATH)

classList = os.listdir(BASEPATH)
print(classList)

for birdClass in classList:
   birdPath = BASEPATH + "/" + birdClass
   birdFiles = os.listdir(birdPath)
   
   splitIndex = len(birdFiles) // splitRatio
   trainFiles = birdFiles[:splitIndex]
   valFiles   = birdFiles[splitIndex:]
   
   #move train and val files
   for f in trainFiles:
      shutil.move(birdPath + "/" + f, TRAINPATH)

   for f in valFiles:
      shutil.move(birdPath + "/" + f, VALPATH)



