from pathlib import Path
from typing import Any
from django import template

register = template.Library()

@register.simple_tag
def name(request):
  return request.GET.get('Name', '')

@register.simple_tag
def tipe(request):
  return request.GET.get('Tipo', '')

@register.simple_tag
def current(request):
  return request.GET.get('current', '')