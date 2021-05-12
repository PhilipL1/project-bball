from os import name
import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db 
from application.models import Teams, Players

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
        test_team= Teams(name = "Lakers", 
        city = "LA", 
        conference = "West",
        rank = 1
        )
        test_player = Players(pl_name= "Kevin", pl_position = "SF")
        test_team.players.append(test_player)
        db.session.add(test_team)# save users to database
        db.session.add(test_player)
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
    
    def test_player_get(self):
        response = self.client.get(url_for('player', id=1))
        self.assertEqual(response.status_code, 200)
   
    def test_update_get(self):
        response = self.client.get(url_for('update', id=1))
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete', id=1), follow_redirects= True)
        self.assertEqual(response.status_code, 200)
    
################################
class TestRead(TestBase):
    def test_read_team(self):
        response= self.client.get(url_for("home"))
        self.assertIn(b"Lakers", response.data)  
        self.assertIn(b"LA", response.data) 
        self.assertIn(b"West", response.data) 
        
       
class TestCreate(TestBase):
    def test_create_team(self):
        response = self.client.post(url_for("create"), # the create route when making the team we need to create a post request.
        data= dict(form_name = 'Knicks',
        form_city = 'New York', 
        form_conference = 'East', 
        form_rank = 2), # data that we are sending with the post requisition  
        follow_redirects= True
        )
        self.assertIn(b"Knicks", response.data) 
        self.assertIn(b"New York", response.data) 
        self.assertIn(b"East", response.data) 
         

class TestPlayer(TestBase):
    def test_player_team(self):
        response = self.client.post(url_for("player", id =1), #id will be 1 in the database
        data= dict(form_name = 'Lebron James', form_position = 'SF'), 
        follow_redirects= True
        )
        self.assertIn(b'Lebron James', response.data)
        self.assertIn(b'SF', response.data)

class TestUpdate(TestBase):
    def test_update_team(self):
        response = self.client.post(url_for("update", id=1), 
        data= dict(form_name = 'Nets',
        form_city = 'Brooklyn', 
        form_conference = 'West', 
        form_rank = 3),
        follow_redirects= True
        )
        self.assertIn(b'Nets', response.data)
        self.assertIn(b'Brooklyn', response.data)
        self.assertIn(b'West', response.data)
        

class TestDelete(TestBase):
    def test_delete_team(self):
        response = self.client.get(url_for("delete", id=1), #id will be 1 in the database
        follow_redirects= True
        )
        self.assertNotIn(b'Lakers', response.data)
        self.assertNotIn(b'LA', response.data)
        self.assertNotIn(b'West', response.data)
        