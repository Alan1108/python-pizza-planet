SHELL=/bin/bash
venv-activate:
	source venv/bin/activate

install-requirements:
	pip3 install -r requirements.txt

migrations: install-requirements
	python3 manage.py db init
	python3 manage.py db migrate
	python3 manage.py db upgrade

run:
	python3 manage.py run

tests: 
	python3 manage.py test

db_drop:
	python3 manage.py db downgrade base
	python3 manage.py db upgrade

db_fill: db_drop
	python3 manage.py seed run --root app/seeds 

coverage_file:
	pip install pytest-coverage
	pytest --cov=app --cov-report xml 
