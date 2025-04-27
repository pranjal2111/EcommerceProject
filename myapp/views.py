import razorpay
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def register(request):
    return render(request,"register.html")

def fetchformdata(request):
    #form to variable
    name=request.POST.get("name")
    email=request.POST.get("email")
    phone=request.POST.get("phone")
    password=request.POST.get("password")
    address=request.POST.get("address")
    gender=request.POST.get("gender")
    role=request.POST.get("role")
    profilepicture=request.FILES["dp"]

    #check email in database
    #if available ==> account already exists , please log in now
    #else ==> insert query into model , show successs message
    if registermodel.objects.filter(email=email,phone=phone).exists():
        messages.error(request, "Account already exists, please login now.")
        return render(request, "login.html")
    else:
        registermodel.objects.all()

 #inser query
    insertquery=registermodel(name=name,email=email,phone=phone,password=password,address=address,gender=gender,role=role,profilepicture=profilepicture)
    insertquery.save()
    messages.success(request,"Registered Successfully!")
    return render(request,"login.html")

def login(request):
    return render(request,"login.html")

def logindata(request):
    identifier=request.POST.get("email")
    password=request.POST.get("password")

    try:

            if '@' in identifier:
                userdata = registermodel.objects.get(email=identifier, password=password)
            else:
                userdata = registermodel.objects.get(phone=identifier, password=password)
            print(userdata)


            request.session["log_id"]=userdata.id
            request.session["log_name"]=userdata.name
            request.session["log_email"]=userdata.email
            request.session["log_role"] = userdata.role
            request.session["profile_picture"] = userdata.profilepicture.url

            print("session name:",request.session["log_name"])
            return redirect("/")

    except:
        messages.error(request, "Invalid Credentials!!")
        return render(request, "login.html")

def logout(request):
    try:
        del request.session["log_id"]
        del request.session["log_name"]
        del request.session["log_email"]
        del request.session["log_role"]
        del request.session["profile_picture"]

    except:
        pass
    return redirect("/login")

def showproducts(request):
    fetchdata = Product.objects.all()
    fetchcatdata = Category.objects.all()

    # Pagination
    paginator = Paginator(fetchdata, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Fetch the user's profile if logged in
    user_profile = None
    if request.session.get("log_id"):
        try:
            user_profile = registermodel.objects.get(user_id=request.session["log_id"])
        except :
            user_profile = None

    context = {
        "data": page_obj,
        "paginator": paginator,
        "user_profile": user_profile,
        "catdata": fetchcatdata

    }
    return render(request, "showproducts.html", context)


def singleproducts(request,id):
    fetchdata = Product.objects.get(id=id)
    fetchproduct=productimage.objects.filter(productid=id)
    context = {
        "data": fetchdata,
        "images":fetchproduct
    }
    return render(request,"singleproducts.html",context)

def addproduct(request):
    if request.session.get("log_role") != 'seller':
        messages.error(request, "You do not have permission to add products.")
        return redirect("/")
    fetchcatdata = Category.objects.all()
    fetchdata = Category.objects.all()
    context = {
        "data": fetchdata,
        "catdata": fetchcatdata,

    }
    fetchproduct = Product.objects.all()
    print(fetchproduct)

    return render(request,"addproduct.html",context)

def insertproduct(request):
    name = request.POST.get('name')
    category = request.POST.get('category')
    image = request.FILES['image']
    price = request.POST.get('price')
    description = request.POST.get('description')
    status = request.POST.get('status')


    insertquery = Product(name=name, category=Category(id=category), image=image, price=price, description=description,
                          status=status,seller=registermodel(id=request.session["log_id"]))
    messages.success(request, "Add Product successfully!")
    insertquery.save()

    return redirect('/')

def manageproduct(request):
    sellerid_loggedin=request.session["log_id"]
    fetchdata=Product.objects.filter(seller=sellerid_loggedin)
    fetchcatdata = Category.objects.all()

    context={
        "data":fetchdata,
        "catdata": fetchcatdata,
    }
    return render(request,"manageproduct.html",context)

def manageinsertproduct(request):
    productid = request.POST.get('productid')

    pimage = request.FILES['pimage']
    insertquery = productimage( productid=Product(id=productid),pimage=pimage)
    messages.success(request, "Add Image successfully!")
    insertquery.save()

    return redirect("/")

def deleteproduct(request,id):
    Product.objects.get(id=id).delete()
    messages.success(request,"Iteam Deleted")
    return redirect("/manageproduct")

def editproduct(request,id):
    print(id)
    fetchdata = Product.objects.get(id=id)
    fetchcategory = Category.objects.all().order_by('id')

    context = {
        "data": fetchdata,
        "category": fetchcategory
    }
    return render(request,"editproduct.html",context)


def updateproduct(request):
    name = request.POST.get("name")
    category = request.POST.get("category")
    price = request.POST.get("price")
    description = request.POST.get("description")
    status = request.POST.get("status")
    pid = request.POST.get("pid")

    # Fetch the existing product
    fetchdata = Product.objects.get(id=pid)

    # Update fields
    fetchdata.name = name
    fetchdata.category = Category(id=category)
    fetchdata.price = price
    fetchdata.description = description
    fetchdata.status = status

    # Check if a new image is uploaded
    fetchdata.image = request.FILES.get('image', fetchdata.image)

    # Save the updated product
    fetchdata.save()
    messages.success(request, "Updated Successfully")
    return redirect("/manageproduct")


def cateviseproduct(request,id):
    fetchcatdata = Category.objects.all()
    catdata = Category.objects.get(id=id)
    fetchdata = Product.objects.filter(category_id=id)
    context = {
        "data":fetchdata,
        "catdata":fetchcatdata,
        "id":catdata.name
    }
    return render(request,"cateviseproduct.html",context)

def inquirypage(request,id):
    fetchdata = Product.objects.get(id=id)
    context = {
        "pid":id,
        "data":fetchdata
    }
    return render(request,"inquiry.html",context)

def submitinquiry(request):
    userid = request.session["log_id"]
    pid = request.POST.get("pid")
    phone = request.POST.get("phone")
    address = request.POST.get("address")
    budget = request.POST.get("budget")
    quantity = request.POST.get("quantity")
    msg = request.POST.get("msg")

    storedata = inquiry(userid=registermodel(id=userid),productid=Product(id=pid),phone=phone,
                        address=address,budget=budget,quantity=quantity,msg=msg)
    storedata.save()
    messages.success(request,"Inquiry Generated.")

    return redirect("/")

def insertintocart(request):
    userid = request.session["log_id"]
    quantity = request.POST.get("quantity")
    pid = request.POST.get("pid")
    price = request.POST.get("price")
    totalamount = int(quantity) * float(price)

    try:
        fetchdata = cart.objects.get(productid=pid,orderstatus=1)
    except:
        fetchdata = None

    if fetchdata is not None:
        # update quantity
        fetchdata.quantity+=int(quantity)
        fetchdata.totalamount+=float(totalamount)
        fetchdata.save()

    else:
        storedata = cart(userid=registermodel(id=userid),productid=Product(id=pid),quantity=quantity,
                         totalamount=totalamount,orderid=0,orderstatus=1)
        storedata.save()
        messages.success(request,"Item Added to cart")
    return redirect("/")

def showcart(request):
    userid = request.session["log_id"]
    fetchdata = cart.objects.filter(userid=userid,orderstatus=1)
    total = sum(item.totalamount for item in fetchdata)
    fetchcatdata = Category.objects.all()

    context = {
        "data":fetchdata,
        "total":total,
        "catdata": fetchcatdata,

    }
    return render(request,"cart.html",context)

def removeitem(request,id):
    cart.objects.get(id=id).delete()
    messages.success(request,"Item removed")
    return redirect("/showcart")

def decrease(request,id):
    fetchdata = cart.objects.get(id=id)
    if fetchdata.quantity == 1:
        fetchdata.delete()
    else:
        fetchdata.quantity-=1
        fetchdata.totalamount-=fetchdata.productid.price
        fetchdata.save()
    return redirect("/showcart")
def increase(request,id):
    fetchdata = cart.objects.get(id=id)
    fetchdata.quantity+=1
    fetchdata.totalamount += fetchdata.productid.price
    fetchdata.save()
    return redirect("/showcart")

def placeorder(request):
    userid = request.session["log_id"]
    finaltotal = request.POST.get("total")
    phone = request.POST.get("phone")
    address = request.POST.get("address")
    paymode = request.POST.get("payment")
    print(paymode)

    if paymode == "Cash on Delivery":
        storedata = ordermodel(
            userid=registermodel(id=userid),
            finaltotal=finaltotal,
            phone=phone,
            address=address,
            paymode=paymode,
            status=True
        )
        storedata.save()

        lastid = storedata.id
        fetchdata = cart.objects.filter(userid=userid, orderstatus=1)
        for i in fetchdata:
            i.orderstatus = 0
            i.orderid=lastid
            i.save()



        messages.success(request,"Order Placed")
    else:
        from django.conf import settings

        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_SECRET_KEY))
        order_amount = int(float(finaltotal) * 100)  # Razorpay needs amount in paise
        razorpay_order = client.order.create({
            "amount": order_amount,
            "currency": "INR",
            "receipt": f"order_rcptid_{userid}",
            "payment_capture": "1",
        })

        storedata = ordermodel(
            userid=registermodel(id=userid),
            finaltotal=finaltotal,
            phone=phone,
            address=address,
            paymode="Online",
            status=True,
            razorpay_order_id=razorpay_order['id'],
        )
        storedata.save()

        lastid = storedata.id

        # Update Cart Items
        cart_items = cart.objects.filter(userid=userid, orderstatus=1)
        for item in cart_items:
            item.orderstatus = 0
            item.orderid = lastid
            item.save()

        from django.conf import settings
        return render(request, "payment.html", {
            "razorpay_order_id": razorpay_order['id'],
            "amount": order_amount,
            "key": settings.RAZORPAY_KEY_ID,
            "currency": "INR",
        })

    return redirect("/")
def your_orders(request):
    if not request.session.get("log_id"):
        messages.error(request, "You need to log in to view your orders.")
        return redirect("/login")

    userid = request.session["log_id"]
    fetch_orders = ordermodel.objects.filter(userid=registermodel(id=userid))
    fetchcatdata = Category.objects.all()

    context = {
        "orders": fetch_orders,
        "catdata": fetchcatdata,

    }
    return render(request, "your_orders.html", context)

def payment_success(request):
 return redirect("/")