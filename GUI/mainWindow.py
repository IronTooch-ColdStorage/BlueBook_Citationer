import tkinter as tk
from tkinter.constants import N, W
from tkinter import *
from tkinter import ttk
import os
import sys
import inspect



currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
classesdir = parentdir + "\\Classes"
citationdir = parentdir + "\\CitationStyles"

sys.path.insert(0, str(classesdir))
sys.path.insert(0, str(citationdir))
from HelperFunctions import *  
from Case import *
from full_cite import full_case_citation
from full_cite import citationClauseMiddle
from short_form_cite import short_form_case_citation


CONSTANT_IMAGE_SIZE = 756
CONSTANT_BUTTONHEIGHT = 30
CONSTANT_BUTTONPADDING = 30

CITE_TYPE = [Constants.CITATION_TYPE_FULLTEXT_STR, 
                Constants.CITATION_TYPE_EMBEDDED_END_STR, 
                Constants.CITATION_TYPE_EMBEDDED_MIDDLE_STR,
                Constants.CITATION_TYPE_SHORT_FORM_STR,
                Constants.CITATION_TYPE_ALT_SHORTFORM_STR]

CASE_TYPE = ["Published Case", 
                "Pending and Unreported Case"]

TK_COLUMN_COUNT = 4

# https://www.educba.com/tkinter-widgets/

myCase = Case()

class MainWindow():

    controls = {}
    myCase = Case()

    def makeLabelAndTextbox(self, tkRoot: tk.Tk, strLabelName: str, strLabelText: str, strEntryName: str, strValueName: str, intRow: int):
        self.controls[strLabelName] = tk.Label(tkRoot, text=strLabelText, name=strLabelName, anchor=W)
        self.controls[strLabelName].grid(row=intRow, column=0, sticky=tk.W + tk.E + tk.S + tk.N)
        self.controls[strValueName] = StringVar()
        self.controls[strEntryName] = tk.Entry(tkRoot, textvariable=self.controls[strValueName], name=strValueName)
        self.controls[strEntryName].grid(row=intRow, column=1, sticky=tk.W + tk.E + tk.S + tk.N)      

    def makeBusinessAndAbbreviateOptions(self, tkRoot: tk.Tk,strIsBusinessName: str, strBusinessLabelText: str, strIsBusinessValue:str,strAbbreviateName: str, strAbbreviateLabelText: str, strAbbreviateValue:str, intRow: int ):
        self.controls[strIsBusinessValue] = IntVar()
        self.controls[strIsBusinessName] = Checkbutton(tkRoot, text = strBusinessLabelText, variable= self.controls[strIsBusinessValue], onvalue = 1, offvalue = 0, anchor=W)
        self.controls[strIsBusinessName].grid(row=intRow, column=2)

        self.controls[strAbbreviateValue] = IntVar()
        self.controls[strAbbreviateName] = Checkbutton(tkRoot, text = strAbbreviateLabelText, variable= self.controls[strAbbreviateValue], onvalue = 1, offvalue = 0, anchor=W)
        self.controls[strAbbreviateName].grid(row=intRow, column=3)

    def DrawMainWindow(self, tkRoot: tk.Tk):

        self.strCourtName = StringVar()

        tkRoot.title("Blue Book Citation Tool by Steve Tuccio")
        tkRoot.geometry("600x600")
        tkRoot.rowconfigure(2,minsize=50, weight=1)
         
        tkRoot.columnconfigure(1,weight=1)

        
        
        self.lblHeader = tk.Label(tkRoot, text='Blue Book Citation Tool', name="lblHeader", anchor=N)
        self.lblHeader.grid(row=0, column=0, sticky=tk.W + tk.E + tk.S + tk.N, columnspan=TK_COLUMN_COUNT)
        self.lblHeader2 = tk.Label(tkRoot, text='by Steven Tuccio', name="lblHeader2", anchor=N)
        self.lblHeader2.grid(row=(HelperFunctions.getTkRow(self.lblHeader) + 1), column=0, sticky=tk.W + tk.E + tk.S + tk.N, columnspan=4)

        self.cbxCiteType = ttk.Combobox(tkRoot, values = CITE_TYPE)
        self.cbxCiteType.set("Select a cite style:")
        self.cbxCiteType.grid(row=(HelperFunctions.getTkRow(self.lblHeader2) + 2), column=0, sticky=tk.W + tk.E + tk.S + tk.N, columnspan=4)
        self.cbxCiteType.set("Full Text Citation")  

        self.cbxCaseType = ttk.Combobox(tkRoot, values = CASE_TYPE)
        self.cbxCaseType.set("Select a case type:")
        self.cbxCaseType.grid(row=(HelperFunctions.getTkRow(self.cbxCiteType) + 1), column=0, sticky=tk.W + tk.E + tk.S + tk.N, columnspan=4)
        self.cbxCaseType.set("Published Case")

        self.makeLabelAndTextbox(tkRoot=tkRoot, 
                                 strLabelName="lblFirstPartyName", 
                                 strLabelText='Enter first party name:', 
                                 strEntryName="txtFirstPartyEntry", 
                                 strValueName="strFirstPartyName", 
                                 intRow=(HelperFunctions.getTkRow(self.cbxCaseType) + 2))
  
        self.makeBusinessAndAbbreviateOptions(  tkRoot=tkRoot,
                                                strBusinessLabelText="Is a business",
                                                strIsBusinessName="chkFirstPartyBusiness",
                                                strIsBusinessValue="intIsFirstPartyBusiness",
                                                strAbbreviateLabelText="Abbreviate?",
                                                strAbbreviateName="chkFirstPartyAbbreviate",
                                                strAbbreviateValue="intAbbreviateFirstParty",
                                                intRow=(HelperFunctions.getTkRow(self.controls["lblFirstPartyName"])))

        self.makeLabelAndTextbox(tkRoot=tkRoot, 
                                 strLabelName="lblSecondPartyName", 
                                 strLabelText='Enter second party name:', 
                                 strEntryName="txtSecondPartyEntry", 
                                 strValueName="strSecondPartyName", 
                                 intRow=(HelperFunctions.getTkRow(self.controls["lblFirstPartyName"]) + 1))
  
        self.makeBusinessAndAbbreviateOptions(  tkRoot=tkRoot,
                                                strBusinessLabelText="Is a business",
                                                strIsBusinessName="chkSecondPartyBusiness",
                                                strIsBusinessValue="intIsSecondPartyBusiness",
                                                strAbbreviateLabelText="Abbreviate?",
                                                strAbbreviateName="chkSecondPartyAbbreviate",
                                                strAbbreviateValue="intAbbreviateSecondParty",
                                                intRow=(HelperFunctions.getTkRow(self.controls["lblSecondPartyName"])))

        self.makeLabelAndTextbox(tkRoot=tkRoot, 
                                strLabelName="lblCourtName", 
                                strLabelText='Enter Court name:', 
                                strEntryName="txtCourtEntry", 
                                strValueName="strCourtName", 
                                intRow=(HelperFunctions.getTkRow(self.controls["lblSecondPartyName"]) + 1))

        self.makeLabelAndTextbox(tkRoot=tkRoot, 
                        strLabelName="lblCaseLocation", 
                        strLabelText='Where is the case found?', 
                        strEntryName="txtCourtLocation", 
                        strValueName="strCourtLocation", 
                        intRow=(HelperFunctions.getTkRow(self.controls["lblCourtName"]) + 1))

        self.makeLabelAndTextbox(tkRoot=tkRoot, 
                        strLabelName="lblDecidedDate", 
                        strLabelText='When was the case decided?', 
                        strEntryName="txtDecidedDate", 
                        strValueName="strDecidedDate", 
                        intRow=(HelperFunctions.getTkRow(self.controls["lblCaseLocation"]) + 1))

        self.makeLabelAndTextbox(tkRoot=tkRoot, 
                        strLabelName="lblPinCite", 
                        strLabelText='Where is the pin cite to?', 
                        strEntryName="txtPinCite", 
                        strValueName="strPinCite", 
                        intRow=(HelperFunctions.getTkRow(self.controls["lblDecidedDate"]) + 1))


        #self.lblDebug = tk.Label(tkRoot, text='My Debug Text', name="lblDebug", anchor=S)
        #self.lblDebug.grid(row=(HelperFunctions.getTkRow(self.controls["lblPinCite"]) + 1), column=1, sticky=tk.W + tk.E + tk.S + tk.N, columnspan=3)
        # gs = tkRoot.grid_size()
        # print (gs[1])



        self.controls["strCitation"] = StringVar()
        self.controls["txtCitation"] = tk.Entry(tkRoot, textvariable=self.controls["strCitation"], name="txtCitation")
        self.controls["txtCitation"].grid(row=(HelperFunctions.getTkRow(self.controls["lblPinCite"]) + 1), column=0, sticky=tk.W + tk.E + tk.S + tk.N, columnspan=4)


        for child in tkRoot.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

    def ProcessUpdates(self, tkRoot: tk.Tk):
	
        
        bolFirstPartyIsBusiness = bool(self.controls["intIsFirstPartyBusiness"].get())
        
        
        #print("Update processed")

        strCiteSelection = str(self.cbxCiteType.get())

        strFirstParty = self.controls["txtFirstPartyEntry"].get()
        strSecondParty = self.controls["txtSecondPartyEntry"].get()
        strCourt = self.controls["txtCourtEntry"].get()
        strLocation = self.controls["txtCourtLocation"].get()
        strDecidedDate = self.controls["txtDecidedDate"].get()
        strPinCite = self.controls["txtPinCite"].get()
        
        myCase.strFirstPartyComplete = strFirstParty
        myCase.strSecondPartyComplete = strSecondParty
        myCase.strCourt = strCourt
        myCase.strCaseLocation = strLocation
        myCase.strDateDecidedDate = strDecidedDate
        myCase.strPinLocation = strPinCite

        

        if strCiteSelection == Constants.CITATION_TYPE_FULLTEXT_STR:
            
            strCitation = full_case_citation(myCase)

        elif strCiteSelection == Constants.CITATION_TYPE_EMBEDDED_MIDDLE_STR:

            strCitation = citationClauseMiddle(myCase)

        elif strCiteSelection == Constants.CITATION_TYPE_SHORT_FORM_STR:

            strCitation = short_form_case_citation(myCase)

        strCitationTextbox = str(self.controls["txtCitation"].get())

        if (strCitation != strCitationTextbox):
            self.controls["txtCitation"].delete(0,END)
            self.controls["txtCitation"].insert (0, strCitation)
            

        


