<h2 align="center">Jeffrey bezos Products</h2>
<div align="center">
<img src="https://i2.wp.com/www.fb101.com/wp-content/uploads/2019/07/FoodProductTop.jpg?fit=678%2C298&ssl=1" 
     target="_blank" rel="noopener" alt="Products">
</div>

# Project Overview
*Mr Jeff Bezos is going to the moon next year, after crushing every local business book and electrical store, he now wants to crush supermarkets like Tesco whom give it's staff actual toilet breaks.* 
<br>
*Big Jeff would like me to design a frontend product table, that allows users to Create, Read, Update and Delete products backed by a restful API to maximise work efficiency.*

*Remember clock is always ticking.* Efficiency. Efficiency. Efficiency.

## Purpose
As part of my code challenge, I have been tasked to create a front-end table that display products, in which the user can add, edit and delete each product.

## Contents
* [purpose](#Purpose)
* [requirements](#Requirements)
   * [front-end-requirements](#Front-end-requirements)
   * [homepage-requirements](#Homepage-requirements)
   * [Add-or-Edit-View-requirements](#Add-or-Edit-View-requirements)
* [wireframes](#Wireframes)
   * [Homepage-wireframe](#Homepage-wireframes)
   * [Add-or-Edit-wireframe](#Add-or-Edit-wireframes)
* [Schema-Design](#Schema-Design)
* [Technologies](#Technologies)
     * [Languages](#Languages)
     * [Libraries](#Libraries)
* [Testing](#Testing) 
* [Deployment](#Deployment)
     * [Remote Deployment](#Remote-Deployment)
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



## Schema-Design

<div align="center">
<img src="https://github.com/michodgs25/Jeffrey-bezos-Products/blob/main/static/images/product-schema.jpg" 
     target="_blank" rel="noopener" alt="Add or Edit wireframe">
</div>


## Technologies 

* JS hint - https://jshint.com/: Tested my JS code and provided feedback to increase code quality.

* W3S html& css validator - https://validator.w3.org/: Tested both my HTML& CSS code and provided feedback to improve quality.

* Pylint - https://pypi.org/project/pylint/: Used with the IDE terminal typing `pylint app.py` this returns a report of the python code.

* pep8 - http://pep8online.com/: An online python code tester, returns any errors within code inputted.

* mobiReady - https://ready.mobi/: Online app that that test whether the app is mobile ready.

* Google dev tools: found top right corner of the chrome browser, more tool then bottom option. Provided a virtual testing environment.

### Languages

In this project I used *HTML5*, *CSS*, *JAVASCRIPT*, *PYTHON* programming languages.

### Libraries

- Materialize CSS and JS Libraries: 
* https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css 

* https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js

- Python 3.7: https://www.python.org/

- Font Awesome: https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css

- JQuery library: https://jquery.com/ 

## Testing

## Deployment


### Remote-Deployment


## Acknowledgements](#Acknowledgements)
I would like to thank Jeffrey Bezos for providing me with this challenge

Thank you to Clere group for providing me the opportunity to display my skills.

### External-Media
All images were take from Google images advanced search with filter - __"free to use or share"__

Wireframe images were taken from __https://github.com/deltabrot/clere-coding-challenge-api__