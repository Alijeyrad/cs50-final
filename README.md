# CS50x Final Project
This is my final project for Cs50x web development with Python and JavaScript.
# Psych Help
Psych Help is a web application providing the serice of psychological assessment. Using this web application you can take tests See the results and then send the results to a professional to have them interpreted and get their recommendations and advice.
### Distinctiveness and Complexity
This project is not defined as a social networking project as it is not meant to be used to share your personal ideas, beliefs or daily routines. It only provides a service and all transactions are strictly professional.
It is also not a simple e-commerce application because what is purchased is a service provided by a mental health professional. The app is meant to facilitate the process of psychological assessment and help people have easy access to professional evaluation, diagnosis and treatment.
The logic behind the main website and control panel is very similar to that of a social networking website where users can follow other users, but the single page application providing the assessment itself can in no way be characterized as neither a social network nor an e-commerce app.
As I am a student of clinical psychology myself, I have a motivation to facilitate the delivery of psychological assessment to anyone who needs this kind of help.
# Technologies used
- Python 3.10
- Django 3.8.2
- Vanilla JavaScript
- [W3.CSS](https://www.w3schools.com/w3css/default.asp) (CSS Framework)
- SQLite 3
- MongoDB 5

### JavaScript libraries
- [react 18.1](https://reactjs.org/) (create react app)
- [axios](https://axios-http.com/docs/intro) 
- [easytimer.js](https://albert-gonzalez.github.io/easytimer.js/) and [easytimer-react-hook](https://www.npmjs.com/package/easytimer-react-hook)

# How to get started
It's recommended to use python 3.8 or higher to run the app.
To download the required python libraries you need to move to the project directory and use pip:
`cd final_project`
`pip install requirements.txt`

Before running the app you need to make the proper migrations:
`python3 manage.py makemigrations`
and then:
`python3 manage.py migrate`

Also make sure you have a running instance of MongoDB on on your local host at [mongodb://127.0.0.1:27017/](mongodb://127.0.0.1:27017/). You can configure this in *`utils.py`* in the root directory where the connection to MongoDB is defined. You can download and install MongoDB from [here](https://www.mongodb.com/docs/v5.0/installation/) if it's not already installed on your system.

The single page application is made with [create react app](https://create-react-app.dev/) but you don't need to run any `npm` command to run it. This part is already made using `npm build` and the build files are served using Django. [Here](https://github.com/Alijeyrad/raect-neo-test) is the repository containing the create react app source code.

To run the app use: `python3 manage.py runserver`

# File Structure
##### *`final_project`*
The main django project in the root directory. It includes project files like *`settings.py`*, or *`urls.py`* which defines the routes to our Django apps.

##### *`home`*
Our first Django app creating the main website containing links to other apps. This app includes on model in *`models.py`* called `Contact`. This model saves messagaes coming from users in the database. *`views.py`* includes two views for serving the *`index.html`* and for saving incoming messages in database.

##### *`media`*
Django uses this directory to save app media like profile images. The directory is defined in *`final_project/settings.py`* like so:
```
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

##### *`panel`*
Our second Django app which includes all the main functionality.
*`models.py`* includes five models: `User` for keeping all the user information, `Doctor` for keeping track of doctors and their specialty, `Follow` to save info about users following each other, `Comment` and `Star` for saving comments and ratings.
*`views.py`* includes all the main logic for the panel, tests, profiles, user authentication, settings, and all API routes like Follow and Rate.
Also I have creates my own [Custom template tags ](https://docs.djangoproject.com/en/3.2/howto/custom-template-tags/) in *`templatetags`* folder. Django template tags allow me to define complex logic for creating templates (in this case shhowing star ratings of each doctor in the page) and reuse them everywhere with just one line of code like: `{% show_stars doctor %}`. The html files for these templates are kept in *`templates/panel/mytemplatetags/`*.

##### *`static`*
Includes all the static files for each app in different folders for img, css and js files.

##### *`templates`*
Includes all the html files for each app.
Our *`test_neo`* folder here includes the build folder created by create react app using `npm run build`.

##### *`test_neo`*
Our third Django app which is a single page application made with create react app. It is the app responsible for giving the Five Factor Personality test and sending the results back to the server.
The test is created using scales from [ipip.ori.org](https://ipip.ori.org/). [Here](https://ipip.ori.org/newPermission.htm) is the permission to use the scales. **Notice** that the results are not to be taken seriously as they are only practice test results.
I use MongoDB to store the results because it's a NoSQL Document based database and is suitable for storing test results which may contain many (up to 600) fields.

##### *`utils.py`*
Includes the MongoDB instance and the PyMongo driver which is used to connect to the database.
