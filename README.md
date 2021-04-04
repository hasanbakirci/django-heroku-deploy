> python manage.py runserver

localhost:8000/admin
localhost:8000/api/urunler
localhost:8000/api/siparisler

Terminalde:

env sanal ortamına giriş için: 

> source ./env/scripts/activate

sanal ortamda kurulu paketler için: 

> pip freeze > requirements.txt

> git init
> 
> git add .
> 
> git commit -m "mesaj"
> 
> heroku login
> 
> heroku create isim
> 
> git push heroku master
> 
> heroku run python manage.py migrate

ilk yükleme ise superuser oluşturmak için: 

> heroku run python manage.py createsuperuser

- Yüklerken Collectstatic hatası verirse :

>  heroku config:set DISABLE_COLLECTSTATIC=1

 yazıp tekrar 

> git push heroku master