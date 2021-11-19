
from Abbreviation import Abbreviation


class CourtAbbreviation(Abbreviation):

    bolIsStateCourt = False

    def __init__(self, orig=None):
        if orig is None:
            self.non_copy_constructor()
        else:
            self.copy_constructor(orig)


    def non_copy_constructor(self):
        pass

    def copy_constructor(self, orig):
        self.strShortForm = orig.strShortForm
        self.strLongForm = orig.strLongForm
        self.bolIsStateCourt = orig.bolIsStateCourt
