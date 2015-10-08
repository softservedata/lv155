echo "Enter DB name: "
read DBNAME
DBEXISTS=$(mysql --batch --skip-column-names -e "SHOW DATABASES LIKE '"$DBNAME"';" | grep "$DBNAME" > /dev/null; echo "$?" )
if [ $DBEXISTS -eq 0 ]; 
then
	echo "A database with name $DBNAME already exists. "
	exit;
else
	echo "A database with name $DBNAME dosn't exist. "
fi
