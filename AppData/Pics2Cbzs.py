import vinFileManagement_Base
from natsort import natsorted
import os
import zipfile

def pics2cbzs(mainFolderPath):
    listOfFolders = vinFileManagement_Base.getFoldersInFolder_std(mainFolderPath)
    for folder in listOfFolders:
        