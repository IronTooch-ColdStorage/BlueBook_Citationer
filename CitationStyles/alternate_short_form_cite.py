from os import remove
from types import new_class
from distutils import util
from Classes.Case import Case
from Classes import *

import Constants

def alt_short_form_case_citation():
    # The name of the first party to the action, underlined or italicized. Omit the other party's name.
    #The volume number; reporter name, abbreviated; the word "at"; and the pinpoint page number.
    # When used in a citation sentence place a period at the end of the citation.

    myCase = Case.getCaseInput()

    strCitation = ""

    strParties = getAltShortCiteParties(myCase)
    strLocation = getAltShortFormLocation(myCase)

    strCitation = strParties + strLocation


    print(strCitation)

def getAltShortCiteParties(myCase: Case) -> str:
    strFirstParty = Case.getPartyName(myCase.strFirstPartyComplete, myCase.bolFirstPartyIsBusiness)
    strParties = strFirstParty + ", "

    return strParties

def getAltShortFormLocation(myCase: Case) -> str:

    strLocation = ""
    strVolumeNumber = Case.getVolumeNumber(myCase.strCaseLocation)
    strVolumeAbbreviation = Constants.getReporterShortName(myCase.strCaseLocation)

    strLocation = strVolumeNumber + " " + strVolumeAbbreviation + " at " + str(myCase.intFirstPinLocation) + "."

    return strLocation