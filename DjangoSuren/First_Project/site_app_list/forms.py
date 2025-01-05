from django import forms

from site_app_list.models import Example1#название НАШЕ базы данных


class SiteItemCrateForm(forms.ModelForm):#при создании используем .ModelForm а не просто Form
    class Meta:
        model=Example1#связываем эту форму с нашей моделью
        fields=("title", "description")#какие поля из модели отображать при создании
        widgets = {"description": forms.Textarea(attrs={"cols": 50, "rows": 10}),}
        help_texts={"description": "какой то текст с помощью",}
    # title = forms.CharField(
    #     max_length=250,
    #     #widget=forms.Textarea(),
    #     widget = forms.TextInput(),
    # )

    # widgets={
    #     "title": forms.Textarea(attrs={"cols":30, "rows":5}),
    # }


class SiteItemUpdateForm(forms.ModelForm):
    class Meta(SiteItemCrateForm.Meta):
        fields=("title",
                "description",
                "aga",
        )