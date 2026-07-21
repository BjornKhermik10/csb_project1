from django.db import migrations


def forwards(apps, schema_editor):
    return


def backwards(apps, schema_editor):
    return


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_demo_data'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]