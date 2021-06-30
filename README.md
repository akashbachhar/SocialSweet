
# Social Sweet

This is a social media website with following features a registered user can do.


## Features

- Sign Up and Log in
- Create Posts
- Edit and Delete a Particular Post
- Like and Share the Posts
- Making Comments on the Posts
- Delete a Comment
- Make a User Profile with relevant Informations Like Profile Picture, About, Gender and Relationship Status.
- Edit the User Profile

  
## Screenshots

<img src="./sweet/static/UI/1.png" alt="UI"/>
<img src="./sweet/static/UI/2.png" alt="UI" width="50%"/>
<img src="./sweet/static/UI/3.png" alt="UI" width="50%"/>

  
## Tech Stack

**Client:** HTML, CSS, Bootstrap, JavaScript, jQuery

**Server:** Python, Django

**Database:** PostgreSQL 

  
## Run Locally

Create a new directory 
```bash
  mkdir SocialSweet
```

Create a virtual environment

```bash
  sudo apt-get install python3-venv
  python3 -m venv env
```
Clone the project

```bash
  git clone https://github.com/akashbachhar/SocailSweet.git
```

Activate the virtual environment

**Linux/Mac:**

```bash
  source env/bin/activate
```

**Windows:**

```bash
  .\Scripts\activate
```

Install the requirements

```bash
  cd SocialSweet
  pip install -r requirements.txt
```

Run the migrations 

```bash
  python manage.py makemigrations
  python manage.py migrate
```

Run the Development Server 

```bash
  python manage.py runserver
```
Head to server http://127.0.0.1:8000

  