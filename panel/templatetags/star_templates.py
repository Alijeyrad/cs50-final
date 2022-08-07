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

@register.simple_tag
def total_stars(doctor):
    d = User.objects.all().filter(pk=doctor.id).first()
    total_stars = 0
    for vote in d.vote_for.all():
        total_stars += vote.stars
    
    return total_stars

@register.inclusion_tag('panel/mytemplatetags/ratings.html')
def show_ratings(doctor):
    d = User.objects.all().filter(pk=doctor.id).first()
    vote_one = 0
    vote_two = 0
    vote_three = 0
    vote_four = 0
    vote_five = 0
    vote_total = 0
    for vote in d.vote_for.all():
        vote_total += 1

        if vote.stars == 1:
            vote_one += 1
        if vote.stars == 2:
            vote_two += 1
        if vote.stars == 3:
            vote_three += 1
        if vote.stars == 4:
            vote_four += 1
        if vote.stars == 5:
            vote_five += 1
    
    if vote_total == 0:
        vote_total = 1

    one_percent = 100*(vote_one/vote_total) if vote_one != 0 else 5
    two_percent = 100*(vote_two/vote_total) if vote_two != 0 else 5
    three_percent = 100*(vote_three/vote_total) if vote_three != 0 else 5
    four_percent = 100*(vote_four/vote_total) if vote_four != 0 else 5
    five_percent = 100*(vote_five/vote_total) if vote_five != 0 else 5

    return {
        'vote_one': vote_one,
        'vote_two': vote_two,
        'vote_three': vote_three,
        'vote_four': vote_four,
        'vote_five': vote_five,
        'vote_total': vote_total,
        'one_percent': one_percent,
        'two_percent': two_percent,
        'three_percent': three_percent,
        'four_percent': four_percent,
        'five_percent': five_percent
    }