# Generated by Django 2.2.12 on 2020-06-01 20:26

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landingpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('two_columns', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], icon='arrow-right', label='Left column content')), ('right_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], icon='arrow-right', label='Right column content'))])), ('code', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('excerpt', wagtail.core.blocks.RichTextBlock())])), ('paragraph', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('excerpt', wagtail.core.blocks.RichTextBlock())])), ('code', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.core.blocks.TextBlock(identifier='code', label='Code'))], label='Code'))])), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(icon='media'))], blank=True, null=True),
        ),
    ]