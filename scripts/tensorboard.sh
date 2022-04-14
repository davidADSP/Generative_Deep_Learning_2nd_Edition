CHAPTER=$1
MODEL=$2
DATASET=$3
echo "Attaching Tensorboard to ./notebooks/$CHAPTER/$MODEL/$DATASET/logs/"
docker-compose exec -e CHAPTER=$CHAPTER -e MODEL=$MODEL  -e DATASET=$DATASET app bash -c 'tensorboard --logdir "./notebooks/$CHAPTER/$MODEL/$DATASET/" --host 0.0.0.0 --port "$TENSORBOARD_PORT"'