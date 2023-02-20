DATASET=$1

if [ $DATASET = "faces" ]
then
source scripts/downloaders/download_kaggle_data.sh jessicali9530 celeba-dataset
elif [ $DATASET = "bricks" ]
then
source scripts/downloaders/download_kaggle_data.sh joosthazelzet lego-brick-images 
elif [ $DATASET = "recipes" ]
then
source scripts/downloaders/download_kaggle_data.sh hugodarwood epirecipes
elif [ $DATASET = "flowers" ]
then
source scripts/downloaders/download_kaggle_data.sh nunenuh pytorch-challange-flower-dataset
elif [ $DATASET = "wines" ]
then
source scripts/downloaders/download_kaggle_data.sh zynicide wine-reviews
elif [ $DATASET = "cellosuites" ]
then
source scripts/downloaders/download_bach_cello_data.sh
elif [ $DATASET = "chorales" ]
then
source scripts/downloaders/download_bach_chorale_data.sh
else
echo "Invalid dataset name - please choose from: faces, bricks, recipes, flowers, wines, cellosuites, chorales"
fi



