# Running project
In terminal, go into directory with `docker-compose.yml` file and type:
```
docker-compose up
```

# Creating super user
At first, go into docker container
```
docker-compose exec web bash
```

then type:
```
python app/manage.py createsuperuser
```
and follow the instructions.


# Using project
### Swagger
There is Swagger available at url `127.0.0.1:8000`.

Unfortunately, I don't think there is a way to use authentication there (which is needed for signing agreements)
and for views with authentication needed, please use Postman.

### Using authentication
At first, use `/users/api-token-auth/` endpoint. It's response will be something like:
```
{
  "token": "tokenAuthValue123456"
}
```
When using endpoints which require authentication, add following header:
```
Authorization: Token tokenAuthValue123456
```


### Running tests
In docker container type:
```
python app/manage.py test
```

Enjoy :)