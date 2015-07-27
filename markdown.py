from __future__ import absolute_import
from django import template
import markdown


register = template.Library()


def markdown_filter(value):
    return markdown.markdown(value)


register.filter('markdown', markdown_filter)
