# coding: utf-8
from django.core.exceptions import ValidationError
from django.forms.fields import MultiValueField, IntegerField, CharField
from django.utils.translation import ugettext_lazy as _
from binascii import unhexlify
from widgets import ImageCountCaptchaWidget


class ImageCountCaptchaField(MultiValueField):

    def __init__(self, min_images=1, max_images=5, attrs={}, *args, **kwargs):
        # set up error messages
        errors = self.default_error_messages.copy()
        if 'error_messages' in kwargs:
            errors.update(kwargs['error_messages'])
        localize = kwargs.get('localize', False)

        self.widget = ImageCountCaptchaWidget(
            min_images=min_images,
            max_images=max_images,
            attrs=attrs
        )

        # set fields
        fields = (
            IntegerField(min_value=0, localize=localize),
            CharField(max_length=255)
        )
        super(ImageCountCaptchaField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        """Compress takes the place of clean with MultiValueFields"""
        if data_list:
            answer = data_list[0]
            # unhash and eval question. Compare to answer.
            unhashed_answer = eval(unhexlify(data_list[1][40:]).split(u"|")[0])
            if answer != unhashed_answer:
                raise ValidationError(_(u'Incorrect, please try again.'))
            return answer
        return None
