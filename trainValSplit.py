import shutil
import os

BASEPATH    = os.getcwd() + "/ourSpec"
#TRAINPATH   = BASEPATH + "/train/"
#VALPATH     = BASEPATH + "/val/"
TRAINPATH   = os.getcwd() + "/train/"
VALPATH     = os.getcwd() + "/val/"

splitRatio = 0.8 #ex: 0.8 = 80% -> train | 20% -> val

#print(BASEPATH)

classList = os.listdir(BASEPATH)
print(classList)

for birdClass in classList:
   birdPath = BASEPATH + "/" + birdClass
   birdFiles = os.listdir(birdPath)
   
   splitIndex = int(len(birdFiles) * splitRatio)
   trainFiles = birdFiles[:splitIndex]
   valFiles   = birdFiles[splitIndex:]
   
   #move train and val files
   for f in trainFiles:
      #shutil.move(birdPath + "/" + f, TRAINPATH + birdClass)
      shutil.copy(birdPath + "/" + f, TRAINPATH + birdClass)

   for f in valFiles:
      #shutil.move(birdPath + "/" + f, VALPATH + birdClass)
      shutil.copy(birdPath + "/" + f, VALPATH + birdClass)



