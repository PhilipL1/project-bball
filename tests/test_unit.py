import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db 
from application.models import Teams

class TestBase(TestCase):# Create the base class
    def create_app(self):# Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True,
            WTF_CSRF_ENABLED= False  #diabled security for testing 
            )
        return app

#Will be called before every test
    def setUp(self): # Set up the database schema(table).   
        db.create_all()# Create table
        test_team= Teams(description= "Test the flask app")# create a new class >>same<<
        db.session.add(test_team)# save users to database
        db.session.commit()

#Will be called after every test
    def tearDown(self):# once each test is completed it will remove everything from the database and drop all schema(table)
        db.session.remove()
        db.drop_all()
    
#test to check that each route will get a status code 
# Write a test class for testing that the home page loads but we are not able to run a get request for delete and update routes.
#going to the url directly 
class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
   
    def test_create_get(self):
        response = self.client.get(url_for('create'))
        self.assertEqual(response.status_code, 200)
   
    def test_update_get(self):
        response = self.client.get(url_for('update', id=1), follow_redirects= True)
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete', id=1), follow_redirects= True)
        self.assertEqual(response.status_code, 200)
################################
class TestRead(TestBase):
    def test_read_team(self):
        response= self.client.get(url_for("home")) #make a get requisition one of the groups. Read the team in the "home" page 
        self.assertIn(b"Test the flask app", response.data) # same as test_task above (>>same<<) b= meanscompare text to webpage 

class TestCreate(TestBase):
    def test_create_team(self):
        response = self.client.post(url_for("create"), # the create route when makinhg the team we need to create a post request.
        data= dict(description = "Create a new team", va= nenkfn, ), # data that we are sending with the post requisition  
        follow_redirects= True
        )
        self.assertIn(b"Create a new team",  response.data) #check if the create..team shows up. only shows if it is added to the data base., then you get the actual data itself
        self.assertIn(b"nenkfn",  response.data) 

class TestUpdate(TestBase):
    def test_update_team(self):
        response = self.client.post(url_for("update", id=1), #id will be 1 in the database
        data = dict(description = "Update a team"), #send info
        follow_redirects= True
        )
        self.assertIn(b"Update a team", response.data)

class TestDelete(TestBase):
    def test_delete_team(self):
        response = self.client.get(url_for("delete", id=1), #id will be 1 in the database
        follow_redirects= True
        )
        self.assertNotIn(b"Test the flask app", response.data)