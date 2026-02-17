from django import template
from website.models import EventMember


register = template.Library()

@register.filter
def get_members_count(event):
    return len(EventMember.objects.filter(event=event))