'''This module serializes passed responses'''


#app imports
from flask import jsonify,make_response



class Serializer:
    '''Contains a method that serializes data passed to it into json form.'''

    @classmethod
    def serialize(cls,response,status_code,message=200):
        """
        Description:Serialize the output to json format.\n
        """
        result = make_response(
            jsonify({
                'status':status_code,
                'data':response
            }),status_code
        )
        return result
        
