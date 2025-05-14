from django.db import migrations

def create_homepage(apps, schema_editor):
    Page = apps.get_model('content_pages', 'Page')
    Page.objects.create(
        title='Home',
        slug='home',
        content='Welcum.'
    )


class Migration(migrations.Migration):

    dependencies = [
        ('content_pages', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_homepage),
    ]
