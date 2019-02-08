'''This module handles all the views related to political parties'''

#standard imports
import json


#third party imports
from flask  import request,jsonify,make_response


#local imports
from app.api.v1.models.parties_models import PartyModel
from app.utils.serializer import Serializer
from app.validators.validators import Validator

#import the blueprint
from app.api.v1 import version_1


@version_1.route("/all-political-parties/",methods=["GET"])
def get_all_parties():
    """
    Description:Sends a get request to retrieve all registered political parties.\n
    """
    response = PartyModel.get_all_parties()
    result = Serializer.serialize(response,200)
    return result





@version_1.route("/create-political-party/",methods=['POST'])
def create_political_party():
    """
    Description:Create a political party.\n
    """
    the_party = request.get_json()

    party = Validator.json_has_payload(the_party)
    
    try:
        valid_party = Validator.field_exists('party',**party)
        party_model = PartyModel(
            valid_party['party_name'],
            valid_party['party_official'],
            valid_party['party_hq'],
            valid_party['logo_url']
        )
        response = party_model.create_political_party()
        result = Serializer.serialize(response,201,'Created')
        return result
    
    except Exception as error:
        return Serializer.serialize(
            "Missing {} field".format(error.args[0]), 400
        )


