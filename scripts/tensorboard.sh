EXPERIMENT_NAME=$1
echo "Attaching Tensorboard to ./notebooks/$EXPERIMENT_NAME/logs/"
docker-compose exec -e EXPERIMENT_NAME=$EXPERIMENT_NAME app bash -c 'tensorboard --logdir "./notebooks/$EXPERIMENT_NAME/logs/" --host 0.0.0.0 --port "$TENSORBOARD_PORT"'