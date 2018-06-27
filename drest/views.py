from dynamic_rest.viewsets import DynamicModelViewSet

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
    User,
)

from drest.serializers import (
    PostSerializer,
    CommentSerializer,
    TagSerializer,
    TeamSerializer,
    RefereeSerializer,
    CountrySerializer,
    GroupSerializer,
    AthleteSerializer,
    CoachSerializer,
    GameSerializer,
    TeamGameCompositionSerializer,
    RefereeGameCompositionSerializer,
    UserSerializer,
)


class PostViewSet(DynamicModelViewSet):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(DynamicModelViewSet):
    model = Comment
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class TagViewSet(DynamicModelViewSet):
    model = Tag
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TeamViewSet(DynamicModelViewSet):
    model = Team
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class RefereeViewSet(DynamicModelViewSet):
    model = Referee
    queryset = Referee.objects.all()
    serializer_class = RefereeSerializer


class CountryViewSet(DynamicModelViewSet):
    model = Country
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class GroupViewSet(DynamicModelViewSet):
    model = Group
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class AthleteViewSet(DynamicModelViewSet):
    model = Athlete
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer


class CoachViewSet(DynamicModelViewSet):
    model = Coach
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


class GameViewSet(DynamicModelViewSet):
    model = Game
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class TeamGameCompositionViewSet(DynamicModelViewSet):
    model = TeamGameComposition
    queryset = TeamGameComposition.objects.all()
    serializer_class = TeamGameCompositionSerializer


class RefereeGameCompositionViewSet(DynamicModelViewSet):
    model = RefereeGameComposition
    queryset = RefereeGameComposition.objects.all()
    serializer_class = RefereeGameCompositionSerializer


class UserViewSet(DynamicModelViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
