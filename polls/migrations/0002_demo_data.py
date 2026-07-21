from django.contrib.auth.hashers import make_password
from django.db import migrations


def seed_demo_data(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Note = apps.get_model('polls', 'Note')

    bjorn, _ = User.objects.get_or_create(
        username='björn',
        defaults={'email': 'bjorn@example.com', 'password': make_password('password123')},
    )
    bob, _ = User.objects.get_or_create(
        username='bob',
        defaults={'email': 'bob@example.com', 'password': make_password('password123')},
    )

    Note.objects.get_or_create(owner=bjorn, title='Björn note 1', defaults={'body': 'Private note for Björn.'})
    Note.objects.get_or_create(owner=bjorn, title='Björn note 2', defaults={'body': 'Another Björn note.'})
    Note.objects.get_or_create(owner=bob, title='Bob note 1', defaults={'body': 'Private note for Bob.'})
    Note.objects.get_or_create(owner=bob, title='Bob note 2', defaults={'body': 'Another Bob note.'})


def unseed_demo_data(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Note = apps.get_model('polls', 'Note')

    Note.objects.filter(owner__username__in=['björn', 'bob']).delete()
    User.objects.filter(username__in=['björn', 'bob']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_demo_data, unseed_demo_data),
    ]