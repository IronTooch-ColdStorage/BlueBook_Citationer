from os import remove
from types import new_class
from distutils import util
from Case import *
import Constants



def short_form_case_citation(myCase: Case) -> str:
    # The name of the first party to the action, underlined or italicized. Omit the other party's name.
    #The volume number; reporter name, abbreviated; the word "at"; and the pinpoint page number.
    # When used in a citation sentence place a period at the end of the citation.


    strCitation = ""

    strParties = getShortCiteParties(myCase)
    strLocation = getShortCiteLocation(myCase)
    

    strCitation = strParties + ", " + strLocation

    #print(strCitation)
    return strCitation

def getShortCiteParties(myCase: Case) -> str:
    strFirstParty = getPartyName(myCase.strFirstPartyComplete, myCase.bolFirstPartyIsBusiness)

    return strFirstParty

def getShortCiteLocation (myCase: Case) -> str:
    
    strLocation = ""
    strVolumeNumber = getVolumeNumber(myCase.strCaseLocation)

    strVolumeAbbreviation = Constant.getReporterShortName(myCase.strCaseLocation)

    strPinLocation = myCase.strPinLocation

    strLocation = strVolumeNumber + " " + strVolumeAbbreviation + " at " + strPinLocation + "."

    return strLocation