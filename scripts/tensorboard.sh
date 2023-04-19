CHAPTER=$1
EXAMPLE=$2
echo "Attaching Tensorboard to ./notebooks/$CHAPTER/$EXAMPLE/logs/"
docker compose exec -e CHAPTER=$CHAPTER -e EXAMPLE=$EXAMPLE app bash -c 'tensorboard --logdir "./notebooks/$CHAPTER/$EXAMPLE/logs" --host 0.0.0.0 --port $TENSORBOARD_PORT'