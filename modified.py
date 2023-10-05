from os import listdir, remove
from os.path import isfile, join
import hashlib

#a hash is a kind of "signature"

BLOCK_SIZE = 65536 #for hash purpose
mypath  = "C:\\Users\\chris\\Desktop\\ctf challenge\\modified" #the path of the folder with images

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))] #an array with the name of every images in the folder



def main(): #the function to execute
    uniqueHashs = [] #the array containing the hash of every single file
    uniqueHashs.append('test') #just to make the array not empty
    for actualFile in onlyfiles:  #the loop to test every file
        actualFile = mypath + actualFile #here we concatenate the path and the filename, to have a full path
        deleted = 0 

        hashOfFile = hashFile(actualFile) #calculate the hash of the file
        for comparaisonHash in uniqueHashs: #test if the hash already exist
            if (hashOfFile == comparaisonHash and deleted != 1): #if yes, we delete the file
                remove(actualFile)
                deleted = 1
        if (deleted != 1):
            uniqueHashs.append(hashOfFile) #else, we keep the file and add it's hash in the array
    return 0;


def hashFile(file_path):
    md5 = hashlib.md5()
    with open(file_path, "rb") as file:
        while True:
            data = file.read(8192)  # Read in 8KB chunks
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()