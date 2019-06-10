# CentryLink Challenge
This API was written using Python and Flask on Windows 10. To run it, first install flask.
```
> pip install Flask
> // or
> py -m pip install Flask
```

## Virtual Environment
Next, in the project folder, we'll want to set up a virtual environment to run the application.
```
> py -m venv venv
```
To set the environment variables on Windows:
```
> set FLASK_ENV=development
> set FLASK_APP=app.py
```
Or on Linux:
```
$ export FLASK_ENV=development
$ export FLASK_APP=app.py
```

## Run it!
Now to run the app:
```
> flask run
```
Note: this opened on port 5000 for me.

## Endpoint
This endpoint was tested using Postman. To get the relevent data, use endpoint:
```
localhost:5000/user/<username>
```

## Extra Challenge
Wasn't able to get this working just yet. So far, only pulling in the repos of the given user. To see progress, use endpoint:
```
localhost:5000/test/user/<username>
```