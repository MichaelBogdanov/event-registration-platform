from django import template
from website.models import Event, Club, EventMember


register = template.Library()

@register.filter
def get_user_events(user):
    return [enrollment.event for enrollment in EventMember.objects.filter(user=user) if enrollment.event.id in [event.id for event in Event.objects.all()]]

@register.filter
def get_user_clubs(user):
    return [enrollment.event for enrollment in EventMember.objects.filter(user=user) if enrollment.event.id in [club.id for club in Club.objects.all()]]

@register.filter
def get_organized_events(user):
    return Event.objects.filter(organizer=user)

@register.filter
def get_organized_clubs(user):
    return Club.objects.filter(organizer=user)

@register.filter
def get_role(user):
    ROLES = {
        'student': 'Учащийся',
        'parent': 'Родитель',
        'organizer': 'Организатор'
    }
    return ROLES[user.role]