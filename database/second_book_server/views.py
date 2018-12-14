from django.contrib import auth
from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import render
from second_book_server.models import *
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse

def registe(request):
    if request.method == 'GET':
        return render(request,'register.html')
    if request.method == 'POST':
        data = request.POST.copy()
        email = data.get('email')
        username = data.get('nickname')
        password = data.get('password')
        university = data.get('university')
        print(email)
        find_same = User.object.filter(email = email)
        print(find_same)
        if len(find_same) > 0:
            return render(request,'register.html')
        else:
            User.object.create_user(email = email,username=username,password = password,university=university)
            return render(request, 'index.html')

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.get('password')
        is_user = User.object.filter(email = email)
        if is_user:
            user = authenticate(email=email, password=password)
            if user is not None:
                auth.login(request,user)
                return render(request,'index.html')
            else:
                return render(request,'login.html')
        else:
            return render(request, 'login.html')

def index(request):
    if request.method == 'GET':
        return render(request,'index.html')
    return HttpResponse('OK')

#活动的详情的战士页面的响应，请求包含活动名称，返回的时候根据特定的名称进行响应
def activity(request):
    if request.method == 'GET':
        return render(request,'activity.html')
    if request.method == 'POST':
        activity_id = request.POST.get('activity_id')
        resultObject = Activity.objects.get(activity_id= activity_id)
        result = model_to_dict(resultObject)
        return JsonResponse(result,safe=True)

#公告的详情的界面响应，请求会返回所有的公告的内容
def announcement(request):
    if(request.method == 'GET'):
        return render(request,"announcement.html")
    if(request.method == 'POST'):
        json_list = []
        announcementObject = Announcement.objects.all()
        for announcement in announcementObject:
            json_data = model_to_dict(announcement)
            json_list.append(json_data)
        return JsonResponse(json_list,safe=False)

#商品的详情界面响应，返回的商品的详细信息这个商品的评价信息
def goods(request):
    if(request.method == 'GET'):
        goods_id = request.GET.get("goods_id")
        goodsObject = Goods.objects.get(goods_id=goods_id)
        goodsResult = model_to_dict(goodsObject)
        bookImage = {}
        bookImage['iamge'] = "static/goods/"+goodsResult['goods_name']+"/"+goodsResult['goods_name']+".jpg"
        bookImage['iamge1'] = "static/goods/" + goodsResult['goods_name'] + "/" + goodsResult['goods_name'] + "1.jpg"
        bookImage['iamge2'] = "static/goods/" + goodsResult['goods_name'] + "/" + goodsResult['goods_name'] + "2.jpg"
        return render(request,'goods.html',{"goods_id":goods_id,"bookImage":bookImage})
    if(request.method == 'POST'):
        goods_id = request.POST['goods_id']
        print(goods_id)
        goodsObject = Goods.objects.get(goods_id = goods_id)
        goodsResult = model_to_dict(goodsObject)
        bookObject = Book.objects.get(bool_id= goodsResult['book_id'])
        print(bookObject)
        bookResult = model_to_dict(bookObject)
        jsonlist = []
        jsonlist.append(goodsResult)
        jsonlist.append(bookResult)
        commentObject = User_comment.objects.filter(goods_id=goods_id)
        for comment in commentObject:
            json_data = model_to_dict(comment)
            user = User.object.get(id = json_data['user_id'])
            userResult = model_to_dict(user)
            json_data['user_id'] = userResult['user_nickname']
            jsonlist.append(json_data)
        return JsonResponse(jsonlist, safe=False)

#商品的列表
def goods_list(request):
    type = request.GET.get('type')
    print(type)
    if type == "所有商品":
        listObject = Goods.objects.filter()
    else:
        listObject = Goods.objects.filter(subject=type)
    jsonlist = []
    for listitem in listObject:
        json_data = model_to_dict(listitem)
        jsonlist.append(json_data)
    return JsonResponse(jsonlist, safe=False)



