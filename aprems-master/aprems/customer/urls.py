"""
URL configuration for aprems project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Home,name="customer/home"),
    path('feedback/', views.feedback_form, name='feedback_form'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('add_product/',views.add_product,name='add_product'),
    path('product_list/',views.product_list,name='product_list'),
    path('add_to_cart/<int:product_id>/',views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('profile/', views.user_profile, name='user_profile'),
    path('payment/', views.payment, name='payment'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_manage_users/', views.manage_users, name='manage_users'),
    path('admin_manage_products/', views.manage_products, name='manage_products'),
    path('admin_manage_feedback/', views.manage_feedback, name='manage_feedback'),

]

# from django.conf import settings
# from django.conf.urls.static import static
#
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)