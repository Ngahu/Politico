'''This module tests version one of the api'''

#third party imports
import json
import unittest


#local import 
from app.tests.v1 import TestBaseClass



class TestApiEndPoints(TestBaseClass):
    """
    Description:This class handles methods to test version 1 of the api
    """
    def test_create_political_office(self):
        """
        Description:Test the creation of a single political office.\n
        """
        response = self.client.post(
            '/api/v1/create-political-office/',
            data = json.dumps(self.demo_office),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)        



    def test_get_all_offices(self):
        """
        Description:Test the retrieval of all offices.\n
        """
        response = self.client.get("/api/v1/all-political-offices/")
        self.assertEqual(response.status_code, 200)

    
    def test_get_specific_office(self):
        """
        Description: Test the retrieval of a single political office.\n
        """
        response = self.client.get("/api/v1/offices/1")
        self.assertEqual(response.status_code, 200)

    
    def test_office_not_found(self):
        """
        Description:Tests the response on a non-existant resource
        """
        response = self.client.get('api/v1/offices/10')
        self.assertEqual(response.status_code, 404)


    # parties
    def test_create_party(self):
        """
        Description:Test the creation of a single political party.\n
        """
        response = self.client.post(
            '/api/v1/create-political-party/',
            data=json.dumps(self.demo_party),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
    

    def test_get_all_parties(self):
        """
        Description:Test the retrieval of all parties.\n
        """
        response = self.client.get('/api/v1/all-political-parties/')
        self.assertEqual(response.status_code, 200)

    
    # def test_get_specific_party(self):
    #     """
    #     Description:Test the retrieval of a single specific party.\n
    #     """
    #     response = self.client.get('api/v1/parties/1/detail')
    #     self.assertEqual(response.status_code, 200)
    

    def test_party_not_found(self):
        """
        Description:Tests the response on a non-existant party.\n
        """
        response = self.client.get('api/v1/parties/10')
        self.assertEqual(response.status_code, 404)

    
    # def test_edit_non_existing_party(self):
    #     """ 
    #     Description:Tests the edit of a non-existant party  
    #     """

    #     response = self.client.put('api/v1/parties/101/update_party')
    #     self.assertEqual(response.status_code, 404)

    
    def test_delete_party(self):
        """
        Description:Test the deleting of an existing party.\n
        """
        response = self.client.delete('api/v1/parties/1/delete')
        self.assertEqual(response.status_code, 200)
    

    # def test_delete_non_existing_party(self):
    #     """
    #     Description:Tst the deleting of a non existing party.\n
    #     """
    #     response = self.client.delete('api/v1/parties/10/delete')
    #     self.assertEqual(response.status_code, 404)
    




