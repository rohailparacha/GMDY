# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-26 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DataimportEntityimportrecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_source', models.CharField(max_length=20)),
                ('import_source_id', models.CharField(max_length=100)),
                ('entity_type', models.CharField(max_length=50)),
                ('entity_id', models.IntegerField()),
                ('memo', models.CharField(blank=True, max_length=5000, null=True)),
            ],
            options={
                'db_table': 'dataimport_entityimportrecord',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DataimportSportradargame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_id', models.CharField(max_length=100)),
                ('event_id', models.IntegerField()),
            ],
            options={
                'db_table': 'dataimport_sportradargame',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DataimportSportradarplayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_id', models.CharField(max_length=100)),
                ('athlete_id', models.IntegerField()),
            ],
            options={
                'db_table': 'dataimport_sportradarplayer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DataimportSportradarteam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_id', models.CharField(max_length=100)),
                ('team_id', models.IntegerField()),
            ],
            options={
                'db_table': 'dataimport_sportradarteam',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DataimportSportradarvenue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_id', models.CharField(max_length=100)),
                ('venue_id', models.IntegerField()),
            ],
            options={
                'db_table': 'dataimport_sportradarvenue',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainAffiliatenetwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('affiliate_network_id', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'main_affiliatenetwork',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainAthlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('popularity_ranking', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'main_athlete',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainAthleteimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'main_athleteimage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainAthletesocialchannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_type', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'main_athletesocialchannel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainAthleteteam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jersey_number', models.CharField(blank=True, max_length=20, null=True)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'main_athleteteam',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'main_brand',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'main_category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainDevicefollower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=255)),
                ('last_seen_datetime', models.DateTimeField()),
                ('created_datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'main_devicefollower',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'main_event',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainEventAthlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'main_event_athlete',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainEventparticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_type', models.CharField(max_length=50)),
                ('participant_role', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'main_eventparticipant',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainExternalcredentials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credentials_type', models.CharField(max_length=30)),
                ('host_name', models.CharField(max_length=100)),
                ('port', models.IntegerField(blank=True, null=True)),
                ('user_name', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('protocol', models.CharField(blank=True, max_length=100, null=True)),
                ('encryption', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'main_externalcredentials',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainFollowedathlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'main_followedathlete',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainFollowedproduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'main_followedproduct',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainFollowedteam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'main_followedteam',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainFollower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField()),
                ('last_seen_datetime', models.DateTimeField()),
                ('created_datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'main_follower',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=1000)),
                ('image_size', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'main_image',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('province', models.CharField(blank=True, max_length=100, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=100, null=True)),
                ('country_code', models.CharField(max_length=3)),
                ('longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True)),
            ],
            options={
                'db_table': 'main_location',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'main_organization',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('description', models.TextField(blank=True, null=True)),
                ('in_stock', models.BooleanField()),
                ('currency', models.CharField(blank=True, max_length=3, null=True)),
                ('ean', models.CharField(blank=True, max_length=15, null=True)),
                ('mpn', models.CharField(blank=True, max_length=1000, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('sku', models.CharField(blank=True, max_length=1000, null=True)),
                ('url', models.CharField(blank=True, max_length=3000, null=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('last_modified', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'main_product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainProductAthlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'main_product_athlete',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainProductEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'main_product_event',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainProductimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_order', models.IntegerField()),
            ],
            options={
                'db_table': 'main_productimage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainProductTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'main_product_team',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainRetailer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('commission', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('referral_url', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'main_retailer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('popularity_ranking', models.IntegerField(blank=True, null=True)),
                ('abbreviation', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'main_team',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainTeamimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'main_teamimage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainTeamlocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'main_teamlocation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainTeamsocialchannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_type', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'main_teamsocialchannel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainUseridentity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'main_useridentity',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainVenue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'main_venue',
                'managed': False,
            },
        ),
    ]
