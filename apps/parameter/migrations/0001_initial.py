# Generated by Django 3.1 on 2022-10-10 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, null=True, verbose_name='Başlık')),
                ('rewrite', models.CharField(blank=True, max_length=200, null=True, verbose_name='Kısaltması')),
                ('area_code', models.IntegerField(blank=True, null=True, verbose_name='Alan Kodu')),
                ('alignment', models.IntegerField(blank=True, null=True, verbose_name='Sıralama')),
            ],
            options={
                'verbose_name': 'Ülke',
                'verbose_name_plural': 'Ülke',
                'ordering': ('text',),
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('text', models.CharField(max_length=200, null=True, verbose_name='Başlık')),
            ],
            options={
                'verbose_name': 'İcon',
                'verbose_name_plural': 'İcon',
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='MenuType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('text', models.CharField(max_length=200, null=True, verbose_name='Başlık')),
            ],
            options={
                'verbose_name': 'Menü Tipi',
                'verbose_name_plural': 'Menü Tipi',
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('text', models.CharField(max_length=200, null=True, verbose_name='Başlık')),
                ('mini_text', models.CharField(blank=True, max_length=250, verbose_name='Mini Üst Başlık')),
                ('button_text', models.CharField(blank=True, max_length=250, verbose_name='Button Yazısı')),
                ('button_link', models.CharField(blank=True, max_length=250, null=True, verbose_name='Button Link')),
                ('active', models.BooleanField(blank=True, null=True, verbose_name='Sayfada Görünsün')),
                ('alignment', models.IntegerField(blank=True, null=True, unique=True, verbose_name='Sıralama')),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Slider',
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('text', models.CharField(blank=True, max_length=400, verbose_name='Firma Adı')),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='sites.site', verbose_name='Site')),
            ],
            options={
                'verbose_name': 'Site Ayarları',
                'verbose_name_plural': 'Site Ayarları',
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, null=True, verbose_name='Başlık')),
                ('code', models.CharField(max_length=15, null=True, verbose_name='İl Kodu')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parameter.country', verbose_name='Ülke')),
            ],
            options={
                'verbose_name': 'İl',
                'verbose_name_plural': 'İl',
                'ordering': ('text',),
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Başlık')),
                ('link', models.CharField(blank=True, max_length=200, null=True, verbose_name='Link')),
                ('alignment', models.IntegerField(blank=True, null=True, verbose_name='Sıralama')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('menu_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='parameter.menutype', verbose_name='Menü Tipi')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='parameter.menu', verbose_name='Üst Menü')),
            ],
            options={
                'verbose_name': 'Menü',
                'verbose_name_plural': 'Menü',
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('text', models.CharField(max_length=200, null=True, verbose_name='Başlık')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parameter.province', verbose_name='İl')),
            ],
            options={
                'verbose_name': 'İlçe',
                'verbose_name_plural': 'İlçe',
                'ordering': ('text',),
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
    ]