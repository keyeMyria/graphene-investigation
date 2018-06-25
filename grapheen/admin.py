from django.contrib import admin

# Register your models here.
from models.models import (
    Post,
    Comment,
    Tag,
    Team,
    Referee,
    Country,
    Group,
    Athlete,
    Coach,
    Game,
    TeamGameComposition,
    RefereeGameComposition
)

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Team)
admin.site.register(Referee)
admin.site.register(Country)
admin.site.register(Group)
admin.site.register(Athlete)
admin.site.register(Coach)
admin.site.register(Game)
admin.site.register(TeamGameComposition)
admin.site.register(RefereeGameComposition)
