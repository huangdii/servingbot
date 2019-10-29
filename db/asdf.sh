
for  i in $(ls | grep .svo.db)
do
NAME=${i%.svo*}
echo $NAME
cp $i $NAME.db
done 

