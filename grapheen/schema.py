import graphene

from graphene_django import DjangoObjectType

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


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment


class TagType(DjangoObjectType):
    class Meta:
        model = Tag


class TeamType(DjangoObjectType):
    class Meta:
        model = Team


class RefereeType(DjangoObjectType):
    class Meta:
        model = Referee


class CountryType(DjangoObjectType):
    class Meta:
        model = Country


class GroupType(DjangoObjectType):
    class Meta:
        model = Group


class AthleteType(DjangoObjectType):
    class Meta:
        model = Athlete


class CoachType(DjangoObjectType):
    class Meta:
        model = Coach


class GameType(DjangoObjectType):
    class Meta:
        model = Game


class TeamGameCompositionType(DjangoObjectType):
    class Meta:
        model = TeamGameComposition


class RefereeGameCompositionType(DjangoObjectType):
    class Meta:
        model = RefereeGameComposition


class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)
    all_comments = graphene.List(CommentType)
    all_tags = graphene.List(TagType)
    all_teams = graphene.List(TeamType)
    all_referees = graphene.List(RefereeType)
    all_countries = graphene.List(CountryType)
    all_groups = graphene.List(GroupType)
    all_athletes = graphene.List(AthleteType)
    all_coaches = graphene.List(CoachType)
    all_games = graphene.List(GameType)
    all_team_game_compositions = graphene.List(TeamGameCompositionType)
    all_referee_game_compositions = graphene.List(RefereeGameCompositionType)

    def resolve_all_posts(self, info, **kwargs):
        return Post.objects.all()

    def resolve_all_comments(self, info, **kwargs):
        return Comment.objects.all()

    def resolve_all_tags(self, info, **kwargs):
        return Tag.objects.all()

    def resolve_all_teams(self, info, **kwargs):
        return Team.objects.all()

    def resolve_all_referees(self, info, **kwargs):
        return Referee.objects.all()

    def resolve_all_countries(self, info, **kwargs):
        return Country.objects.all()

    def resolve_all_groups(self, info, **kwargs):
        return Group.objects.all()

    def resolve_all_athletes(self, info, **kwargs):
        return Athlete.objects.all()

    def resolve_all_coaches(self, info, **kwargs):
        return Coach.objects.all()

    def resolve_all_games(self, info, **kwargs):
        return Game.objects.all()

    def resolve_all_team_game_compositions(self, info, **kwargs):
        return TeamGameComposition.objects.all()

    def resolve_all_referee_game_compositions(self, info, **kwargs):
        return RefereeGameComposition.objects.all()
