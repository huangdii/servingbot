for i in $(ls)
do
if [[ $i == *".bak" ]]; then
	echo "$i is .bak file.. skipping!"
else
	mv $i $i.bak
fi
done

