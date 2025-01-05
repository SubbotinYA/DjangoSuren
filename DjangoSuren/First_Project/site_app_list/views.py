
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (TemplateView,
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )

from .forms import SiteItemCrateForm,SiteItemUpdateForm
from .models import Example1

# def index_view(request:HttpRequest)->HttpResponse:
#     my_views_list2 = Example1.objects.order_by("-id").all()    # решили вытащить из базы объекты. .order_by это сортировка объекта (-id) это сортирова в обратную сторону
#     context = { "my_list" : my_views_list2 }
#
#     # my_views_list=[ #это ручной список. сверху сделали автоматическое создание из объектов нашей модели
#     #     "Element 1",
#     #     "Element 2",
#     #     "Element 3",
#     #     "Еще элемент добавили",
#     #     ]
#     #context = {"my_list": my_views_list1}
#
#     return render( request, "site_app_list/index.html", context)
#           ####"app_views":app_views_list[:3] такой записью определяем количество элементов брать из базы



# class SiteListIndexView(TemplateView):
#     template_name = "site_app_list/index.html"
#
#     def get_context_data(self, **kwargs): #переопределяем функцию
#         context= super().get_context_data(**kwargs)#метод  берет данные из базы данных
#         context["app_views"]=Example1.objects.order_by("-id").all()# Этим мы переопределили метод
#         return context

class SiteListView(ListView):
    template_name = "site_app_list/index.html"
    queryset = Example1.objects.order_by("-id").all()[:4]#сформулировали и сформировали запрос
    #model = Example1# model = Example1 берет все из базы. Этим мы назначаем сколько элементов брать из базы
    #context_object_name = "my_list"  # это для строки {% for app in my_list %} в Index.html.# но когда закомментировали строка стала {% for app in object_list %}
    # def get_context_data(self, **kwargs):
    #     print('Example1._meta.app_label= ',Example1._meta.app_label) #это просто пример
    #     print('Example1._meta.model_name= ',Example1._meta.model_name)
    #     return super().get_context_data(**kwargs)

class SiteListIndexView(ListView):
    template_name = "site_app_list/siteapp_list.html"
    model = Example1# здесь показываем всех игроков т.к. не использовали  queryset = Example1.objects.order_by("-id").all()[:4]

class SiteListAgaView(ListView):
    template_name = "site_app_list/siteapp_list.html"
    queryset = Example1.objects.filter(aga=True).all()#отфильтровали улыбающихся игроков

class SiteDetailView(DetailView):
    template_name = "site_app_list/siteapp_detail.html"
    model = Example1

class SiteItemCreateView(CreateView): #это для формы титл
    model = Example1
    form_class = SiteItemCrateForm
    template_name = "site_app_list/siteapp_form.html"
    #fields = ("title", "description") #добавили description

    # после нажатия на копку создается объект и  переходим на SiteApp:detail. Чтобы не переопределять эту функцию в других классах представления создадим get_absolute_url в модели Example1
    # def get_success_url(self):
    #     return reverse(
    #         "SiteApp:detail",# на эту вьюшку
    #         kwargs={"pk":self.object.pk},) примени primery_key(то есть id) на self.object(это объект который создали только что)

class SiteItemUpdateView(UpdateView):
    model = Example1
    template_name = "site_app_list/siteapp_update_form.html"
    form_class = SiteItemUpdateForm

class SiteItemDeleteView(DeleteView):
    model = Example1
    template_name = "site_app_list/site_app_delete.html"
    success_url = reverse_lazy('Site_app:list')#куды переходим после удаления на подготовленную страницу