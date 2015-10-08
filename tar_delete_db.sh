#echo -n "Enter the MySQL root passwd:"
#read -s rootpw
echo -n "Enter database name what you want to delete: "
read dbname 
echo -n "Enter DB username: "
read dbuser
#echo -n "Ented DB user passwd:"
#read dbpw

mysqladmin -u $dbuser -p drop $dbname
 
