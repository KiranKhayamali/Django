"""meeting_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from website.views import welcome, date, about, electronics
from coffee_shop.views import Home, Signup, Thanks, Details, PlaceOrder
urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome', welcome, name='welcome'),
    path('datetime', date),
    path('about', about),
    path('meetings/', include('meetings.urls')),
    path('store', electronics, name='store'),
    path('', Home, name='home'),
    path('signup/', Signup, name='signup'),
    path('thanks', Thanks, name='thanks'),
    path('details/', Details, name='details'),
    path('order/', PlaceOrder, name='order'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
