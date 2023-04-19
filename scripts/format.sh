docker compose exec app black -l 80 .
docker compose exec app flake8 --max-line-length=80 --exclude=./data --ignore=W503,E203,E402
docker compose exec app flake8_nb --max-line-length=80 --exclude=./data --ignore=W503,E203,E402