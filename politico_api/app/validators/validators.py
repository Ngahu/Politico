'''This module contains classes that  handle data validation.'''
import re
import json

from app.utils.serializer import Serializer




class Validator:
    """
    Description:Handle data validation in different endpoints.\n
    """

    @classmethod
    def json_has_payload(cls,json_dict):
        """
        Description:Validate if a passed json object is empty or contains data.\n
        """
        if not json_dict:
            return 'You cannot submit an empty payload.'
        
        return  json_dict
    

    @classmethod
    def is_valid_word(cls,user_input):
        """
        Description:Validates a passed args which is the user input to make sure its a String.\n
        """
        if isinstance(user_input,str):
            return True
        return False

    


    @classmethod 
    def field_exists(cls,entity,**payload):
        """
        Description:Validate based on entity whether a field exists or not.\n
        """
        if entity == 'office':
            for key, value in data.items():
                if key not in ('office_name', 'office_type'):
                    return 'Missing {} field'.format(key)
                elif Validator.is_valid_word(value) is False:
                    return 'Missing value for the {} field'.format(key)
            
            return payload
        
        elif entity == 'party':
            for key, value in data.items():
                if key not in ('party_name', 'party_official', 'party_hq', 'logo_url'):
                    return 'Missing {} field'.format(key)
                
                elif Validator.is_valid_word(value) is False:
                    return 'Missing value for the {} field'.format(key)
            
            return payload
    


    @classmethod
    def validate_email(cls,user_input):
        """
        Description:Validate whether a users email is valid or not.\n
        """
        is_valid = re.search(r'^\w+@\w+.\w+$', user_input)
        if is_valid:
            return user_input
        return False
        

