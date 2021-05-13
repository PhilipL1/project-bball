# Basketball App Project 

## My approach 
might delete this section 
working process 

## Architecture
### Database Structure
Pictured below is an entity relationship diagram (ERD) showing the structure of the database. The relationship between these 2 tables is a one to many relationship as the  foreign key is the player table. As a result, each player can have one team but one team can have many players in the database. 

### CI Pipeline
The picture below is a continuous integration pipeline with associated frameworks and services related to them. This pipeline allows for rapid and simple development-to-deployment by automating the integration process. This means, python code using visual studio code platform on my local machine can be pushed to Github. The new code will automatically be pushed to Jenkins via webhook to so that it can be autatically installed on the cloud virtual machone. From there, tests are automatically run and reports are produced.
-- A testing environment for the app is also run in debugger mode, allowing for dynamic testing.----

## Project Management 
Trello was used to track the progress of the project (pictured below). You can find the link to this board here:

A Trello board was used to tack my project. The elements of the project move left to right from point of conception which is the product backlog to completed work section where the work is finialised and completed. 
* *Product Backlog* 
   A list of essential and non essential requirements set out in the brief in order to maximise the mark scheme. 
* *Sprint backlog*
   list of elements that will be next in line to do.
* *Sprint 1* 
   list of tasks that i am currently doing 
* *completed tasks* 
   list of task that has be completed and no longer need editing.    
   
## Risk Assessment
The risk assessment for this project can be found in full here: 


Here is a screenshot at the start of my project:

Here is a screenshot at the end of my project:

## Testing
pytest is used to run unit tests on the app. These are designed to assert that if a certain function is run, the output should be a known value. Jenkins produces console outputs (pictured below) that will inform the developer how many tests the code passed and which tests they failed.

Coverage report is also displayed to help the developer understand how much of the code in the app has been successfully tested. Jenkins automatically moves this report to the 'templates' folder so that it can be navigated to in a browser, as shown in the picture below.

## Front-End Design
A functioning front-end website and integrated API's, using Flask was used in the project to create a CRUD website. As seen below:

Home page is where  majority of the functionality takes place. 

Navigating to the create teams page will direct the user to input information regarding their team and submit the information. The inout information will be displayed in the home page with option to update or delete the team. 

Adding players to the team is also an option on the home page where users can click on the add players button which syncrinses with that specific team and they can add players to that particular team. 

