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




