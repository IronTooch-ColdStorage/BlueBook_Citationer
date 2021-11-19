
from Abbreviation import Abbreviation
from CourtAbbrev import CourtAbbreviation
from ReporterAbbreviation import ReporterAbbreviation
import distutils

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

CITATION_TYPE_FULLTEXT_STR = "Full Text Citation"
CITATION_TYPE_EMBEDDED_END_STR = "Embedded citation (end of line)"
CITATION_TYPE_EMBEDDED_MIDDLE_STR = "Embedded citation (middle of line)"
CITATION_TYPE_SHORT_FORM_STR = "Short form citation"
CITATION_TYPE_ALT_SHORTFORM_STR = "Alternate Short Form Citation"

class Constants:
    lstAbbreviations = []
    lstReporters = []
    lstCourts = []
    lstSuffixes = []


    def __init__(self):
        self.lstReporters = self.getReporters()
        self.lstCourts = self.getCourts()
        self.lstSuffixes = self.getRemovableSuffixes()


    def getReporters(self) -> list:
        lstReporterLines = getCleanList("./Raw_Data/Reporters.txt")
        # Remove the Note Field
        lstReporterLines.pop(0)
        lstReporters = []

        for line in lstReporterLines:
            lstReporterToken = str(line).split(";")
            tmpReporter = ReporterAbbreviation()
            tmpReporter.strLongForm = str(lstReporterToken[REPORTER_LONG_NAME_POSITION])
            tmpReporter.strShortForm = str(lstReporterToken[REPORTER_SHORT_NAME_POSITION])
            tmpReporter.bolIsCourtSpecificReporter = distutils.util.strtobool(lstReporterToken[REPORTER_ISCOURTSPECIFIC_POSITION])
            tmpReporter.bolIsStateReporter = distutils.util.strtobool(lstReporterToken[REPORTER_ISSTATEREPORTER_POSITION])
            
            
            lstReporters.append(tmpReporter)
        
        return lstReporters

    def getCourts(self) -> list:
        lstCourtLines = getCleanList("./Raw_Data/Courts.txt")
        # Remove the Note Field
        lstCourtLines.pop(0)

        lstCourts = []

        for line in lstCourtLines:
            tmpCourt = CourtAbbreviation()
            lstCourtTokens = str(line).split(";")
            tmpCourt.bolIsStateCourt = bool(lstCourtTokens[COURT_IS_STATE_COURT_POSTION])
            tmpCourt.strShortForm = str(lstCourtTokens[COURT_SHORT_NAME_POSTION])
            tmpCourt.strLongForm = str(lstCourtTokens[COURT_LONG_NAME_POSTION])
            lstCourts.append(tmpCourt)
        
        return lstCourts

    def getRemovableSuffixes(self) -> list:

        lstSuffixes = getCleanList("./Raw_Data/Suffixes.txt")
        return lstSuffixes

    def getCourtShortName(self, strLongName: str) -> str:
        strSearchedCourtLower = str(strLongName.lower())
        strSearchedCourtLower = strSearchedCourtLower.removeprefix("the ")

        for court in self.lstCourts:
            strTokenCourtLower = str(court.strLongForm).lower()
            if strTokenCourtLower == strSearchedCourtLower:
                return CourtAbbreviation(court).strShortForm
        # print ("COURT NOT FOUND ( " + strLongName + ")")
        return "COURT NOT FOUND ( " + strLongName + ")"

    def getReporterShortName(self, strLongName: str) -> str:

        try:
            strReporterTokens = strLongName.split(" of the ")
            strSuffixElement = strReporterTokens.pop(1)
            strReporterTokens = strSuffixElement.split("beginning")
            strReporter = strReporterTokens.pop(0).strip()
            strReporter = strReporter.removesuffix(",")


            for reporter in self.lstReporters:
                if reporter.strLongForm == strReporter:

                    return Abbreviation(reporter).strShortForm
            # print ("REPORTER NOT FOUND ( " + strLongName + ")")
        except IndexError:
            return "REPORTER INVALID"
        return "REPORTER NOT FOUND ( " + strLongName + ")"

    def getReporterIsStateReporter(self, strLongName: str) -> bool:
        for reporter in self.lstReporters:
            if reporter.strLongForm == strLongName:
                return ReporterAbbreviation(reporter).bolIsStateReporter
        return False

    def getReporterIsCourtReporter(self, strLongName: str) -> bool:
        for reporter in self.lstReporters:
            if reporter.strLongForm == strLongName:
                return ReporterAbbreviation(reporter).bolIsCourtSpecificReporter
        return False


def getCleanList(strFile: str) -> list:
    file = open(strFile, "r")
    lstLines = file.readlines()
    lstNewList = []

    for line in lstLines:
        lstNewList.append(line.strip())
    
    return lstNewList