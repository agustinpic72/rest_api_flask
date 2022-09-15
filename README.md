<h1>Rest api with flask</h1>
<p>Rest Api created with Flask, to install this project please follow the instructions below.</p>
<p>-First of all create a virtual environment and install required dependencies i suggest to use 'pipenv install -r requirements.txt'</p>
<p>-Then you can run the app.py file with 'Python app.py' or 'Python3 app.py'</p>
<p>Once you have your server running you have to setup a new user, you can use the <strong>localhost/signup</strong> link or just enter the index and it'll redirect you to the signup page. After that you need to create sign in, and then create your first post with postman. the method you should use is <strong>POST</strong> format of the json is:<br> 
        {<br>
           "description": "Description as a String",<br>
            "priority": Integer,<br>
            "status": "Published / Deleted",<br>
            "title": "Title as a String",<br>
            "user" : 1 This is your user id, as Integer<br>
        }</p>
<p>Once you have your first post, you can see it through your navigator signin in at <strong>localhost/signin</strong>.</p>
<h1>Swagger</h1>
<p>Please note that you can check all the methods included in this rest-api at the link <strong>localhost/swagger</strong></p>