'''Define  political office model and its methods. '''

import datetime


OFFICE_DB = []



class OfficeModel:
    """
    Description:Handle all the operations related to  political offices.\n
    """
    def __init__(self,office_name, office_type):
        """
        Description:Define the instance variables.\n
        """
        self.office_id = len(OFFICE_DB)+1
        self.office_name = office_name
        self.office_type = office_type
        self.created_on = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
        