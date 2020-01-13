sudo apt-get install libssl-dev

mkdir ~/tz_volume

docker run --name tzproject2 -v ~/tz_volume:/var/lib/mysql \
-p 3307:3306 -e MYSQL_USER=a -e MYSQL_PASSWORD=a -e MYSQL_ROOT_PASSWORD=a \
-e MYSQL_DATABASE=a mysql:latest