#script to send 20 data inputs to InfluxDB server

url='http://localhost:8086/write?db=parameters'


#echo $PATH

for i in {1..70}
do
	p = $(bc <<< "1+${i}/10")
	q=$(bc <<< "1+${i}/10")
	query1="voltage,source=top value=${p}"
	query2="current,source=top value=${q}"
#	echo $q
	curl -i -XPOST ${url} --data-binary "${query1}"
	echo $p
	curl -i -XPOST ${url} --data-binary "${query2}"
	p=$((1+i/70))
	q=$((1-i/70))

	query1="voltage,source=middle value=${p}"
	query2="current,source=middle value=${q}"
	curl -i -XPOST ${url} --data-binary "${query1}"
	curl -i -XPOST ${url} --data-binary "${query2}"

	p=$((1+i/35))
	q=$((1-i/35))

	query1="voltage,source=bottom value=${p}"
	query2="current,source=bottom value=${q}"
	curl -i -XPOST ${url} --data-binary "${query1}"
	curl -i -XPOST ${url} --data-binary "${query2}"

	sleep 1
done
