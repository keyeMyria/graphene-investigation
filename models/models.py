from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    tags = models.ManyToManyField('Tag', related_name='posts')
    title = models.CharField(max_length=200)
    text = models.TextField()
    post_date = models.DateTimeField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        'Post',
        related_name='comments',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    creator = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    bodytext = models.TextField()
    post_date = models.DateTimeField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bodytext


class Tag(models.Model):
    name = models.CharField(max_length=128)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class Team(models.Model):
    counry = models.OneToOneField(
        'Country',
        related_name='team',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    group = models.ForeignKey(
        'group',
        related_name='teams',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    ranking = models.PositiveSmallIntegerField()
    games = models.ManyToManyField('Game', through='TeamGameComposition')


class Referee(models.Model):
    user = models.OneToOneField(
        User,
        related_name='referee',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    poor_eyesight = models.BooleanField(default=True)
    games = models.ManyToManyField('Game', through='RefereeGameComposition')


class Country(models.Model):
    name = models.CharField(max_length=128)
    population = models.PositiveIntegerField()
    annual_gdp = models.BigIntegerField()
    national_anthem_text = models.TextField()


class Group(models.Model):
    GROUP_A = 'GROUP_A'
    GROUP_B = 'GROUP_B'
    GROUP_C = 'GROUP_C'
    GROUP_D = 'GROUP_D'
    GROUP_E = 'GROUP_E'
    GROUP_F = 'GROUP_F'
    GROUP_G = 'GROUP_G'
    GROUP_H = 'GROUP_H'
    GROUP_I = 'GROUP_I'
    GROUP_J = 'GROUP_J'
    GROUP_K = 'GROUP_K'
    GROUP_L = 'GROUP_L'
    GROUP_NAMES = (
        (GROUP_A, 'Group A'),
        (GROUP_B, 'Group B'),
        (GROUP_C, 'Group C'),
        (GROUP_D, 'Group D'),
        (GROUP_E, 'Group E'),
        (GROUP_F, 'Group F'),
        (GROUP_G, 'Group G'),
        (GROUP_H, 'Group H'),
        (GROUP_I, 'Group I'),
        (GROUP_J, 'Group J'),
        (GROUP_K, 'Group K'),
        (GROUP_L, 'Group L'),
    )
    name = models.CharField(choices=GROUP_NAMES, max_length=7)


class Athlete(models.Model):
    user = models.OneToOneField(
        User,
        related_name='athlete',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    team = models.ForeignKey(
        'Team',
        related_name='athletes',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
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

    user = models.OneToOneField(
        User,
        related_name='coach',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    team = models.ForeignKey(
        'Team',
        related_name='coaches',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    favorite_strategy = models.CharField(
        choices=FAVORITE_STRATEGY_CHOICES,
        default=FOUR_FOUR_TWO,
        max_length=20
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
    team = models.ForeignKey(
        'Team',
        related_name='team_game_compositions',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    game = models.ForeignKey(
        'Game',
        related_name='team_game_compositions',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    is_home = models.BooleanField(default=False)
    result = models.CharField(
        null=True,
        blank=True,
        choices=RESULT_CHOICES,
        max_length=5
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
    referee = models.ForeignKey(
        'Referee',
        related_name='referee_game_compositions',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    game = models.ForeignKey(
        'Game',
        related_name='referee_game_compositions',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    position = models.CharField(
        choices=REFEREE_POSITIONS,
        default=MAIN,
        max_length=15
    )

