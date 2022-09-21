# First part
The first part it's about logic tasks in python
## Fizz buzz
Code a program (in python) that displays the numbers from 1 to 100 on the
screen, substituting the multiples of 3 for the word "fizz", the multiples of 5 for
"buzz" and the multiples of both, that is, the multiples of 3 and 5, by the word
"fizz buzz".
## Fibonacci list
In mathematics, the Fibonacci sequence or serie is the following infinite sequence
of natural numbers: 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597 ...
where f (0) = 0, f (1) = 1 and f (n) = f (n-1) + f (n-2).
Code a program (in python) that solves for any number in the Fibonacci series.
## Word counter
Given an input text, Code a program (in python) that displays the number of
repetitions of each word.
Sample text: "Hi how are things? How are you? Are you a developer? I am also a
developer"
## Tests
You can run all the tests with:
```bash
pytest
```
Also can add -v parameter for a more verbose output.

# Backend Knowledge application test
## Rest api with flask
Rest Api created with Flask, to install this project please follow the instructions below.

-First of all create a virtual environment and install required dependencies with:
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
### Use
Once you have your server running you have to setup a new user, you can use the [localhost/signup](http://localhost:5000/signup) link or just enter the [index](http://localhost:5000) and it'll redirect you to the signup page. After that you need to enter to [sign in](http://localhost:5000/signin), and create your first post with postman. The method you should use is <strong>POST</strong> the format of the json is:

```JSON
{
"description": "Description as a String",
"priority": 10,
"status": "Published / Deleted",
"title": "Title as a String",
"user" : 1
}
```
Once you have your first post, you can see it through your navigator signin in at [localhost/signin](http://localhost:5000/signin).
### Swagger

Please note that you can check all the methods included in this rest-api at the link [localhost/swagger](http://localhost:5000/swagger).

#### Notes

The links in this repo only work if you have initiated your project at the default port 5000.