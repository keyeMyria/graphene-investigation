from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', related_name='posts')
    tags = models.ManyToManyField('Tag', related_name='posts')
    title = models.CharField(max_length=200)
    text = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments')
    creator = models.ForeignKey('auth.User', related_name='comments')
    bodytext = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bodytext


class Tag(models.Model):
    name = models.CharField(max_length=128)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class Team(models.Model):
    counry = models.OneToOneField('Country', related_name='team')
    group = models.ForeignKey('group', related_name='teams')
    ranking = models.PositiveSmallIntegerField()
    games = models.ManyToManyField('Game', through='TeamGameComposition')


class Referee(models.Model):
    user = models.OneToOneField('auth.User', related_name='referee')
    poor_eyesight = models.BooleanField(default=True)
    games = models.ManyToManyField('Game', through='RefereeGameComposition')


class Country(models.model):
    name = models.CharField(max_length=128)
    population = models.PositiveIntegerField()
    annual_gdp = models.BigIntegerField()
    national_anthem_text = models.TextField()


class Group(models.model):
    GROUP_A = 'GROUP_A'
    GROUP_B = 'GROUP_B'
    GROUP_C = 'GROUP_C'
    GROUP_D = 'GROUP_D'
    GROUP_E = 'GROUP_E'
    GROUP_F = 'GROUP_F'
    GROUP_NAMES = (
        (GROUP_A, 'Group A'),
        (GROUP_B, 'Group B'),
        (GROUP_C, 'Group C'),
        (GROUP_D, 'Group D'),
        (GROUP_E, 'Group E'),
        (GROUP_F, 'Group F'),
    )
    name = models.CharField(choices=GROUP_NAMES)


class Athlete(models.Model):
    user = models.OneToOneField('auth.User', related_name='athlete')
    team = models.ForeignKey('Team', related_name='athletes')
    height = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()


class Coach(models.Model):
    FOUR_FOUR_TWO = 'FOUR_FOUR_TWO'
    FIVE_FOUR_ONE = 'FIVE_THREE_ONE'
    FIVE_THREE_TWO = 'FIVE_THREE_TWO'
    FAVORITE_STRATEGY_CHOICES = (
        (FOUR_FOUR_TWO, 'Four Four Two'),
        (FIVE_FOUR_ONE, 'Five Four One'),
        (FIVE_THREE_TWO, 'Five Three Two'),
    )

    user = models.OneToOneField('auth.User', related_name='coach')
    team = models.ForeignKey('Team', related_name='coaches')
    favorite_strategy = models.CharField(
        choices=FAVORITE_STRATEGY_CHOICES,
        default=FOUR_FOUR_TWO,
    )


class Game(models.Model):
    start_time = models.DateTimeField()
    location = models.TextField()


class TeamGameComposition(models.Model):
    WIN = 'WIN'
    LOSE = 'LOSE'
    DRAW = 'DRAW'
    RESULT_CHOICES = (
        (WIN, 'Win'),
        (LOSE, 'Lose'),
        (DRAW, 'Draw'),
    )
    team = models.ForeignKey('Team', related_name='team_game_compositions')
    game = models.ForeignKey('Game', related_name='team_game_compositions')
    is_home = models.BooleanField(default=False)
    result = models.CharField(
        null=True,
        blank=True,
        choices=RESULT_CHOICES
    )


class RefereeGameComposition(models.Model):
    MAIN = 'MAIN'
    ASSISTANT = 'ASSISTANT'
    GOAL_LINE = 'GOAL_LINE'
    REFEREE_POSITIONS = (
        (MAIN, 'Main'),
        (ASSISTANT, 'Assistant'),
        (GOAL_LINE, 'Goal Line'),
    )
    referee = models.ForeignKey('Referee', related_name='referee_game_compositions')
    game = models.ForeignKey('Game', related_name='referee_game_compositions')
    position = models.CharField(
        choices=REFEREE_POSITIONS,
        default=MAIN,
    )

