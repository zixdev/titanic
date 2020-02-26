

test:
	docker-compose run web sh -c "python manage.py test"

install:
	cp .env.example .env
	PIPENV_VENV_IN_PROJECT=1 pipenv install --dev
	docker-compose build

up:
	docker-compose up
build:
	docker-compose build

reinstall:
	@make destroy
	@make install
stop:
	docker-compose stop
restart:
	docker-compose restart
down:
	docker-compose down
destroy:
	docker-compose down --rmi all --volumes
ps:
	docker-compose ps

clean-docker:
	docker-compose ps --all
	docker-compose kill $(docker-compose ps -q)
	docker-compose rm $(docker-compose ps -a -q)


