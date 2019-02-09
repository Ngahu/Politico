'''This module handles all the views related to political parties'''


#standard imports
import json


#third party imports
from flask  import request,jsonify,make_response

#local imports
from app.utils.serializer import Serializer
from app.validators.validators import Validator
from app.api.v1.models.office_models import OfficeModel


#import the blueprint
from app.api.v1 import version_1





@version_1.route("/all-political-offices/",methods=["GET"])
def get_all_political_offices():
    """
    Description:Sends a get request to retrieve all registered political parties.\n
    """
    response = OfficeModel.get_all_offices()
    result = Serializer.serialize(response,200)
    return result





@version_1.route("/create-political-office/",methods=['POST'])
def create_office():
    """
    Description:Create a single political office.\n
    """
    the_office = request.get_json()

    r_office = Validator.json_has_payload(the_office)

    try:
        office = Validator.field_exists('office', **r_office)
        office_name = office['office_name']
        office_type = office['office_type']

        office_model = OfficeModel(office_name, office_type)
        response  =office_model.create_political_office()
        result = Serializer.serialize(response, 201, 'Created')
        return result
    

    except Exception as error:
        return Serializer.serialize(
                "Missing {} field".format(error.args[0]), 400)





@version_1.route("/offices/<int:office_id>",methods=['GET'])
def get_specific_office(office_id):
    """
    Description:Retrieve a specific political office by its id.\n
    """
    if office_id is not None:

        #check if office exists
        office_exists= OfficeModel.check_office_exists(office_id)

        if office_exists:
            response = OfficeModel.get_office_by_id(office_id)
            result = Serializer.serialize(response,200)
            return result
        
        else:
            result = Serializer.serialize(
                'Office {} is not available'.format(office_id), 404, 'Not Found'
            )
        
        return result
    
    else:
        error = Serializer.serialize(
            'Office id cannot be none', 405, 'Not Allowed'
        )
    
    return error