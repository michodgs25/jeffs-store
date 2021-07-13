<h2 align="center">Jeffs Store</h2>
<div align="center">
<img src="https://i2.wp.com/www.fb101.com/wp-content/uploads/2019/07/FoodProductTop.jpg?fit=678%2C298&ssl=1" 
     target="_blank" rel="noopener" alt="Products">
</div>

# Project Overview
*Mr Jeff Bezos is going to the moon next year, after crushing every local business book and electrical store, he now wants to crush supermarkets like Tesco whom give it's staff actual toilet breaks.* 
<br>
*Big Jeff would like me to design a frontend product table, that allows users to Create, Read, Update and Delete products.*

*Remember clock is always ticking.* Efficiency. Efficiency. Efficiency.

## Purpose
As part of my code challenge, I have been tasked to create a front-end table that display products, in which the user can add, edit and delete a product.

## Contents
* [purpose](#Purpose)
* [requirements](#Requirements)
   * [front-end-requirements](#Front-end-requirements)
   * [homepage-requirements](#Homepage-requirements)
   * [Add-or-Edit-View-requirements](#Add-or-Edit-View-requirements)
* [wireframes](#Wireframes)
   * [Homepage-wireframe](#Homepage-wireframes)
   * [Add-or-Edit-wireframe](#Add-or-Edit-wireframes)
* [Database](#Database)
* [Heroku](#Heroku)
* [Technologies](#Technologies)
     * [Languages](#Languages)
     * [Libraries](#Libraries)
* [Deployment](#Deployment)
     * [Heroku](#Heroku)
* [Acknowledgements](#Acknowledgements)
     * [External-Media](#External-Media)

## Requirements
Each product will have an: 'ID',  'Name',  'Price',  'Currency'.

A user should be able to: 

* Create a product
* Read product
* Update product
* Delete a product

This is called the CRUD method.

### Front-end requirements

#### Homepage requirements

- This page should show a button to add new products

- This page should display a table of existing products.

- Clicking the "Add product" button should either take the user to a new page, or present a pop up dialog window showing the "Product Editor" form.

- The table itself should have columns to show the Id, Name, Price, and Actions (buttons to edit and delete existing products), the price column values should show a concatenation of a product's "price" and "currency" (e.g. "9.99 USD"

- The Actions column should contain two buttons on each row, one to edit the product, and one to delete it. 

- Clicking the edit product button should show similar behaviour to adding a new product, however the form should already be populated with the data from the selected product, and upon saving will update the product.

- Clicking the delete button should delete the product and also refresh the table to reflect this. 


#### Add or Edit View requirements

- This page/pop up dialog should show a form with three input fields, one for "Name", "Price", and "Currency", as well as buttons to either cancel or save the state of the form.

- When creating a new product, all fields should be blank. When updating an existing product, the fields should be populated with the data of the product being modified.

- Upon pressing save, a product will be either created or updated, then the user should be taken back to the table view.

- When pressing cancel, the user will simply be taken back to the table view.

## Wireframes

<h2 align="center">Homepage wireframe</h2>

<div align="center">
<img src="https://user-images.githubusercontent.com/28734598/124751825-fce7e180-df1e-11eb-90a9-479c24c58aeb.png" 
     target="_blank" rel="noopener" alt="Homepage wireframe">
</div>

<h2 align="center">Add or Edit wireframes</h2>

<div align="center">
<img src="https://user-images.githubusercontent.com/28734598/124751836-007b6880-df1f-11eb-9735-e98707dadc8a.png" 
     target="_blank" rel="noopener" alt="Add or Edit wireframe">
</div>


## Database
I chose MongoDB as my chosen database, because MongoDB provides high performance data persistence. In particular,

Support for embedded data models reduces I/O activity on database system.
Indexes support faster queries and can include keys from embedded documents and arrays.
Rich Query Language
MongoDB supports a rich query language to support read and write operations (CRUD) see more at: https://docs.mongodb.com/manual/introduction/


## Heroku 

I hosted the product table on Heroku as it is simple to set up for small scale projects such as this. See more at - https://devcenter.heroku.com/


## Technologies 

* W3S html& css validator - https://validator.w3.org/: Tested both my HTML& CSS code and provided feedback to improve quality.

* Google dev tools: found top right corner of the chrome browser, more tool then bottom option. Provided a virtual testing environment.

### Languages

In this project I used *HTML5*, *CSS*, *PYTHON* and *JINJA* programming languages.

### Libraries

- Flask 
* https://flask.palletsprojects.com/en/2.0.x/

- MongoDb
* https://www.mongodb.com/

- Materialize CSS and JS Libraries: 
* https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css 

* https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js

- Python 3.7: https://www.python.org/

- Font Awesome: https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css

- JQuery library: https://jquery.com/ 

## Deployment

#### Requirements 
You will need the following tools installed on your system:

Python 3 - https://www.python.org/downloads/
An IDE such as Visual Studio, gitpod, Code, or like this project gitpod
An account at MongoDB Atlas - https:https://github.com/michodgs25/Sprint//www.mongodb.com/
Git - https://gist.github.com/derhuerst/1b15ff4652a867391f03


I personally used github on my local machine to develop the site using Python 3.7.3 and deployed to Heroku via Github.

1. To download or clone the site to your local machine you will need to go to my repo [here.](https://github.com/michodgs25/jeffs-store) and see deployment steps in https://help.github.com/en/articles/cloning-a-repository

2. Before you download or clone the site you will need to ensure you have Python 3.7 or above installed.

3. Once you have Python installed, created a virtual environment as appropriate to your chosen IDE and os.

4. Run the requirements.txt file as appropriate to your IDE to install the relevant required packages dependencies for the project into your virtual environment.

5. Create a MONGODB account, Create a cluster and follow the mongodb steps to connecting with your application.

6. I created an env.py file(make sure its added to gitignore) add the following:
  - **IP**: `0.0.0.0`
  - **PORT**: `8000`
  - **MONGO_URI**: `string to connect with MongoDB`
  - **SECRET_KEY**: `your chosen secret key`

7. Add these to the top of your app.py file:
import os
from flask import (
    Flask, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

8. Run the app.py file as appropriate to your chosen environment and os.

9. You should now be able to view the site on your localhost on port 8000.


## Heroku

#### Instructions
To deploy this app to Heroku you need to follow the steps below:

- Create a **requirements.txt** file so that Heroku can install all the dependencies required to run the app.
  `pip freeze > requirements.txt`

- Create a **Procfile** with the command:
  `echo web: python app.py > Procfile`

- In this step, you have to create a free account on the [Heroku website](https://signup.heroku.com/).
-  Login to the account, click on new and then create a new app. In the following screen, you need to give a name and choose the Europe region.
-  In the menu access the **Deploy** option, after that click on Connect to Github. Just below provide the information from the app's repository on GitHub and select the option Enable Automatic Deploy.
- On the Dashboard of the APP, click on Settings and then click on the option **Reveal config Vars**.
- Now you need to add the following variables to **Reveal config Vars**:
  - **IP**: `0.0.0.0`
  - **PORT**: `8000`
  - **MONGO_URI**: `string to connect with MongoDB`
  - **SECRET_KEY**: `your chosen secret key`
- You are now ready to access the deployed app on Heroku.


## Acknowledgements

Thank you to Clere group for providing me the opportunity to display my skills.

### External-Media
All images were take from Google images advanced search with filter - __"free to use or share"__

Wireframe images were taken from __https://github.com/deltabrot/clere-coding-challenge-api__
