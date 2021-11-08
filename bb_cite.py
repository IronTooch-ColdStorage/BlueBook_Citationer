
import Constants
from CitationStyles.alternate_short_form_cite import alt_short_form_case_citation
from CitationStyles.full_cite import full_case_citation


print("Select what type of citation to create: ")
print("1: Full citation")
print("2: Embedded citation (end of line)")
print("3: Embedded citation (middle of line)")
print("4: Short form citation")
print("5: Alternate Short Form Citation")

citation_type = input("")

print("Citation type is: " + citation_type)

if (int(citation_type) == Constants.FULL_CITATION):
    print("What type of citation is this?")
    print("1: Published Case")
    print("2: Pending and Unreported Case")
    citation_source = "1" #input("")
    #print("Full Cite")
    full_case_citation()
elif (int(citation_type) == Constants.EMBEDDED_END):
    print("Embedded End")
elif (int(citation_type) == Constants.EMBEDDED_MIDDLE):
    print ("Embedded Middle")
elif (int(citation_type) == Constants.SHORT_FORM):
    print("Short Form")
elif (int(citation_type) == Constants.ALTERNATE_SHORT_FORM):
    print ("Alternate Short Form")
    alt_short_form_case_citation()




# Make table of courts
# Make table of abbreviations
# Make table of states
