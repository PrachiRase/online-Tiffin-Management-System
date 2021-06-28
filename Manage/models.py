from django.db import models

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email

class Menu(models.Model):
    mid = models.AutoField(primary_key=True)
    mtitle = models.CharField(max_length=50)
    mtype = models.CharField(max_length=50)
    mprice = models.IntegerField(default=0)
    #mimg = models.ImageField(upload_to="images", default="")
    mdesc = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.mtitle

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    cname = models.CharField(max_length=90)
    cemail = models.CharField(max_length=90)
    address = models.CharField(max_length=90)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Order from ' + self.cname + ' - ' + self.items_json

class Payment(models.Model):
    Pid = models.AutoField(primary_key=True)
    cardowner = models.CharField(max_length=100)
    cardnumber = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    cvv = models.IntegerField()

    def __str__(self):
        return 'Payment from ' + self.cardowner