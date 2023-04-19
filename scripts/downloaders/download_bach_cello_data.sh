docker compose exec app bash -c "
mkdir /app/data/bach-cello/
cd /app/data/bach-cello/ && 
echo 'Downloading...' && 
curl -O http://www.jsbach.net/midi/cs1-1pre.mid -s &&
curl -O http://www.jsbach.net/midi/cs1-2all.mid -s &&
curl -O http://www.jsbach.net/midi/cs1-3cou.mid -s &&
curl -O http://www.jsbach.net/midi/cs1-4sar.mid -s &&
curl -O http://www.jsbach.net/midi/cs1-5men.mid -s &&
curl -O http://www.jsbach.net/midi/cs1-6gig.mid -s &&
curl -O http://www.jsbach.net/midi/cs2-1pre.mid -s &&
curl -O http://www.jsbach.net/midi/cs2-2all.mid -s &&
curl -O http://www.jsbach.net/midi/cs2-3cou.mid -s &&
curl -O http://www.jsbach.net/midi/cs2-4sar.mid -s &&
curl -O http://www.jsbach.net/midi/cs2-5men.mid -s &&
curl -O http://www.jsbach.net/midi/cs2-6gig.mid -s &&
curl -O http://www.jsbach.net/midi/cs3-1pre.mid -s &&
curl -O http://www.jsbach.net/midi/cs3-2all.mid -s &&
curl -O http://www.jsbach.net/midi/cs3-3cou.mid -s &&
curl -O http://www.jsbach.net/midi/cs3-4sar.mid -s &&
curl -O http://www.jsbach.net/midi/cs3-5bou.mid -s &&
curl -O http://www.jsbach.net/midi/cs3-6gig.mid -s &&
curl -O http://www.jsbach.net/midi/cs4-1pre.mid -s &&
curl -O http://www.jsbach.net/midi/cs4-2all.mid -s &&
curl -O http://www.jsbach.net/midi/cs4-3cou.mid -s &&
curl -O http://www.jsbach.net/midi/cs4-4sar.mid -s &&
curl -O http://www.jsbach.net/midi/cs4-5bou.mid -s &&
curl -O http://www.jsbach.net/midi/cs4-6gig.mid -s &&
curl -O http://www.jsbach.net/midi/cs5-1pre.mid -s &&
curl -O http://www.jsbach.net/midi/cs5-2all.mid -s &&
curl -O http://www.jsbach.net/midi/cs5-3cou.mid -s &&
curl -O http://www.jsbach.net/midi/cs5-4sar.mid -s &&
curl -O http://www.jsbach.net/midi/cs5-5gav.mid -s &&
curl -O http://www.jsbach.net/midi/cs5-6gig.mid -s &&
curl -O http://www.jsbach.net/midi/cs6-1pre.mid -s &&
curl -O http://www.jsbach.net/midi/cs6-2all.mid -s &&
curl -O http://www.jsbach.net/midi/cs6-3cou.mid -s &&
curl -O http://www.jsbach.net/midi/cs6-4sar.mid -s &&
curl -O http://www.jsbach.net/midi/cs6-5gav.mid -s &&
curl -O http://www.jsbach.net/midi/cs6-6gig.mid -s &&
echo '🚀 Done!'
" 