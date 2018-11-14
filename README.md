[![Build Status](https://travis-ci.com/queenfiona/SendITv3.svg?branch=ft-parcels-put-API-161716449)](https://travis-ci.com/queenfiona/SendITv3)
[![Coverage Status](https://coveralls.io/repos/github/queenfiona/SendITv3/badge.svg?branch=ft-parcels-put-API-161716449)](https://coveralls.io/github/queenfiona/SendITv3?branch=ft-parcels-put-API-161716449)
[![Maintainability](https://api.codeclimate.com/v1/badges/00bf7a16c12b7b3edaaa/maintainability)](https://codeclimate.com/github/queenfiona/SendITv3/maintainability)
# SendITv3
SendIT is a courier service that helps users deliver parcels to different destinations provides courier quotes based on weight categories.
# Start develop branch
Start challenge two base branch story
# Start setup API development environment branch
Start setup API development environment branch story
# Start create post API for parcel delivery orders story
Create a feature branch for post API and start create post API for parcel delivery orders story
# Start fetch all parcel delivery orders story
Create a feature branch for fetching all parcel delivery orders
# Start fetch a specific parcel delivery order by its parcel id story
Create a feature branch for fetching a specific parcel delivery order and start associated story
# Start fetch all parcel delivery orders of a specific user story
Create a feature branch for fetching all parcel delivery orders of a specific user and start associated story
# Start cancel a parcel delivery order story
Create a feature branch for cancelling a parcel delivery order and start associated story

# Manual to test application
# In terminal:
	git clone 
	cd into the cloned repo
	git checkout ft-parcels-put-API-161716449
# To run:
# Heroku
	In terminal type: heroku local
	Open postman to run API endpoints to:
		1. Make a parcel delivery order
			POST https://send-it-v1.herokuapp.com/api/v1/parcels
		2. Get all parcel delivery orders
			GET https://send-it-v1.herokuapp.com/api/v1/parcels
		3. Get a specific parcel delivery order by parcel id
			GET https://send-it-v1.herokuapp.com/api/v1/parcels/1
		4. Get orders associated to a user id
			GET https://send-it-v1.herokuapp.com/api/v1/users/1/parcels
		5. Change status of a parcel delivery order
			PUT https://send-it-v1.herokuapp.com/api/v1/parcels/1/cancel
# Flask
	In terminal type:
		export FLASK_APP=run.py
		export FLASK_DEBUG=True
		flask run
	Open postman to run API endpoints to:
		1. Make a parcel delivery order
			POST http://127.0.0.1:5000/api/v1/parcels
		2. Get all parcel delivery orders
			GET http://127.0.0.1:5000/api/v1/parcels
		3. Get a specific parcel delivery order by parcel id
			GET http://127.0.0.1:5000/api/v1/parcels/1
		4. Get orders associated to a user id
			GET http://127.0.0.1:5000/api/v1/users/1/parcels
		5. Change status of a parcel delivery order
			PUT http://127.0.0.1:5000/api/v1/parcels/1/cancel







