''' defines the base test classes '''

import unittest

#local imports 
from app import create_app

from app.api.v1.models.office_models import OfficeModel



class TestBaseClass(unittest.TestCase):
    """
    Description:Create a base test class
    """
    test_office_db = [{
        "created_on":"Saturday, 09. February 2019 08:55AM",
        "name": "President of the Republic of Kenya",
        "office_id": 1,
        "office_type":"legislative"
    }] 

    test_party_db = [{
        "created_on": "Wednesday, 06. February 2019 10:39PM",
        "logo_url": "link-link",
        "party_hq": "Nairobi",
        "party_id": 1,
        "party_name": "Wiper",
        "party_official": "John Doe"
    }]

    def setUp(self):
        """ Sets up testing client """
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        self.demo_office = dict(
            office_type = 'legistrative',
            office_name = 'The Governor, County Government of Nairobi'
        )

        self.invalid_party = dict(
            party_name = 'The Test Party',
            logo_url = '',
            party_official='A Human',
            party_hq='Party',

        )
        self.demo_party = dict(
            party_name = 'Jubilee Party',
            party_official = 'A person',
            party_hq='Narok',
            logo_url = "https://unsplash.com/photos/fI8yIH-rV5I"
        )

        self.bad_request = dict(
            office_type = "___",
            office_name = "Governor Embu"
        )
        