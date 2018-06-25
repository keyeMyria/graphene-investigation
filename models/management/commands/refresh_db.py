from datetime import datetime
from random import randint, choice, random, sample
import string
import time
import pytz

from django.core.management import call_command
from django.core.management.base import BaseCommand

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


class Command(BaseCommand):
    help = 'Completely refreshes the database with new data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('THIS WIPES ALL THE DATA FROM THE DATABASE'))
        self.stdout.write(self.style.NOTICE('WIPING DATA NOW'))
        call_command('flush')

        self.stdout.write(self.style.SUCCESS('Creating data'))

        # create 48 countries
        self.stdout.write(self.style.SUCCESS('Creating countries'))
        countries = []
        for num in range(48):
            digits = "".join( [choice(string.digits) for i in range(100)] )
            chars = "".join( [choice(string.ascii_letters) for i in range(150)] )

            country = Country.objects.create(
                name='Country_{0}'.format(num + 1),
                population=randint(10000000, 200000000),
                annual_gdp=randint(200000000000, 2000000000000),
                national_anthem_text=digits + chars
            )
            countries.append(country)

        # create 12 groups
        self.stdout.write(self.style.SUCCESS('Creating groups'))
        groups = []
        for letter in 'ABCDEFGHJIKL':
            group = Group.objects.create(name='GROUP_{0}'.format(letter))
            groups.append(group)


        # create 48 teams. 4 teams in each group
        self.stdout.write(self.style.SUCCESS('Creating teams'))
        teams = []
        for index, country in enumerate(countries):
            group_index = int(index / 4)
            team = Team.objects.create(
                counry=country,
                group=groups[group_index],
                ranking=index + 1
            )
            teams.append(team)

        # create 72 games (each team plays all the other teams in their group)
        # that's 6 games per group * 12 groups
        self.stdout.write(self.style.SUCCESS('Creating games'))
        games = []
        locs = ['Big Stadium', 'Small Stadium', 'Rowdy Stadium', 'Quiet Stadium']
        for num in range(72):
            game = Game.objects.create(
                start_time=randomDate("2018-06-14 07:00", "2018-07-21 21:00", random()),
                location=locs[num % 4]
            )
            games.append(game)

        # associate each team with a game. 72 games so 144 team_game_compositions
        self.stdout.write(self.style.SUCCESS('Creating team-game-compositions'))
        game_counter = 0
        for index, group in enumerate(groups):
            # for each group, create all the comps
            # 6 games in a group. so creat 2 TeamGameCompositions 6 times

            game_mapping = [[0, 1], [2, 3], [0, 2], [1, 3], [0, 3], [1, 2]]
            teams = group.teams.all() # 4 teams
            for game_num in range(6):
                game_map = game_mapping[game_num]
                TeamGameComposition.objects.create(
                    team=teams[game_map[0]],
                    game=games[game_counter],
                    is_home=True,
                    result=TeamGameComposition.WIN
                )
                TeamGameComposition.objects.create(
                    team=teams[game_map[1]],
                    game=games[game_counter],
                    is_home=False,
                    result=TeamGameComposition.LOSE
                )
                game_counter += 1

        # create users.
        # (11 athletes + 1 coach per team) * 48 teams + 10 referess == 586 users
        self.stdout.write(self.style.SUCCESS('Creating users'))
        users = []
        NUM_USERS = 586
        for num in range(NUM_USERS):
            user = User.objects.create_user('user_{0}'.format(num + 1))
            users.append(user)

        # create athletes. 11 athletes per team
        self.stdout.write(self.style.SUCCESS('Creating athlets'))
        user_index = 0
        for team_index, team in enumerate(teams):
            for num in range(11):
                user_index = team_index * 12 + num
                Athlete.objects.create(
                    user=users[user_index],
                    team=team,
                    height=randint(68, 78),
                    weight=randint(175, 250)
                )

        # create coaches. 1 coach per team
        self.stdout.write(self.style.SUCCESS('Creating coaches'))
        for team in teams:
            user_index += 1
            random_strat_index = randint(0, 2)
            Coach.objects.create(
                user=users[user_index],
                team=team,
                favorite_strategy=Coach.FAVORITE_STRATEGY_CHOICES[random_strat_index][0]
            )

        # create 10 referees
        self.stdout.write(self.style.SUCCESS('Creating referees'))
        referees = []
        for num in range(10):
            user_index += 1
            referee = Referee.objects.create(
                user=users[user_index]
            )
            referees.append(referee)

        # create the referee_game_compositions
        # loop through each game and create 3 compositions for each game
        self.stdout.write(self.style.SUCCESS('Creating referee-game-compostions'))
        for game in games:
            refs_for_game = sample(referees, 3)
            for index in range(3):
                RefereeGameComposition.objects.create(
                    referee=refs_for_game[index],
                    game=game,
                    position=RefereeGameComposition.REFEREE_POSITIONS[index][0]
                )

        # create 10 random tags
        self.stdout.write(self.style.SUCCESS('Creating tags'))
        tags = []
        for index in range(10):
            name = "".join( [choice(string.ascii_letters) for i in range(100)] )
            tag = Tag.objects.create(name=name)
            tags.append(tag)

        # create 75 blog posts
        self.stdout.write(self.style.SUCCESS('Creating posts'))
        posts = []
        for index in range(75):
            tags_to_choose = sample(tags, 3)
            post = Post.objects.create(
                author=users[randint(0, NUM_USERS - 1)],
                post_date=randomDate("2018-06-14 07:00", "2018-07-21 21:00", random()),
                title="".join( [choice(string.ascii_letters) for i in range(10)] ),
                text="".join( [choice(string.ascii_letters) for i in range(100)] )
            )
            post.tags.add(tags_to_choose[0], tags_to_choose[1], tags_to_choose[2])
            posts.append(post)

        # create 3 comments for each post
        self.stdout.write(self.style.SUCCESS('Creating comments'))
        for post in posts:
            for index in range(3):
                Comment.objects.create(
                    post=post,
                    creator=users[randint(0, NUM_USERS - 1)],
                    bodytext="".join( [choice(string.ascii_letters) for i in range(55)] ),
                    post_date=randomDate("2018-06-14 07:00", "2018-07-21 21:00", random())
                )


def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in datetime
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)
    local_tz = pytz.timezone("US/Pacific")
    utc_dt = datetime.utcfromtimestamp(ptime).replace(tzinfo=pytz.utc)
    local_dt = local_tz.normalize(utc_dt.astimezone(local_tz))
    return local_dt

def randomDate(start, end, prop):
    return strTimeProp(start, end, '%Y-%m-%d %H:%M', prop)
