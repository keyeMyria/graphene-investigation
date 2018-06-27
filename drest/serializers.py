from dynamic_rest.serializers import (
    DynamicModelSerializer,
)
from dynamic_rest.fields import (
    DynamicMethodField,
    DynamicRelationField
)

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


class PostSerializer(DynamicModelSerializer):

    class Meta:
        model = Post
        name = 'post'
        fields = (
            'author',
            'tags',
            'title',
            'text',
            'post_date',
            'updated',
            'created',
            'id',
            'comments'
        )
        deferred_fields = (
            'author',
            'tags',
            'comments',
        )

    author = DynamicRelationField('UserSerializer')
    tags = DynamicRelationField('TagSerializer', many=True)
    comments = DynamicRelationField('CommentSerializer', many=True)


class CommentSerializer(DynamicModelSerializer):

    class Meta:
        model = Comment
        name = 'comment'
        fields = (
            'post',
            'creator',
            'bodytext',
            'post_date',
            'updated',
            'created',
            'id'
        )
        deferred_fields = (
            'post',
            'creator',
        )

    creator = DynamicRelationField('UserSerializer')
    post = DynamicRelationField('PostSerializer')


class TagSerializer(DynamicModelSerializer):

    class Meta:
        model = Tag
        name = 'tag'
        fields = (
            'name',
            'updated',
            'created',
            'posts',
            'id'
        )
        deferred_fields = (
            'posts',
        )

    posts = DynamicRelationField('PostSerializer', many=True)


class TeamSerializer(DynamicModelSerializer):

    class Meta:
        model = Team
        name = 'team'
        fields = (
            'country',
            'group',
            'ranking',
            'games',
            'coaches',
            'athletes',
            'team_game_compositions',
            'id'
        )
        deferred_fields = (
            'country',
            'group',
            'games',
            'coaches',
            'athletes',
            'team_game_compositions',
        )

    country = DynamicRelationField('CountrySerializer')
    group = DynamicRelationField('GroupSerializer')
    games = DynamicRelationField('GameSerializer', many=True)
    coaches = DynamicRelationField('CoachSerializer', many=True)
    athletes = DynamicRelationField('AthleteSerializer', many=True)
    team_game_compositions = DynamicRelationField('TeamGameCompositionSerializer', many=True)


class RefereeSerializer(DynamicModelSerializer):

    class Meta:
        model = Referee
        name = 'referee'
        fields = (
            'user',
            'poor_eyesight',
            'games',
            'referee_game_compositions',
            'id'
        )
        deferred_fields = (
            'user',
            'games',
            'referee_game_compositions',
        )

    user = DynamicRelationField('UserSerializer')
    games = DynamicRelationField('GameSerializer', many=True)
    referee_game_compositions = DynamicRelationField('RefereeGameCompositionSerializer', many=True)


class CountrySerializer(DynamicModelSerializer):

    class Meta:
        model = Country
        name = 'country'
        plural_name = 'countries'
        fields = (
            'name',
            'population',
            'annual_gdp',
            'national_anthem_text',
            'team',
            'id'
        )
        deferred_fields = (
            'team',
        )

    team = DynamicRelationField('TeamSerializer')


class GroupSerializer(DynamicModelSerializer):

    class Meta:
        model = Group
        name = 'group'
        fields = (
            'name',
            'teams',
            'id'
        )
        deferred_fields = (
            'teams',
        )

    teams = DynamicRelationField('TeamSerializer', many=True)


class AthleteSerializer(DynamicModelSerializer):

    class Meta:
        model = Athlete
        name = 'athlete'
        fields = (
            'user',
            'team',
            'height',
            'weight',
            'id'
        )
        deferred_fields = (
            'user',
            'team',
        )

    user = DynamicRelationField('UserSerializer')
    team = DynamicRelationField('TeamSerializer')


class CoachSerializer(DynamicModelSerializer):

    class Meta:
        model = Coach
        name = 'coach'
        plural_name = 'coaches'
        fields = (
            'user',
            'team',
            'favorite_strategy',
            'id'
        )
        deferred_fields = (
            'user',
            'team',
        )

    user = DynamicRelationField('UserSerializer')
    team = DynamicRelationField('TeamSerializer')


class GameSerializer(DynamicModelSerializer):

    class Meta:
        model = Game
        name = 'game'
        fields = (
            'start_time',
            'id',
            'location',
            'teams',
            'referees',
            'team_game_compositions',
            'referee_game_compositions',
        )
        deferred_fields = (
            'teams',
            'referees',
            'team_game_compositions',
            'referee_game_compositions',
        )

    teams = DynamicRelationField('TeamSerializer', many=True)
    referees = DynamicRelationField('RefereeSerializer', many=True)
    team_game_compositions = DynamicRelationField('TeamGameCompositionSerializer', many=True)
    referee_game_compositions = DynamicRelationField('RefereeGameCompositionSerializer', many=True)


class TeamGameCompositionSerializer(DynamicModelSerializer):

    class Meta:
        model = TeamGameComposition
        name = 'team_game_composition'
        fields = (
            'id',
            'team',
            'game',
            'is_home',
            'result'
        )
        deferred_fields = (
            'team',
            'game',
        )

    team = DynamicRelationField('TeamSerializer')
    game = DynamicRelationField('GameSerializer')


class RefereeGameCompositionSerializer(DynamicModelSerializer):

    class Meta:
        model = RefereeGameComposition
        name = 'referee_game_composition'
        fields = (
            'id',
            'referee',
            'game',
            'position',
        )
        deferred_fields = (
            'referee',
            'game',
        )

    referee = DynamicRelationField('RefereeSerializer')
    game = DynamicRelationField('GameSerializer')


class UserSerializer(DynamicModelSerializer):

    class Meta:
        model = User
        name = 'user'
        fields = (
            'posts',
            'comments',
            'athlete',
            'coach',
            'referee',
            'date_joined',
            'email',
            'id',
            'is_active',
            'is_staff',
            'is_superuser',
            'first_name',
            'last_name',
            'username',
        )
        read_only_fields = (
            'date_joined',
            'id',
            'is_active',
            'is_staff',
            'is_superuser',
            'first_name',
            'last_name',
            'username',
        )
        deferred_fields = (
            'posts',
            'comments',
            'athlete',
            'coach',
            'referee',
        )

    posts = DynamicRelationField('PostSerializer', many=True)
    comments = DynamicRelationField('CommentSerializer', many=True)
    athlete = DynamicRelationField('AthleteSerializer')
    coach = DynamicRelationField('CoachSerializer')
    referee = DynamicRelationField('RefereeSerializer')
