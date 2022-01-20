from django import template
from ..models import *
from django.db.models import Count,Q,Max
from django.contrib.auth.models import User


register = template.Library()

@register.inclusion_tag("favorite.html")
def sell_count(request):
    return request.user.fa_pro.count()

