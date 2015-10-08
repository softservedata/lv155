#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # no color

printf "Enter directories counters: \n"
read count
if ! [[ "$count" =~ ^[0-9]+$ ]]
then
	printf "${RED}Sorry, integer only${NC}\n"
else
until [ $count -lt 1 ];
do 
printf "Enter directory name: \n"
read dirname

if [ ! -d "$dirname" ]
then
	printf "${GREEN} Directory $dirname doesn't exist.${NC}\n"
	
else
	printf "${RED} Directory $dirname exist ${NC}\n"
fi;
echo counter $count
let count-=1
done
fi

