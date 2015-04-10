# coding: utf-8
from django import forms
from django.conf import settings
from django.template.defaultfilters import mark_safe
from binascii import hexlify, unhexlify
from PIL import Image
from random import randint
import base64
import cStringIO as StringIO
import hashlib


class ImageCountCaptchaWidget(forms.MultiWidget):

    def __init__(self, min_images=1, max_images=5, attrs=None, *args, **kwargs):
        self.attrs = attrs or {}
        self.min_images = min_images
        self.max_images = max_images

        widgets = (
            forms.TextInput(attrs={'size': '5', 'autocomplete': 'off'}),
            forms.HiddenInput()
        )
        super(ImageCountCaptchaWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        return [u"", self.hashed_answer]

    def render(self, name, value, attrs=None):
        x = randint(self.min_images, self.max_images)
        y = self.max_images - x
        self.x = x
        self.y = y
        self.hashed_answer = hashlib.sha1(settings.SECRET_KEY + str(x)). \
            hexdigest() + hexlify(str(x))
        if value:
            value[1] = self.hashed_answer

        # render image
        output = StringIO.StringIO()
        im_answer = Image.open(settings.CAPTCHA_IMAGE_ANSWER)
        im_other = Image.open(settings.CAPTCHA_IMAGE_OTHER)

        im_answer_size = im_answer.size
        im_other_size = im_other.size

        im = Image.new(
            "RGBA",
            getattr(settings, 'CAPTCHA_IMAGE_DIMENSIONS', (100, 50))
        )

        for i in xrange(self.x):
            im.paste(im_answer, (i * im_answer_size[0], 0), im_answer)
        for i in xrange(self.y):
            im.paste(
                im_other,
                (self.x * im_answer_size[0] + i * im_other_size[0], 0),
                im_other
            )

        im.save(output, format="PNG")
        output.seek(0)
        image_b64 = base64.b64encode(output.read())

        return mark_safe(
            u'<img src="data:image/png;base64,%s" class="cp-image"> %s' % (
                image_b64,
                super(ImageCountCaptchaWidget, self).render(name, value, attrs)
            ))
