# coding: utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.views.generic.edit import FormView
from image_count_captcha.fields import ImageCountCaptchaField


class ExampleForm(forms.Form):
    field = forms.CharField(required=True)
    captcha = ImageCountCaptchaField(
        label=_(u"How many circles do you see?"),
        min_images=1,
        max_images=5,
        required=True)


class HomeView(FormView):
    form_class = ExampleForm
    template_name = "form.html"
