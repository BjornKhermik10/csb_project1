from django.db import migrations


def forwards(apps, schema_editor):
    Note = apps.get_model('polls', 'Note')

    Note.objects.filter(id=1).update(title='Björn note 1', body='Private note for Björn.')
    Note.objects.filter(id=2).update(title='Björn note 2', body='Another Björn note.')


def backwards(apps, schema_editor):
    Note = apps.get_model('polls', 'Note')

    Note.objects.filter(title='Björn note 1').update(title='Bjorn note 1', body='Private note for Bjorn.')
    Note.objects.filter(title='Björn note 2').update(title='Bjorn note 2', body='Another Bjorn note.')


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_rename_bjorn_demo_user'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]