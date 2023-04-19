docker compose exec app bash -c "
mkdir /app/data/bach-chorales/
cd /app/data/bach-chorales/ && 
echo 'Downloading...' && 
curl -LO https://github.com/czhuang/JSB-Chorales-dataset/raw/master/Jsb16thSeparated.npz -s &&
echo '🚀 Done!'
" 
