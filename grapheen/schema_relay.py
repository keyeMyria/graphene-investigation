import graphene
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

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
    RefereeGameComposition,
    User
)


#1 Relay allows you to use django-filter for filtering data.
# Here, you’ve defined a FilterSet, with the desired fields for each model
class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = [
            'author',
            'tags',
            'title',
            'text',
            'post_date',
            'updated',
            'created',
        ]


class CommentFilter(django_filters.FilterSet):
    class Meta:
        model = Comment
        fields = [
            'post',
            'creator',
            'bodytext',
            'post_date',
            'updated',
            'created',
        ]


class TagFilter(django_filters.FilterSet):
    class Meta:
        model = Tag
        fields = [
            'name',
            'updated',
            'created',
        ]


class TeamFilter(django_filters.FilterSet):
    class Meta:
        model = Team
        fields = [
            'country',
            'group',
            'ranking',
            'games',
        ]


class RefereeFilter(django_filters.FilterSet):
    class Meta:
        model = Referee
        fields = [
            'user',
            'poor_eyesight',
            'games',
        ]


class CountryFilter(django_filters.FilterSet):
    class Meta:
        model = Country
        fields = [
            'name',
            'population',
            'annual_gdp',
            'national_anthem_text',
        ]


class GroupFilter(django_filters.FilterSet):
    class Meta:
        model = Group
        fields = ['name']


class AthleteFilter(django_filters.FilterSet):
    class Meta:
        model = Athlete
        fields = [
            'user',
            'team',
            'height',
            'weight',
        ]


class CoachFilter(django_filters.FilterSet):
    class Meta:
        model = Coach
        fields = [
            'user',
            'team',
            'favorite_strategy',
        ]


class GameFilter(django_filters.FilterSet):
    class Meta:
        model = Game
        fields = [
            'start_time',
            'location',
        ]


class TeamGameCompositionFilter(django_filters.FilterSet):
    class Meta:
        model = TeamGameComposition
        fields = [
            'team',
            'game',
            'is_home',
            'result',
        ]


class RefereeGameCompositionFilter(django_filters.FilterSet):
    class Meta:
        model = RefereeGameComposition
        fields = [
            'referee',
            'game',
            'position',
        ]


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username']


class PostNode(DjangoObjectType):
    class Meta:
        model = Post
        #3 Each node implements an interface with an unique ID
        # (you’ll see the result of this in a bit).
        interfaces = (graphene.relay.Node,)


class CommentNode(DjangoObjectType):
    class Meta:
        model = Comment
        interfaces = (graphene.relay.Node,)


class TagNode(DjangoObjectType):
    class Meta:
        model = Tag
        interfaces = (graphene.relay.Node,)


class TeamNode(DjangoObjectType):
    class Meta:
        model = Team
        interfaces = (graphene.relay.Node,)


class RefereeNode(DjangoObjectType):
    class Meta:
        model = Referee
        interfaces = (graphene.relay.Node,)


class CountryNode(DjangoObjectType):
    class Meta:
        model = Country
        interfaces = (graphene.relay.Node,)


class GroupNode(DjangoObjectType):
    class Meta:
        model = Group
        interfaces = (graphene.relay.Node,)


class AthleteNode(DjangoObjectType):
    class Meta:
        model = Athlete
        interfaces = (graphene.relay.Node,)


class CoachNode(DjangoObjectType):
    class Meta:
        model = Coach
        interfaces = (graphene.relay.Node,)


class GameNode(DjangoObjectType):
    class Meta:
        model = Game
        interfaces = (graphene.relay.Node,)


class TeamGameCompositionNode(DjangoObjectType):
    class Meta:
        model = TeamGameComposition
        interfaces = (graphene.relay.Node,)


class RefereeGameCompositionNode(DjangoObjectType):
    class Meta:
        model = RefereeGameComposition
        interfaces = (graphene.relay.Node,)


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node,)


class RelayQuery(graphene.ObjectType):
    #4  Uses the PostNode with the relay_post field inside the your new query.
    post = graphene.relay.Node.Field(PostNode)
    comment = graphene.relay.Node.Field(CommentNode)
    tag = graphene.relay.Node.Field(TagNode)
    team = graphene.relay.Node.Field(TeamNode)
    referee = graphene.relay.Node.Field(RefereeNode)
    country = graphene.relay.Node.Field(CountryNode)
    group = graphene.relay.Node.Field(GroupNode)
    athlete = graphene.relay.Node.Field(AthleteNode)
    coach = graphene.relay.Node.Field(CoachNode)
    game = graphene.relay.Node.Field(GameNode)
    team_game_composition = graphene.relay.Node.Field(TeamGameCompositionNode)
    referee_game_composition = graphene.relay.Node.Field(RefereeGameCompositionNode)
    user = graphene.relay.Node.Field(UserNode)

    #5 Defines the relay_posts field as a Connection, which
    # implements the pagination structure.
    all_posts = DjangoFilterConnectionField(PostNode, filterset_class=PostFilter)
    all_comments = DjangoFilterConnectionField(CommentNode, filterset_class=CommentFilter)
    all_tags = DjangoFilterConnectionField(TagNode, filterset_class=TagFilter)
    all_teams = DjangoFilterConnectionField(TeamNode, filterset_class=TeamFilter)
    all_referees = DjangoFilterConnectionField(RefereeNode, filterset_class=RefereeFilter)
    all_countries = DjangoFilterConnectionField(CountryNode, filterset_class=CountryFilter)
    all_groups = DjangoFilterConnectionField(GroupNode, filterset_class=GroupFilter)
    all_athletes = DjangoFilterConnectionField(AthleteNode, filterset_class=AthleteFilter)
    all_coaches = DjangoFilterConnectionField(CoachNode, filterset_class=CoachFilter)
    all_games = DjangoFilterConnectionField(GameNode, filterset_class=GameFilter)
    all_team_game_compositions = DjangoFilterConnectionField(TeamGameCompositionNode, filterset_class=TeamGameCompositionFilter)
    all_referee_game_compositions = DjangoFilterConnectionField(RefereeGameCompositionNode, filterset_class=RefereeGameCompositionFilter)
    all_users = DjangoFilterConnectionField(UserNode, filterset_class=UserFilter)


class RelayCreatePost(graphene.relay.ClientIDMutation):
    post = graphene.Field(PostNode)

    class Input:
        title = graphene.String()
        text = graphene.String()


    def mutate_and_get_payload(root, info, **kwargs):
        user = User.objects.get(id=444) # hardcode user for onw
        post = Post.objects.create(
            author=user,
            title=kwargs.get('title'),
            text=kwargs.get('text'),
        )

        return RelayCreatePost(post=post)


class RelayMutation(graphene.AbstractType):
    create_post = RelayCreatePost.Field()
