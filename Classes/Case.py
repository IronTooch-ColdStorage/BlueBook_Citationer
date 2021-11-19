
import time
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
classesdir = parentdir + "\\Classes"

sys.path.insert(0, str(classesdir))

import Constants
from distutils import util

from HelperFunctions import HelperFunctions

Constant = Constants.Constants()

class Case:

    strFirstPartyComplete = "FirstParty"
    bolFirstPartyIsBusiness = False

    strSecondPartyComplete = "SecondParty"
    bolSecondPartyIsBusiness = False


    strCourt = "MyCourt"

    strCaseLocation = "MyReporterLocation"

    strDateDecidedDate = "January 1, 1900"

    intBeginningPage = 1
    intFirstPinLocation = 2

    strDocketNumber = "MyDocket1"
    strPinLocation = ""

    


    def getDecidedYear(self) -> str:

        self.strDateDecidedDate = str(self.strDateDecidedDate).strip()
        try: 
            dtDecidedDate = HelperFunctions.getDate(self.strDateDecidedDate)
        except ValueError:
                return "INVALID DATE"
        #print(dtDecidedDate.tm_year)
        return str(dtDecidedDate.tm_year)

    def getBeginningPage(strCaseLocation: str) -> str:
    #Yank everything before "beginning on page"
        strStartPage = strCaseLocation.split("beginning on page ").pop()
        return strStartPage
        
def getReporterCite(strFullLocationFound: str) -> str:

    intVolumeNumber = -1
    strVolumeName = "-1"
    strVolumeEdition = "-1"
    intBeginningLocation = -1
    strAbbreviatedVolumeName = "-1"
    strAbbreviatedVolumeEdition = "-1"

    #print( str(intVolumeNumber) + " " + strAbbreviatedVolumeName + strAbbreviatedVolumeEdition + " " + str(intBeginningLocation))
    
def getPartyName(strPartyFullName: str, bolIsBusiness: bool) -> str:
    
    strPartyName = ""
    if not bolIsBusiness:
        strPartyName = getPartyLastName(strPartyFullName)
        return strPartyName
    #TODO If Party is Business...

def getPartyLastName(strPartyName: str) -> str:

    if (strPartyName == ""):
        return ""
    strPartyName = removeSuffixes(strPartyName)
    string_tokens = str(strPartyName).split()
    return string_tokens.pop()

def removeSuffixes(strParty: str) -> str:
    strParty = strParty.strip()
    lstSuffixes = Constant.getRemovableSuffixes()

    for strSuffix in lstSuffixes:
        strParty = strParty.removesuffix(strSuffix)

    strParty = strParty.strip()
    strParty = strParty.removesuffix(",")
    return strParty

def getVolumeNumber(strCaseLocation: str) -> str:

    
    # Get string to first comma

    #Volume 805 of the North Western Reporter, second series, beginning on page 1
    string_tokens = strCaseLocation.split(",") #[Volume 805 of the North Western Reporter, second series, beginning on page 1]


    volumeNumber = string_tokens[0].split(" of the ")[0] #[Volume 805, North Western Reporter]
    splitTokens = volumeNumber.split()
    if len(splitTokens) == 0:
        return "INVALID"
    volumeNumber = splitTokens.pop()
    return volumeNumber

def getBeginningPage(strCaseLocation: str) -> str:
    #Yank everything before "beginning on page"
    strStartPage = strCaseLocation.split("beginning on page ").pop()
    return strStartPage

def getCaseInput() -> Case:
    
    myCase = Case()

    print("Who is the first party?")

    myCase.strFirstPartyComplete = input()

    print("Is First Party a business?   Default is No")

    strUserInput = input()
    if strUserInput == "":
        bolIsBuisness = False
    else:
        bolIsBuisness = bool(util.strtobool(input()))
    myCase.bolFirstPartyIsBusiness = bolIsBuisness

    print("Who is the second party?")
    myCase.strSecondPartyComplete = input()

    print("Is Second Party a business?  Default is No")


    strUserInput = input()
    if strUserInput == "":
        bolIsBuisness = False
    else:
        bolIsBuisness = bool(util.strtobool(input()))

    myCase.bolSecondPartyIsBusiness = bolIsBuisness

    print("Abbreviate? True / False")
    abbreviate =  input()

    print("What court is the case in?")
    myCase.strCourt =  input()

    print("Where is the case found?")
    myCase.strCaseLocation = input()

    print("When was the case decided?")
    myCase.strDateDecidedDate = input()

    print("Where is the pin cite to?")
    myCase.intFirstPinLocation = input()

    return myCase