from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.db import models
from django.utils import timezone

class MyUserManager(BaseUserManager):
    def create_user(self,email,username,password,university):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            user_nickname = username,
            university = university
        )
        user.set_password(password)
        user.save(using = self.db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    object = MyUserManager()
    register_time = models.DateTimeField('Register time',auto_now_add=True)
    user_nickname = models.CharField(max_length=30,default= "")
    university = models.CharField(max_length=30,default="")
    user_profile = models.TextField()
    USERNAME_FIELD = 'email'
    user_profile = models.TextField(null=True)
    is_admin = models.BooleanField(blank=False,default= False)
    user_is_active = models.BooleanField(blank=False,default= False)

class Book(models.Model):
    bool_id = models.CharField(max_length=30, primary_key=True)
    book_name = models.TextField(unique=True)
    publish_time = models.DateField(null=True)
    book_version = models.CharField(max_length=15)
    author = models.TextField(null=True)
    publish_house = models.CharField(max_length=30)


class Goods(models.Model):
    goods_id = models.CharField(max_length=30, primary_key=True)
    user_id = models.ManyToManyField(User)
    book_id = models.ManyToManyField(Book)
    goods_time = models.DateField(null=False)
    goods_price = models.DecimalField(max_digits=10, decimal_places=2)
    introduction = models.TextField()
    subject = models.TextField()
    amount = models.IntegerField()


#  关于登录时间有问题
class Logininformation(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    log_time = models.DateField(auto_now_add=True)
    log_ip = models.GenericIPAddressField()
    log_outtime = models.DateField()


class User_address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address_1 = models.TextField(null=True)
    address_2 = models.TextField(null=True)
    address_3 = models.TextField(null=True)
    address_4 = models.TextField(null=True)
    address_5 = models.TextField(null=True)


class Chat_record(models.Model):
    record_id = models.CharField(max_length=30, primary_key=True)
    sender_id = models.CharField(max_length=30)
    receiver_id = models.CharField(max_length=30)
    content = models.TextField()
    date_time = models.DateField(auto_now_add=True)


class Shopping_cart(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    goods_id = models.ForeignKey(Goods, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    amount = models.IntegerField()


class Favorites(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    goods_id = models.ForeignKey(Goods, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    Label = models.TextField()


class Ordersheet(models.Model):
    order_id = models.CharField(max_length=30, primary_key=True)
    buyer_id = models.CharField(max_length=30)
    Seller_id = models.CharField(max_length=30)
    goods_id = models.ForeignKey(Goods, on_delete=models.CASCADE)
    state = models.CharField(max_length=10)
    is_paid = models.BooleanField()


class User_comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(default='系统默认好评')
    goods_id = models.ForeignKey(Goods, on_delete=models.CASCADE)
    date = models.DateField()


class Coupon(models.Model):
    Coupon_id = models.CharField(max_length=30, primary_key=True)
    coupon_name = models.CharField(max_length=50)
    credits = models.DecimalField(max_digits=5, decimal_places=5)
    begin_time = models.DateField(auto_now_add=True)
    end_time = models.DateField()


#活动的详情的列表
class Activity(models.Model):
    #活动的id 由系统自动生成
    activity_id = models.CharField(max_length=30, primary_key=True)
    #活动的名称由管理员发布时来决定
    activity_name = models.CharField(max_length=50)
    #活动的内容
    content = models.TextField()
    #活动的开始时间
    begin_time = models.DateField()
    #活动的结束时间
    end_time = models.DateField()


class Activity_price(models.Model):
    activity_id = models.ManyToManyField(Activity)
    goods_id = models.ManyToManyField(Goods)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Announcement(models.Model):
    an_id = models.CharField(max_length=30, primary_key=True)
    an_title = models.CharField(max_length=50)
    an_content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
