#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example.settings")

    from django.core.management import execute_from_command_line

    # for example purpouse - DO NOT add this in production
    sys.path.append(os.path.abspath(__file__ + '/../../../image_count_captcha'))

    execute_from_command_line(sys.argv)
