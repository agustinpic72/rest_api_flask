# Rest api with flask
Rest Api created with Flask, to install this project please follow the instructions below.

-First of all create a virtual environment and install required dependencies i suggest to use:
```bash
pipenv install -r requirements.txt
```
-Then you can run the app.py file with: 
```bash
Python app.py
```
or 
 ```bash
Python3 app.py
```
## Use
Once you have your server running you have to setup a new user, you can use the [localhost/signup](http://localhost:5000/signup) link or just enter the index and it'll redirect you to the signup page. After that you need to create sign in, and then, create your first post with postman. The method you should use is <strong>POST</strong> the format of the json is:

```JSON
{
"description": "Description as a String",
"priority": Integer,
"status": "Published / Deleted",
"title": "Title as a String",
"user" : 1 This is your user id, as Integer
}
```
Once you have your first post, you can see it through your navigator signin in at [localhost/signin](http://localhost:5000/signin).
## Swagger

Please note that you can check all the methods included in this rest-api at the link [localhost/swagger](http://localhost:5000/swagger).

### Notes

The links in this repo only work if you have initiated your project at the default port 5000.