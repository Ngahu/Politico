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



@version_1.route("/parties/<int:party_id>",methods=['GET'])
def get_specific_party(party_id):
    """
    Description:Retrieve a specific political party by its id.\n
    """

    if party_id is not None:

        #Check if party exists
        party_exists = PartyModel.check_party_exists(party_id)

        if party_exists:
            response = PartyModel.get_party_by_id(party_id)
            result = Serializer.serialize(response,200)
            return result
        
        else:
            result = Serializer.serialize(
                'Party {} is not available'.format(party_id), 404, 'Not Found'
            )
        return result
    
    else:
        error = Serializer.serialize(
            'Party id cannot be none', 405, 'Not Allowed'
        )
    
    return error



@version_1.route("/parties/<int:party_id>",methods=['PATCH'])
def party_update(party_id):
    """
    Description:Update an existing party
    """
    raw_updates = request.get_json()

    updates = Validator.json_has_data(raw_updates)

    try:
        party = PartyModel.check_party_exists(party_id)

        if party:
            response = PartyModel.update_party(party, **updates)
            result = Serializer.serialize(response, 200)
            return result
        
        return make_response(jsonify({
            'message':'Party Does not exist',
            'status': 'Not Found'
        }),404)

    except Exception:
        return Serializer.serialize(updates, 500)
        