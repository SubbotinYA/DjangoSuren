from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name= 'SiteApp' # написали название приложения для префикса в пространстве имен.path('',views.SiteListView.as_view(),name="index") вот здесь name="index" может быть и в других приложениях

urlpatterns = [
#path('',views.index_view, name="index"),
#path('',views.SiteIndex.as_view(),name="index") # path("", TemplateView.as_view(template_name="index.html"), name="begin") это в главной url. здесь  не использовали (template_name="index.html") т.к. есть вьюшка и и там через render отправляется страница пользователю

path('',views.SiteListView.as_view(),name="index"),
path('list/',views.SiteListIndexView.as_view(),name="list"),
path('aga/',views.SiteListAgaView.as_view(),name="aga"),
path("<int:pk>/",views.SiteDetailView.as_view(),name="detail"), #этот pk получили от href="{% url 'SiteApp:detail' element.pk %}"
path('create/',views.SiteItemCreateView.as_view(),name="create"),
path('<int:pk>/update/',views.SiteItemUpdateView.as_view(),name="update"),
path('<int:pk>/confirm-delete/',views.SiteItemDeleteView.as_view(),name="delete"),

    # path('',
    # #      TemplateView.as_view(
    # #      #template_name="site_app_list/index.html"
    # #
    # # ), ## вместо этого блока указали функцию из views.py
    #      views.index_view, # крутотень from . import views импортировали views. views.index_view используем только функцию index_view
    #      name="index"
    #      ),
]
