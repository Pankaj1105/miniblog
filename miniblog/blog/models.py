from django.db import models

# 13] Create your models here.
class Post(models.Model):
 title = models.CharField(max_length=150)
 desc = models.TextField() #we can put timming author name any thing here

 #we have to post blog so the blog needs one title and descrption so we are making the table.and the table is made in model.py

 #now we have to genrate  the model in SQl queryes so run two commmnds
# python manage.py makemigrations 
# for making table in backend we run command
#  python manage.py migrate here default table will also create. and our table will also create

#14] for registering our model we have to go to admin.py

#make super user  python manage.py createsuperuser