#script to send 20 data inputs to InfluxDB server

url='http://localhost:8086/write?db=test'


#echo $PATH

for i in {1..20}
do
	p=$((RANDOM%11+25))
	q=$((RANDOM%11+25))
	query1="foobar,eggs=raw value=${q}"
	query2="foobar,bacon=streaky value=${p}"
	echo $q
	curl -i -XPOST ${url} --data-binary "${query1}"
	sleep 1s
	echo $p
	curl -i -XPOST ${url} --data-binary "${query2}"
	sleep 10s
done
