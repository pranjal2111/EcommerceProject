"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path

from django.conf.urls.static import static

from django.conf import settings

from myapp import views

urlpatterns = [

                  path('admin/', admin.site.urls),
                  path('register', views.register),
                  path('fetchformdata', views.fetchformdata),
                  path('login', views.login),
                  path('', views.showproducts),
                  path('singleproducts/<int:id>', views.singleproducts),
                  path('logindata',views.logindata),
                  path('logout', views.logout),
                  path('addproduct',views.addproduct),
                  path('insertproduct', views.insertproduct),
                  path('manageproduct',views.manageproduct),
                  path('manageinsertproduct', views.manageinsertproduct),
                  path('deleteproduct/<int:id>', views.deleteproduct),
                  path('editproduct/<int:id>', views.editproduct),
                  path('updateproduct', views.updateproduct),
                path("cateviseproduct/<int:id>",views.cateviseproduct),
                path("inquirypage/<int:id>",views.inquirypage),
                path("submitinquiry",views.submitinquiry),
                path("insertintocart",views.insertintocart),
                path("placeorder",views.placeorder),
                path("showcart",views.showcart),
                path("removeitem/<int:id>",views.removeitem),
                path("decrease/<int:id>",views.decrease),
                path("increase/<int:id>",views.increase),
                path('your-orders', views.your_orders),
                path('payment-success', views.payment_success),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


