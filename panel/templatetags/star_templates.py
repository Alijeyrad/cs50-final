import math
from panel.models import User
from django import template

register = template.Library()

@register.inclusion_tag('panel/mytemplatetags/stars.html')
def show_stars(doctor):
    d = User.objects.all().filter(pk=doctor.id).first()
    stars = 0
    votes = 0
    for vote in d.vote_for.all():
        stars += vote.stars
        votes += 1
    if votes == 0:
        votes = 1
    mean_stars = math.floor(stars / votes)
    stars_list = [1 for star in range(mean_stars)]
    while len(stars_list) != 5:
        stars_list.append(0)
    
    return {'stars_list': stars_list}