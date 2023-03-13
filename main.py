import os

fileName = input("Enter name for file: ")

imageDir = "./" + fileName + "/images"

texDir = "./" + fileName

texFile = "./" + fileName + "/" + fileName + ".tex"

print(imageDir)
print(texFile)

if os.path.exists(texDir) == False:
    os.mkdir(texDir)

if os.path.exists(imageDir) == False:
    os.mkdir(imageDir)

with open(texFile,"w") as f:
    with open("filler.txt", "r") as fill:
        filler = fill.readlines()

    f.writelines(filler)
