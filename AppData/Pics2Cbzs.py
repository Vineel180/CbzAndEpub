import vinFileManagement
from natsort import natsorted
import os
import zipfile

def pics2cbzs(mainFolderPath):
    listOfFolders = vinFileManagement.getFoldersInFolder_std(mainFolderPath)
    for folder in listOfFolders:
        