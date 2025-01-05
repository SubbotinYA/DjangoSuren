"""
URL configuration for First_Project project.

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
from django.template.backends.django import Template
from django.urls import path, include
from django.views.generic import TemplateView
#здесь прописывают маршруты к шаблонам
#name="begin" так назвали нашу ссылку стартовой страницы
urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="begin"), #path("", здесь "" означают главную страницу.читай по слогам... "" этим поставили стартовой страницей. TemplateView.as_view это отрисовка нашего шаблона "index.html" не указали папку, т.к. ранее указали в settings DIRS': [BASE_DIR / 'templates'],
    path('site_app/', include('site_app_list.urls', namespace='Site_app')), #отделили urls админки от других urls и создали url.py в приложении site_app_list. site_app так назвали нашу ссылку на приложение по namespace делают переход в html
    path('admin/', admin.site.urls),
]
