'''This module contains the party related data'''


#import time
import datetime


#the parties database.
PARTY_DB = []


class PartyModel:
    """
    Description:Define methods  that handle all action regarding political parties.\n
    model Fields:
    Party_name
    party_official
    party_hq
    logo_url
    created_on
    """
    def __init__(self,party_name, party_official, party_hq, logo_url):
        """Initializes the instance  variables"""

        self.party_id = len(PARTY_DB) + 1
        self.party_name = party_name
        self.party_hq = party_hq
        self.party_official = party_official
        self.logo_url = logo_url
        self.created_on = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")

    

    def create_political_party(self):
        """
        Description:Create a political party.\n
        """

        try:
            new_party = dict(
                party_id = self.party_id,
                party_name = self.party_name,
                party_hq = self.party_hq,
                party_official = self.party_official,
                logo_url = self.logo_url,
                created_on = self.created_on
            )
            PARTY_DB.append(new_party)

            return new_party
        
        except Exception as error:
            raise Exception(error)
    

    @classmethod
    def get_all_parties(cls):
        """
        Description:Return all political parties.\n
        """
        return  PARTY_DB
    
    @classmethod
    def check_party_exists(cls,party_id):
        """ 
        Description:Checks if a specific party exists.\n
        Required Args: party_id.\n
        """
        for party in PARTY_DB:
            if  party['party_id'] == party_id:
                return party
        
        return None
    

    @classmethod
    def get_party_by_id(cls,party_id):
        """
        Description:Return a specific party given the party id.\n
        """
        the_party = PartyModel.check_party_exists(party_id)
        
        return the_party

    @classmethod
    def update_party(cls,party,**kwargs):
        """ Updates party with user defined information """
        for key, value in kwargs.items():
            party[key] = value

        return PARTY_DB

    
    @classmethod
    def delete_party(cls,party):
        """
        Description:Delete a political party if it exists.\n
        """
        PARTY_DB.remove(party)
        return 'Successfuly deleted party'
        


