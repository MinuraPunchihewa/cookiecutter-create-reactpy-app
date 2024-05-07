install:
	pip install -r requirements.txt

run:
	backend="{{ cookiecutter.backend }}"; \
	if [ "$$backend" = "flask" ]; then \
		gunicorn main:app --reload; \
	elif [ "$$backend" = "fastapi" ] || [ "$$backend" = "starlette" ]; then \
		uvicorn main:app --reload; \
	else \
		echo "Backend not supported!"; \
		exit 1; \
	fi