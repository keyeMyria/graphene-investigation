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
    RefereeGameComposition,
    User
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


class UserType(DjangoObjectType):
    class Meta:
        model = User


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
    all_users = graphene.List(UserType)

    post = graphene.Field(
        PostType,
        id=graphene.Int(),
        name=graphene.String()
    )
    comment = graphene.Field(
        CommentType,
        id=graphene.Int(),
        bodytext=graphene.String()
    )
    tag = graphene.Field(TagType)
    team = graphene.Field(TeamType)
    referee = graphene.Field(RefereeType)
    countrie = graphene.Field(CountryType)
    group = graphene.Field(GroupType)
    athlete = graphene.Field(AthleteType)
    coache = graphene.Field(CoachType)
    game = graphene.Field(GameType)
    team_game_composition = graphene.Field(TeamGameCompositionType)
    referee_game_composition = graphene.Field(RefereeGameCompositionType)
    user = graphene.Field(UserType)

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

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_post(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')

        if id is not None:
            return Post.objects.get(pk=id)

        if title is not None:
            return Post.objects.get(title=title)

        return None

    def resolve_comment(self, info, **kwargs):
        id = kwargs.get('id')
        bodytext = kwargs.get('bodytext')

        if id is not None:
            return Comment.objects.get(pk=id)

        if bodytext is not None:
            return Comment.objects.get(bodytext=bodytext)

        return None

# 1) Defines a mutation class. Right after, you define the output of the mutation, the data
# the server can send back to the client. The output is defined field by field for
# learning purposes. On the next mutation you’ll define them as just one.
class CreatePost(graphene.Mutation):
    id = graphene.Int()
    author = graphene.Field(User)
    tags = graphene.List(Tag)
    title = graphene.String()
    text = graphene.String()
    post_date = graphene.types.datetime.DateTime()
    updated = graphene.types.datetime.DateTime()
    created = graphene.types.datetime.DateTime()

    #2 Defines the data you can send to the server, in this case, it's
    # the author_id, title, and text.
    class Arguments:
        author_id = graphene.Int()
        title = graphene.String()
        text = graphene.String()

    #3 The mutation method: it creates a post on the database using the data sent by the user,
    # through the author_id, title, and text parameters. After, the server returns the CreatePost
    # class with the data just created. See how this matches the parameters set on #1.
    def mutate(self, info, author_id, title, text):
        user = User.objects.get(id=author_id)
        post = Post.objects.create(user=user, title=title, text=text)

        return CreatePost(
            id=link.id,
            url=link.url,
            description=link.description,
        )

#4 Creates a mutation class with a field to be resolved, which points to our mutation defined before.
class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
