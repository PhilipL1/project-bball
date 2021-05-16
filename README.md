# Basketball App Project 

## Contents
* [Introduction](#introduction) 
  * [Objective](#objective)
  * [Proposal](#proposal)
* [Architecture](#architecture)
  * [Risk Assessment](#risk-assessment)
  * [Project Management](#trello-board)
  * [Database Structure](#entity-relationship-diagram)
  * [Test Analysis](#analysis-of-testing)
  * [Continuous Integration pipeline](#continuous-integration)
* [Development](#development)
  * [Unit Testing](#unit-testing)
  * [Front-End Design](#front-end)
* [Footer](#footer)

## Introduction

### Objective
The objective provided for this project is as follows:
> To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.
<br/>
This will allow the trainers to:
>* Objectively assess candidates capability with the technologies and concepts you have been taught.
<br/>
>* Assess your development against SFIA.

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
My Flask application is a Basketball Fantasy application where users are able to create their own basketball teams. Users are able to read the created teams on the home page whilst having access to update, delete and add players to the teams created. 

An outline of how CRUD will be implemented can be seen below.

**Create**:
* Re-direct the end-user to a page where they can create a team 
   * Team name 
   * Team city 
   * Team conference 
   * Team rank 

**Read**:
* Read the different teams on the home page
   * Team name 
   * Team city 
   * Team conference 
   * Team rank 

**Update**:
* A button to update the team that was created 
   * Team name 
   * Team city 
   * Team conference 
   * Team rank 

**Delete**:
* A button to delete the team that was created 
   * Team name 
   * Team city 
   * Team conference 
   * Team rank
   
**Add players**:
* Button to add players to teams 
   * Player name 
   * Player position 
<br/>

# Architecture
## Risk Assessment
My detailed Risk Assessment can be seen below, outlining the major and minor risks associated with this project.
<br/>
Here is a screenshot of my risk assessment at the start of my project:
<br/>

![risk assessment image](https://i.imgur.com/vYA3mmn.png)
<br/><br/>
Below is a screenshot of additional risks that where added at the end of my project when the risks became clear:
<br/>

![risk assessment image2](https://i.imgur.com/aM8dZDf.png)
<br/>
The full risk assessment for this project can be found [here](https://docs.google.com/spreadsheets/d/1j92ZZFjaw2ThyvHosCYimrIyu2FGiy_rgDWGJiYk2zA/edit?usp=sharing). 
<br/>

## Project Management 
### Trello Board
Trello was used to track the progress of the project (pictured below). You can find the link to this board [here](https://trello.com/b/4UYzCR2H). I used Trello board rather than other project management tools such as Jira because it is free to use and user friendly which helps with visualisation of the project so that task can be completed efficiently.  
<br/>

![After - trello board image](https://i.imgur.com/6vIvGiq.png)![](https://i.imgur.com/JiCgcf5.png)
<br/><br/>
The elements of the project move left to right from point of conception which is the product backlog to completed work section where the work is finialised. 
* *Product Backlog* 
   * Moscow Prioritisation: Prioritising workflow so project can be completed efficiently.
   * Product resources: files that i need for the project to be successful 
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
<br/>

## Database Structure
### Entity Relationship Diagram
Pictured below is an entity relationship diagram (ERD) showing the structure of the database. The relationship between these 2 tables is a one to many relationship thus the  foreign key is in the player table. As a result, a team can have many players but a player can have ONLY have one team in the database. 
<br/>

![ERD image 1](https://i.imgur.com/8rIjm4P.png)
<br/><br/>
It was not a priority to create a many to many relationship however if I had enough time I would of created a many to many relationship using an associatation table that breaks into two many to one relationships. As a result, the relationship would of been a player can be on many teams and a team can have many players. The ERD is shown below. 
<br/>

![ERD image 2](https://i.imgur.com/zDCwcN2.png)
<br/>

## Analysis of Testing
This project includes basic forms of testings which are unit and integration testing. There are other forms of testing that was not used in the project due to the level of complicity of the project and time. The image below shows other test that was not tested in this project. 
<br/>

![image of some out-of-scope forms of testing](https://i.imgur.com/RSqnyl9.png)
<br/>
[reference](http://www.qafileshare.com/mcw/deloitte/deloitteselfstudy/PRDTRE.pdf)
<br/>

### Continuous Integration pipeline
The picture below is a continuous integration pipeline with associated frameworks and services related to them. This pipeline allows for rapid and simple development-to-deployment by automating the integration process. This means, python code using visual studio code platform on my local machine can be pushed to Github. The new code in the repo will automatically be pushed to Jenkins via webhook so that the code can be built on the cloud virtual machine. From there, unit and integration test are automatically run and reports are produced. The developer can assess the report and refractor the program as required. 
<br/>

![ci pipeline](https://i.imgur.com/bDoWIRq.png)

#### Jenkins Script
The build script can be broken into these stages, shown below.  
<br/>
**1.** Installation of the virtual environment

```
sudo apt update 
sudo apt install chromium-chromedriver -y
sudo apt-get install python3-venv

sudo apt install python3 python3-pip python3-venv -y 
python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt
```
<br/>
**2.** Unit and integration testing

```
python3 -m pytest --junitxml=junit/test-results.xml --cov=application --cov-report=xml --cov-report=html --cov-report term-missing
```
<br/>
**3.** Run the application 

```
python3 create.py
python3 app.py
```
<br/>

## Development
### Unit Testing
Unit testing is used here by seperating the route functions and testing each function with various scenarios. Each function should return the expected response under each given scenario for the test to be successful. These tests are run automatically after every Git push using Jenkins. Jenkins prints out whether or not the tests were successsful. 
<br/> 
A coverage report is also displayed  noting the percentage of the application that was tested. This information helps the developer understand how much of the code in the app has been successfully tested. 
<br/>
If any of the unit testing fails, the entire Jenkins build is marked as a fail. However, this project had a 100% coverage indicating efficiency as all the lines in my code was fully tested and there were no unnecessary syntax in my code. 
<br/>

![Picture of Coverage report 1](https://i.imgur.com/ya8qO3S.png)
<br/>
![Picture of Coverage report 2](https://i.imgur.com/8xbmgAD.png)
<br/>
![Picture of Coverage report 3](https://i.imgur.com/e3bIizj.png)
<br/>

## Front-End Design
A functioning front-end website and integrated API's, using Flask was used in the project to create a CRUD website.
<br/>
When navigating to the home page (/home) or to the URL with no specified path, the user is given a list of current entries or a blank page waiting for teams to be created. 
<br/>
At the top of the page is a navigation bar (defined in a base layout template, and therefore available on every page). One of the links directs the user to the home page and the other to a team creation page.
<br/>

![home page image](https://i.imgur.com/nNxYIdu.png)

When the user navigates to the creation page (/create) a team entry is immediately created in the database. The database for the entry is then updated every time the user edits and submits a field.
<br/>

![creation page](https://i.imgur.com/lstOWLS.png)

Once a field is submitted the user will be re-directed to the home page where all the relevant information can be viewd.

An update, delete and add player button is located directly under each team. These buttons are associated to each team so each function can perform accordingly for that specific team. 
<br/>

![created a team page](https://i.imgur.com/xG0hBqg.png)
<br/>

## Footer
### Future Improvements
* Using Integration testing to test the app as a whole, by thr selenium approach would be ideal. Using selenium will stimulate a user navigating the site (by clicking on elements in each page) and filling in forms as the testing specifies, and then my tests also check the database for the expected data. The test will be automated using jenkins. If any of the integration testing fails, the entire Jenkins build is marked as a fail.
* As mentioned in the original proposal, having a many to many relationship database will allow more freedom for the end- user as the same player can be used for different teams. Thus, application will be more fun and closer to a fantasy basketball app. 
* Test-driven development: It would of been ideal to have a test- driven approach, however this was not possible as I was still learning the tools to create the application with a close deadline approaching. If I was going to have a test driven approach to my project I would of created an excel spreadsheet. As test were made, the spreadsheet would be filled. Then the application would have been created. 

The picture below is a template of what my spreadsheet would of looked like; with some few boxes filled in as an example. 
<br/>

![image of testing analysis document](https://i.imgur.com/iFr82ee.png)
<br/>
The document can be viewed [here](https://docs.google.com/spreadsheets/d/1G0hngrY3RG9x3Idi1l68PvQ4eNlrKRW-xB_Yy0FTvkU/edit?usp=sharing)
<br/><br/>

### Author
Philip Lartey

### Acknowledgements
* [Harry Volker](https://github.com/htr-volker)
* [Oliver Nichols](https://github.com/OliverNichols)








