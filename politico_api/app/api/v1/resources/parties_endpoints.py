'''This module handles all the views related to political parties'''

#standard imports
import json


#third party imports
from flask  import request,jsonify,make_response


#local imports
from app.api.v1.models.parties_models import PartyModel
from app.utils.serializer import Serializer

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



