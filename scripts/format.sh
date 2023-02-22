docker-compose exec app black -l 120 .
docker-compose exec app flake8 --max-line-length=120 --exclude=./data --ignore=W503,E203,E402
docker-compose exec app flake8_nb --max-line-length=120 --exclude=./data --ignore=W503,E203,E402