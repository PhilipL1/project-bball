# Basketball App Project 


## Contents
* [Introduction](#introduction) 
  * [Objective](#objective)
  * [Proposal](#proposal)
* [Architecture](#architecture)
  * [Risk Assessment](#risk-assessment)
  * [Trello Board](#trello-board)
  * [Entity Relationship Diagram](#entity-relationship-diagram)
  * [Test Analysis](#analysis-of-testing)
  * [Continuous Integration pipeline](#continuous-integration)
* [Development](#development)
  * [Unit Testing](#unit-testing)
  * [Front-End Design](#front-end)
  * [Integration Testing](#integration-testing)
* [Footer](#footer)

## Introduction

### Objective
The objective provided for this project is as follows:
> To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.
This will allow the trainers to: 
> Objectively assess your capability with the technologies and
concepts you have been taught.
> Assess your development against SFIA.

More specifically, the following is required:
* Functioning CRUD application created in Python
* Functioning front-end to website using Flask
* Trello board or equivalent
* Relational database - must contain at least one one-to-many relationship
* Clear documentation
* Detailed risk assessment
* Automated tests 
* Fully integrated into Github or other VCS

### Proposal
My Flask application is a Basketball Fantasy application where users are able to create a basketball team. Users are able to read the created teams on the home page whilst having access to update, delete and add players to the teams created. 

An outline of how CRUD will be implemented can be seen below.

**Create**:
* Team name 
* Team city 
* Team conference 
* Team rank 

**Read**:
* Read the team that was created 
   * Team name 
   * Team city 
   * Team conference 
   * Team rank 

**Update**:
* Update the team that was created 
   * Team name 
   * Team city 
   * Team conference 
   * Team rank 

**Delete**:
* Delete the team that was created 
   * Team name 
   * Team city 
   * Team conference 
   * Team rank
   * 
**Add players**:
* PLayer name 
* Player position 

## Architecture

### Database Structure
### Entity Relationship Diagram
Pictured below is an entity relationship diagram (ERD) showing the structure of the database. The relationship between these 2 tables is a one to many relationship thus the  foreign key is the player table. As a result, each player can have one team but one team can have many players in the database. 

![ERD image](ADD IMAGE)
<br/><br/>
It was not necessary to create a many to many relationship however if i had enough time i would of created a many to many relationship using an associatation table that breaks into two many to one relationships. As a result, the relationship would of been one player can be on many teams and one team can have many players. The ERD is shown below. 

![ERD image2](ADD IMAGE)
<br/><br/>


## Project Management 
### Trello Board
Trello was used to track the progress of the project (pictured below). You can find the link to this board here:
(ENTER URL)
<br/><br/>
I used Trello board rather than other project management tools such as Jira because it is free to use and user friendly which helps with visualisation of the project so that task can be completed efficiently.  
<br/><br/>
![trello board image](ADD IMAGE)
The elements of the project move left to right from point of conception which is the product backlog to completed work section where the work is finialised. 
* *Product Backlog* 
   A list of essential and non essential requirements set out in the brief in order to maximise the mark scheme. 
* *Sprint backlog*
   All of the incomplete requirements that are expected to be done in the current sprint
* *Sprint: In progress* 
   All of the incomplete requirements that are currently in progress of being completed 
* *Requires Testing* 
   All of the requirements that have been developed but require further tests
* *completed tasks* 
   list of task that has been completed and no longer need editing.    
   
## Risk Assessment
The full risk assessment for this project can be found [here]:
(ADD URL) 

Here is a screenshot at the start of my project:
<br/><br/>
![risk assessment image]( ADD IMAGE)
<br/>
Here is a screenshot at the end of my project:
<br/><br/>
![risk assessment image2]( ADD IMAGE)
<br/>

## Analysis of Testing
This project includes to basic forms of testing which are unit and integration testing. There are other forms of testing that was not used in the project due to the level of complicity of the project and time. The image below shows other test that was not tested in this project. 
<br/>
![image of some out-of-scope forms of testing](ADD IMAGE)
[reference](http://www.qafileshare.com/mcw/deloitte/deloitteselfstudy/PRDTRE.pdf)
<br/>

It would be ideal to have a test- driven approach, however I was not able to have this ideal approach as I was still learning the tools to create the application with a close deadline approaching. If I was going to have a test driven approach to my project I would of created an excel spreadsheet. As test were made, the spreadsheet would be filled. Then the application would have been created. 
The picture below is a template of what my spreadsheet would of looked like and some sections filled in. 
<br/>
![image of testing analysis document](ADD IMAGE)
The document can be viewed [here]  (ENTER URL)


### Continuous Integration pipeline
The picture below is a continuous integration pipeline with associated frameworks and services related to them. This pipeline allows for rapid and simple development-to-deployment by automating the integration process. This means, python code using visual studio code platform on my local machine can be pushed to Github. The new code in the repo will automatically be pushed to Jenkins via webhook so that the code can be built on the cloud virtual machine. From there, unit and integration test are automatically run and reports are produced. The developer can assess the report and refractor the program as required. 
<br/>
--MIGTH REMOVE: A testing environment for the app is also run in debugger mode, allowing for dynamic testing.----

#### Jenkins Script
ADD STEPS

## Development
### Unit Testing
Unit testing is used here by seperating the route functions and testing each function with various scenarios. Each function should return the expected response under each given scenario for the test to be successful. These tests are run automatically after every Git push using Jenkins. Jenkins prints out whether or not the tests were successsful and also gives a coverage report noting the percentage of the application that was tested.


pytest is used to run unit tests on the app. These are designed to assert that if a certain function is run, the output should be a known value. Jenkins produces console outputs (pictured below) that will inform the developer how many tests the code passed and which tests they failed.

Coverage report is also displayed to help the developer understand how much of the code in the app has been successfully tested. Jenkins automatically moves this report to the 'templates' folder so that it can be navigated to in a browser, as shown in the picture below.
## Front-End Design
A functioning front-end website and integrated API's, using Flask was used in the project to create a CRUD website. As seen below:

Home page is where  majority of the functionality takes place. 

Navigating to the create teams page will direct the user to input information regarding their team and submit the information. The inout information will be displayed in the home page with option to update or delete the team. 

Adding players to the team is also an option on the home page where users can click on the add players button which syncrinses with that specific team and they can add players to that particular team. 

