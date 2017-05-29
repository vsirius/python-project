# python-APP
```sh
docker pull siriusgti/python-app
```
```
docker run -p 80:80 --name python-app --link application-db:siriusgti/mysql-db -d -t siriusgti/python-app
```
