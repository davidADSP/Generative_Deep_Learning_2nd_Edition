MODEL=$1
DATASET=$2
echo "Attaching Tensorboard to ./notebooks/$MODEL/$DATASET/logs/"
docker-compose exec -e CHAPTER=$CHAPTER -e MODEL=$MODEL  -e DATASET=$DATASET app bash -c 'tensorboard --logdir "./notebooks/$MODEL/$DATASET/logs" --host 0.0.0.0 --port "$TENSORBOARD_PORT"'