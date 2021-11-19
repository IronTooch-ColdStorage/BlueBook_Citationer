from os import remove
from types import new_class
from distutils import util
from Case import *
import Constants



# Make table of courts
# Make table of abbreviations
# Make table of states
Constant = Constants.Constants()

def full_case_citation(myCase: Case) -> str:

    strCitation = ""

    strParties = getFullCiteParties(myCase)
    strLocation = getFullCiteLocation(myCase)
    strParenthetical = getParenthetical(myCase)
    

    strCitation = strParties + strLocation + strParenthetical

    #print(strCitation)
    return strCitation
    
def getFullCiteParties(myCase: Case) -> str:
    strFirstParty = getPartyName(myCase.strFirstPartyComplete, myCase.bolFirstPartyIsBusiness)
    strSecondParty = getPartyName(myCase.strSecondPartyComplete, myCase.bolSecondPartyIsBusiness)
    strParties = strFirstParty + " v. " + strSecondParty + ", "

    return strParties

def getFullCiteLocation (myCase: Case) -> str:
    
    strLocation = ""
    strVolumeNumber = getVolumeNumber(myCase.strCaseLocation)

    strBeginningPage = getBeginningPage(myCase.strCaseLocation)

    strVolumeAbbreviation = Constant.getReporterShortName(myCase.strCaseLocation)

    strPinLocation = myCase.strPinLocation

    strLocation = strVolumeNumber + " " + strVolumeAbbreviation + " " + strBeginningPage + ", " + strPinLocation + " "

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


    strShortCourtName = Constant.getCourtShortName(myCase.strCourt)
    # TODO If State Court and Reporter is state Reporter, omit state
    # TODO If State Court and Reporter has specific Jurisdiction, omit both


    

    strDecidedYear = myCase.getDecidedYear()
    bolIsCourtReporter = Constant.getReporterIsCourtReporter(myCase.strCaseLocation)

    if bolIsCourtReporter:
        return  "(" +  strDecidedYear + ")."

    else:

        return "(" + strShortCourtName + " " + strDecidedYear + ")."

def citationClauseMiddle(myCase: Case) -> str:
    strFullCite = full_case_citation(myCase)
    strMiddleCite = strFullCite.removesuffix(".")
    strMiddleCite = strMiddleCite + ","

    return strMiddleCite