from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Teams
        teams = [
            {"name": "Marvel", "description": "Team Marvel Superheroes"},
            {"name": "DC", "description": "Team DC Superheroes"}
        ]
        db.teams.insert_many(teams)

        # Users
        users = [
            {"name": "Spider-Man", "email": "spiderman@marvel.com", "team": "Marvel"},
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
            {"name": "Batman", "email": "batman@dc.com", "team": "DC"}
        ]
        db.users.insert_many(users)

        # Activities
        activities = [
            {"user": "spiderman@marvel.com", "activity": "Running", "duration": 30},
            {"user": "ironman@marvel.com", "activity": "Cycling", "duration": 45},
            {"user": "wonderwoman@dc.com", "activity": "Swimming", "duration": 60},
            {"user": "batman@dc.com", "activity": "Yoga", "duration": 40}
        ]
        db.activities.insert_many(activities)

        # Workouts
        workouts = [
            {"name": "Cardio Blast", "suggested_for": "Marvel"},
            {"name": "Strength Builder", "suggested_for": "DC"}
        ]
        db.workouts.insert_many(workouts)

        # Leaderboard
        leaderboard = [
            {"user": "spiderman@marvel.com", "points": 100},
            {"user": "ironman@marvel.com", "points": 90},
            {"user": "wonderwoman@dc.com", "points": 110},
            {"user": "batman@dc.com", "points": 95}
        ]
        db.leaderboard.insert_many(leaderboard)

        # Ensure unique index on email
        db.users.create_index([("email", 1)], unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data!'))
