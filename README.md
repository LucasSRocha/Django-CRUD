# Django-CRUD

This is an API for creating, reading, updating and deleting resources and categories.

---
## REQUIREMENTS
- [docker-compose](https://docs.docker.com/compose/install/)

---

## USAGE
### Run the project
```
$ git clone https://github.com/LucasSRocha/Django-CRUD.git


$ cd Django-CRUD
```
You can build the docker image and then start it (or do it all at once)
```
$ docker-compose build

$ docker-compose up
```
or
```
$ docker-compose up --build
```
#### You can access all images' bashes:

- The project itself: ``` $ docker-compose exec web bash ```


- Postgres:  ``` $ docker-compose exec db bash ```

### Run tests
```
$ cd Django-CRUD


$ docker-compose run web python django_crud/manage.py test core
```

### Get Authentication

```
$ docker-compose run web python django_crud/manage.py createsuperuser
```

With your username and password make a post request to ```/auth/login```

```
$ curl -d "username=admin&password=admin" -X POST http://localhost:8000/auth/login/


{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTcwNDM1NjM5LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.-mQHuiEELlGG6-6GdAjBbHHZo2yLlolE1rXnU_Cv0FE"}
```

Use the token value as your authorization header

```
$ curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTcwNDM1NjM5LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.-mQHuiEELlGG6-6GdAjBbHHZo2yLlolE1rXnU_Cv0FE" -X GET http://localhost:8000/


{"category":"http://localhost:8000/category/","shoes":"http://localhost:8000/shoes/"}
```

### Without authentication
```
$ curl -X GET http://localhost:8000/


{"detail":"Authentication credentials were not provided."}
```

### You can create a Category

By sending a POST request to '/category/' with the *category* data you can create new unique categories.

```
curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTcwNDM1NjM5LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.-mQHuiEELlGG6-6GdAjBbHHZo2yLlolE1rXnU_Cv0FE" -d "category=Calçados" -X POST http://localhost:8000/category/


{"id":3,"category":"Calçados"}

```

You also can:

- list at ```/category/```

- put, patch, delete at ```/category/:id```

### For this project we're focusing on Shoes (Other models may be included later)

Shoes are defined by this atributes:

- price
- size
- color
- shoes_stock
- shoes_bought
- shoe_model
- shoe_brand
- class_category

To create a Shoe object it's necessary to pass this atributes:
- size
- price
- color
- shoe_model
- shoe_stock

```  
$ curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTcwNDM2Njk2LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.Tr6MW5oYxStU4b97Sut7800cCV19TRdj40kyVgN1d3w" -d "size=10&price=10.99&color=black&shoe_model=Ekin&shoe_stock=100" -X POST http://localhost:8000/shoes/

{"id":14,"price":10.99,"size":"10","color":"black","shoes_stock":0,"shoes_bought":0,"shoe_model":"Ekin","shoe_brand":"","class_category":[]}
```

You also can:

- list at ```/shoes/```

- put, patch, delete at ```/shoes/:id```

### And for mass insert you can use /_resource_/csv_import

To get a list of the available resources make a GET request at ```/```

```
$ curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTcwNDM1NjM5LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.-mQHuiEELlGG6-6GdAjBbHHZo2yLlolE1rXnU_Cv0FE" -X GET http://localhost:8000/


{"category":"http://localhost:8000/category/","shoes":"http://localhost:8000/shoes/"}
```
To mass insert categories with a csv file you have to use the following column pattern at the link '/category/csv_import':

```*category*```

To mass insert shoes with a csv file you have to use the following column pattern at the link '/shoes/csv_import':

```*price,discount,size,color,shoes_stock,shoes_bought,shoe_model,shoe_brand,class_category*```

Doing so you'll be able to mass insert shoes and even calculate discounts if you wish so.
