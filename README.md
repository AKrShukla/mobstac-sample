

Clone This Project (Make Sure You Have Git Installed)
```
git remote add origin https://github.com/AKrShukla/mobstac-sample.git
```
Install Dependencies 

```
pip install -r requirements.txt
```

Set Database (Make Sure you are in directory same as manage.py)
```
python manage.py makemigrations
python manage.py migrate
```
Create SuperUser 
```
python manage.py createsuperuser
```
Run Server
```
python manage.py runserver
```
After all these steps , you can start testing and developing this project. 

#### That's it! Happy Coding!
