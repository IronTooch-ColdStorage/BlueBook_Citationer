
from Classes.Abbreviation import Abbreviation
from Classes.CourtAbbrev import CourtAbbreviation
from Classes.ReporterAbbreviation import ReporterAbbreviation

FULL_CITATION = 1
EMBEDDED_END = 2
EMBEDDED_MIDDLE = 3
SHORT_FORM = 4
ALTERNATE_SHORT_FORM = 5

COURT_SHORT_NAME_POSTION = 1
COURT_LONG_NAME_POSTION = 0
COURT_IS_STATE_COURT_POSTION = 2


REPORTER_LONG_NAME_POSITION = 0
REPORTER_SHORT_NAME_POSITION = 1
REPORTER_ISSTATEREPORTER_POSITION = 2
REPORTER_ISCOURTSPECIFIC_POSITION = 3

def RemovableSuffixes() -> list:

    lstSuffixes = getCleanList("./Raw_Data/Suffixes.txt")
    return lstSuffixes

def getCourts() -> list:
    lstCourtLines = getCleanList("./Raw_Data/Courts.txt")

    lstCourts = []

    for line in lstCourtLines:
        tmpCourt = CourtAbbreviation()
        lstCourtTokens = str(line).split(";")
        tmpCourt.bolIsStateCourt = bool(lstCourtTokens[COURT_IS_STATE_COURT_POSTION])
        tmpCourt.strShortForm = str(lstCourtTokens[COURT_SHORT_NAME_POSTION])
        tmpCourt.strLongForm = str(lstCourtTokens[COURT_LONG_NAME_POSTION])
        lstCourts.append(tmpCourt)
    
    return lstCourts
        
def getCourtShortName(strLongName: str) -> str:
    lstCourts = getCourts()
    strSearchedCourtLower = str(strLongName.lower())
    strSearchedCourtLower = strSearchedCourtLower.removeprefix("the ")

    for court in lstCourts:
        strTokenCourtLower = str(court.strLongForm).lower()
        if strTokenCourtLower in strSearchedCourtLower:
            return CourtAbbreviation(court).strShortForm
    return "COURT NOT FOUND ( " + strLongName + ")"

def getReporters() -> list:
    lstReporterLines = getCleanList("./Raw_Data/Reporters.txt")
    # Remove the Note Field
    lstReporterLines.pop(0)
    lstReporters = []

    for line in lstReporterLines:
        lstReporterToken = str(line).split(";")
        tmpReporter = ReporterAbbreviation()
        tmpReporter.strLongForm = str(lstReporterToken[REPORTER_LONG_NAME_POSITION])
        tmpReporter.strShortForm = str(lstReporterToken[REPORTER_SHORT_NAME_POSITION])
        tmpReporter.bolIsCourtSpecificReporter = bool(lstReporterToken[REPORTER_ISCOURTSPECIFIC_POSITION])
        tmpReporter.bolIsStateReporter = bool(lstReporterToken[REPORTER_ISSTATEREPORTER_POSITION])
        
        
        lstReporters.append(tmpReporter)
    
    return lstReporters

def getReporterShortName(strLongName: str) -> str:
    lstReporters = getReporters()

    for reporter in lstReporters:
        if reporter.strLongForm in strLongName:
            return Abbreviation(reporter).strShortForm
    return "REPORTER NOT FOUND ( " + strLongName + ")"

def getCleanList(strFile: str) -> list:
    file = open(strFile, "r")
    lstLines = file.readlines()
    lstNewList = []

    for line in lstLines:
        lstNewList.append(line.strip())
    
    return lstNewList