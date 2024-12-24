import vinTerminalFormatting as v
import vinFileManagement
import AppData.Cbzs2Pics as Cbzs2Pics
import AppData.Epubs2Pics as Epubs2Pics
import AppData.Pics2Cbzs as Pics2Cbzs

while True:

    operation = v.inputSpecial("0: Pics to Cbz. 1: Cbz to Pics. 2: Epub to Pics. | ", v.Blue+v.Bright, v.Green+v.Bright)
    if operation not in ["1", "2", "0"]:
        v.printSpecial("Invalid input. Retry.", v.Red)
        print()
        continue
    print()

    print("Enter nothing for default path.")
    mainFolderPath = v.inputSpecial("Main Folder Path: ", inputAttribute=v.Green+v.Bright)
    if not mainFolderPath:
        mainFolderPath = r"D:\Code\ProgramFiles\CbzAndEpub\Welcome"
    if not vinFileManagement.doesFolderExist(mainFolderPath):
        v.printSpecial("This folder doesn't exist. Retry.", v.Red)
        print()
        continue
    print()

    if operation == "0":
        Pics2Cbzs.pics2cbzs(mainFolderPath)
    elif operation == "1":
        Cbzs2Pics.cbzs2pics(mainFolderPath)
    else:
        Epubs2Pics.epubs2pics(mainFolderPath)
