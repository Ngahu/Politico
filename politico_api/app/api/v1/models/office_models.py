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

    

    def create_political_office(self):
        """
        Description:Create a political office.\n
        """
        try:
            new_office = dict(
                office_id = self.office_id,
                office_name = self.office_name,
                office_type = self.office_type,
                created_on = self.created_on
            )
            OFFICE_DB.append(new_office)

            return new_office
        
        except Exception as error:
            raise Exception(error)
    

    @classmethod 
    def get_all_offices(cls):
        """
        Description:Return a list of all political parties.\n
        """
        return OFFICE_DB

    @classmethod
    def check_office_exists(cls,office_id):
        """
        Description:Check if a specific political office does exist.\n
        Required Args: office_id.\n
        """
        for office in  OFFICE_DB:
            if office['office_id'] = office_id:
                return office
        return None
    
    @classmethod
    def get_office_by_id(cls,office_id):
        """
        Description:Return a specific political office given the office id if it does exist.\n
        """
        the_office = OfficeModel.check_office_exists(office_id)

        return the_office
    

    @classmethod 
    def update_office(cls,office,*args, **kwargs):
        """
        Description:Updates a political office with the user defined information.\n
        """
        for key, value in kwargs.items():
            office[key] = value
        
        return OFFICE_DB
    
    @classmethod
    def delete_office(cls,office):
        """
        Description:Delete a political office if it exists.\n
        """
        OFFICE_DB.remove(office)
        
        return 'Successfully deleted political office.'



        
