USER=$1
DATASET=$2

docker compose exec app bash -c "cd /app/data/ && kaggle datasets download -d $USER/$DATASET && echo 'Unzipping...' && unzip -q -o /app/data/$DATASET.zip -d /app/data/$DATASET && rm /app/data/$DATASET.zip && echo '🚀 Done!'"

