<h1>Rest api with flask</h1>
<p>Rest Api created with Flask, to install this project please follow the below instructions.</p>
<p>-First of all create a virtual environment and install required dependencies with 'pipenv install -r requirements.txt'</p>
<p>-Then you can run the app.py file with 'Python app.py' or 'Python3 app.py'</p>
<p>Once you have your server running you have to setup a new user, you can use the localhost/signup link or just enter the index and it'll redirect you to the signup page. After that you need to create sign in, and then create your first post with postman. the format you should use is: 
        {<br>
           "description": "Description as a String",<br>
            "priority": Integer,<br>
            "status": "Published / Deleted",<br>
            "title": "Title as a String",<br>
            "user" : 1 <!-- this is your user id --><br>
        }</p>