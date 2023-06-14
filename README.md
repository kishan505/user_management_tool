# User Management Tool 

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/kishan505/user_management_tool.git
$ cd user_management_tool
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `python3`.

Once `pip` has finished downloading the dependencies:

then after create superuser for access admin pannel

```sh
(venv)$ python manage.py createsuperuser
```

then after run project

```sh
(venv)$ python manage.py runserver
```

after project run, import user_management_postman_collection.json in POSTMAN

## API Reference

#### User sign up

```http
  POST /sign_up
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. enter username   |
| `email` | `string` | **Required**. enter valid email address   |
| `password` | `string` | **Required**. enter password must be 6 character |
| `confirm_password` | `string` | **Required**. confirm_password same as password  |



#### User login

```http
  POST /login
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. enter your username   |
| `password` | `string` | **Required**. enter your password   |


#### Create User Profile

```http
  POST /create_user_profile
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `user_id` | `integer` | **Required**. enter user_id for get user  |
| `profile_photo` | `file` | upload image from your computer   |
| `location` | `string` | enter your location   |
| `designation` | `string` | enter your designation   |



for open admin pannal navigate to  `http://127.0.0.1:8000/admin`  Url.
