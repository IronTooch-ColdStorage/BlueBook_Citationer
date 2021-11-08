from os import remove
from types import new_class
from distutils import util
from Classes.Case import Case
from Classes import *
import Constants



# Make table of courts
# Make table of abbreviations
# Make table of states


def full_case_citation():
    
    myCase = Case.getCaseInput()

    strCitation = ""

    strParties = getFullCiteParties(myCase)
    strLocation = getLocation(myCase)
    strParenthetical = getParenthetical(myCase)
    

    strCitation = strParties + strLocation + strParenthetical

    print(strCitation)
    
def getFullCiteParties(myCase: Case) -> str:
    strFirstParty = Case.getPartyName(myCase.strFirstPartyComplete, myCase.bolFirstPartyIsBusiness)
    strSecondParty = Case.getPartyName(myCase.strSecondPartyComplete, myCase.bolSecondPartyIsBusiness)
    strParties = strFirstParty + " v. " + strSecondParty + ", "

    return strParties

def getLocation (myCase: Case) -> str:
    
    strLocation = ""
    strVolumeNumber = Case.getVolumeNumber(myCase.strCaseLocation)

    strBeginningPage = Case.getBeginningPage(myCase.strCaseLocation)

    strVolumeAbbreviation = Constants.getReporterShortName(myCase.strCaseLocation)

    strLocation = strVolumeNumber + " " + strVolumeAbbreviation + " " + strBeginningPage + ", " + str(myCase.intFirstPinLocation) + " "

    return strLocation


    
def tokenize_party(strParty):

    string_tokens = str(strParty).split()

    for token in string_tokens:
        # If abbreviate and token is abbreviatable, abbreviate
        print("...")
        print(token) 
    




def readWholeVolume(strCaseLocation: str) -> str:

    string_tokens = strCaseLocation.split(",")
    for token in string_tokens:
        # If abbreviate and token is abbreviatable, abbreviate
        print("...")
        print(token)

def getParenthetical(myCase: Case) -> str:


    strShortCourtName = Constants.getCourtShortName(myCase.strCourt)
    # TODO If State Court and Reporter is state Reporter, omit state
    # TODO If State Court and Reporter has specific Jurisdiction, omit both

    strDecidedYear = myCase.getDecidedYear()

    return "(" + strShortCourtName + " " + strDecidedYear + ")."