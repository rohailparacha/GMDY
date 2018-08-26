# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DataimportEntityimportrecord(models.Model):
    import_source = models.CharField(max_length=20)
    import_source_id = models.CharField(max_length=100)
    entity_type = models.CharField(max_length=50)
    entity_id = models.IntegerField()
    memo = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dataimport_entityimportrecord'


class DataimportSportradargame(models.Model):
    sr_id = models.CharField(max_length=100)
    event_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dataimport_sportradargame'


class DataimportSportradarplayer(models.Model):
    sr_id = models.CharField(max_length=100)
    athlete_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dataimport_sportradarplayer'


class DataimportSportradarteam(models.Model):
    sr_id = models.CharField(max_length=100)
    team_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dataimport_sportradarteam'


class DataimportSportradarvenue(models.Model):
    sr_id = models.CharField(max_length=100)
    venue_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dataimport_sportradarvenue'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MainAffiliatenetwork(models.Model):
    name = models.CharField(max_length=100)
    affiliate_network_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_affiliatenetwork'


class MainAthlete(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True, null=True)
    popularity_ranking = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_athlete'


class MainAthleteimage(models.Model):
    athlete = models.ForeignKey(MainAthlete, models.DO_NOTHING)
    image = models.ForeignKey('MainImage', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_athleteimage'


class MainAthletesocialchannel(models.Model):
    channel_type = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    athlete = models.ForeignKey(MainAthlete, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_athletesocialchannel'


class MainAthleteteam(models.Model):
    jersey_number = models.CharField(max_length=20, blank=True, null=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField(blank=True, null=True)
    athlete = models.ForeignKey(MainAthlete, models.DO_NOTHING)
    team = models.ForeignKey('MainTeam', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_athleteteam'


class MainBrand(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'main_brand'


class MainCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'main_category'


class MainDevicefollower(models.Model):
    device_id = models.CharField(max_length=255)
    last_seen_datetime = models.DateTimeField()
    follower = models.ForeignKey('MainFollower', models.DO_NOTHING)
    created_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'main_devicefollower'


class MainEvent(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True, null=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField(blank=True, null=True)
    venue = models.ForeignKey('MainVenue', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_event'


class MainEventAthlete(models.Model):
    event = models.ForeignKey(MainEvent, models.DO_NOTHING)
    athlete = models.ForeignKey(MainAthlete, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_event_athlete'
        unique_together = (('event', 'athlete'),)


class MainEventparticipant(models.Model):
    participant_type = models.CharField(max_length=50)
    participant_role = models.CharField(max_length=50)
    athlete = models.ForeignKey(MainAthlete, models.DO_NOTHING, blank=True, null=True)
    event = models.ForeignKey(MainEvent, models.DO_NOTHING)
    team = models.ForeignKey('MainTeam', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_eventparticipant'


class MainExternalcredentials(models.Model):
    credentials_type = models.CharField(max_length=30)
    host_name = models.CharField(max_length=100)
    port = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    protocol = models.CharField(max_length=100, blank=True, null=True)
    encryption = models.CharField(max_length=100, blank=True, null=True)
    affiliate_network = models.ForeignKey(MainAffiliatenetwork, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_externalcredentials'


class MainFollowedathlete(models.Model):
    athlete = models.ForeignKey(MainAthlete, models.DO_NOTHING)
    follower = models.ForeignKey('MainFollower', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_followedathlete'
        unique_together = (('follower', 'athlete'),)


class MainFollowedproduct(models.Model):
    product = models.ForeignKey('MainProduct', models.DO_NOTHING)
    follower = models.ForeignKey('MainFollower', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_followedproduct'
        unique_together = (('follower', 'product'),)


class MainFollowedteam(models.Model):
    team = models.ForeignKey('MainTeam', models.DO_NOTHING)
    follower = models.ForeignKey('MainFollower', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_followedteam'
        unique_together = (('follower', 'team'),)


class MainFollower(models.Model):
    guid = models.UUIDField()
    last_seen_datetime = models.DateTimeField()
    created_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'main_follower'


class MainImage(models.Model):
    url = models.CharField(max_length=1000)
    image_size = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'main_image'


class MainLocation(models.Model):
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=100, blank=True, null=True)
    country_code = models.CharField(max_length=3)
    longitude = models.DecimalField(max_digits=20, decimal_places=8, blank=True, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_location'


class MainOrganization(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'main_organization'


class MainProduct(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)
    in_stock = models.BooleanField()
    brand = models.ForeignKey(MainBrand, models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(MainCategory, models.DO_NOTHING, blank=True, null=True)
    retailer = models.ForeignKey('MainRetailer', models.DO_NOTHING, blank=True, null=True)
    currency = models.CharField(max_length=3, blank=True, null=True)
    ean = models.CharField(max_length=15, blank=True, null=True)
    mpn = models.CharField(max_length=1000, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    sku = models.CharField(max_length=1000, blank=True, null=True)
    url = models.CharField(max_length=3000, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_product'


class MainProductAthlete(models.Model):
    product = models.ForeignKey(MainProduct, models.DO_NOTHING)
    athlete = models.ForeignKey(MainAthlete, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_product_athlete'
        unique_together = (('product', 'athlete'),)


class MainProductEvent(models.Model):
    product = models.ForeignKey(MainProduct, models.DO_NOTHING)
    event = models.ForeignKey(MainEvent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_product_event'
        unique_together = (('product', 'event'),)


class MainProductTeam(models.Model):
    product = models.ForeignKey(MainProduct, models.DO_NOTHING)
    team = models.ForeignKey('MainTeam', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_product_team'
        unique_together = (('product', 'team'),)


class MainProductimage(models.Model):
    display_order = models.IntegerField()
    image = models.ForeignKey(MainImage, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(MainProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_productimage'


class MainRetailer(models.Model):
    name = models.CharField(max_length=100)
    affiliate_network = models.ForeignKey(MainAffiliatenetwork, models.DO_NOTHING, blank=True, null=True)
    commission = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    referral_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_retailer'


class MainTeam(models.Model):
    name = models.CharField(max_length=100)
    organization = models.ForeignKey(MainOrganization, models.DO_NOTHING)
    popularity_ranking = models.IntegerField(blank=True, null=True)
    abbreviation = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_team'


class MainTeamimage(models.Model):
    image = models.ForeignKey(MainImage, models.DO_NOTHING, blank=True, null=True)
    team = models.ForeignKey(MainTeam, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_teamimage'


class MainTeamlocation(models.Model):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField(blank=True, null=True)
    location = models.ForeignKey(MainLocation, models.DO_NOTHING, blank=True, null=True)
    team = models.ForeignKey(MainTeam, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_teamlocation'


class MainTeamsocialchannel(models.Model):
    channel_type = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    team = models.ForeignKey(MainTeam, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_teamsocialchannel'


class MainUseridentity(models.Model):
    facebook_id = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_useridentity'


class MainVenue(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True, null=True)
    location = models.ForeignKey(MainLocation, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_venue'
