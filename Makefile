install:
	pip install -r requirements.txt

run:
	gunicorn main:app --reload