# Generated by Django 2.1.4 on 2019-02-13 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='balans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo', models.FloatField(default=0, verbose_name='saldo')),
                ('comment', models.CharField(max_length=100, null=True)),
                ('date', models.DateField()),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Comercial',
            fields=[
                ('contract', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='О/Р')),
                ('name', models.CharField(max_length=100, verbose_name='Споживач')),
                ('ipn', models.CharField(max_length=20, null=True, verbose_name='ІПН')),
                ('meter_sn', models.CharField(blank=True, max_length=20, null=True, verbose_name='Лічильник №:')),
                ('phone_num', models.CharField(blank=True, max_length=13, null=True, verbose_name='Ном.телефону')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Ел. поштова скринька')),
            ],
            options={
                'ordering': ['account'],
            },
        ),
        migrations.CreateModel(
            name='gadget_hw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50, null=True)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Comercial')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='gadget_HW_meter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kWh', models.FloatField(default=0, verbose_name='кВт')),
                ('kVArh_p', models.FloatField(default=0, verbose_name='кВар поз.')),
                ('kVArh_n', models.FloatField(default=0, verbose_name='кВар нег.')),
                ('kVAh', models.FloatField(default=0, verbose_name='кВА')),
                ('cur_sum_V', models.FloatField(default=0, verbose_name='В')),
                ('cur_L1_V', models.FloatField(default=0, verbose_name='В Ф1')),
                ('cur_L2_V', models.FloatField(default=0, verbose_name='В Ф2')),
                ('cur_L3_V', models.FloatField(default=0, verbose_name='В Ф3')),
                ('cur_F', models.FloatField(default=0, verbose_name='Частота')),
                ('meterDate', models.BigIntegerField(default=0, verbose_name='Дата')),
                ('gadget_HW_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.gadget_hw', verbose_name='№ пристрою')),
            ],
            options={
                'ordering': ['meterDate'],
            },
        ),
        migrations.CreateModel(
            name='gadget_HW_meter_max_dem_h',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kW', models.FloatField(default=0, verbose_name='макс.кВт')),
                ('meterDate', models.BigIntegerField(default=0, verbose_name='Дата')),
                ('gadget_HW_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.gadget_hw', verbose_name='№ пристрою')),
            ],
            options={
                'ordering': ['meterDate'],
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=5, unique=True)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='meterDataPrivate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokazT0', models.FloatField(default='0.0', verbose_name='показник')),
                ('pokazT1', models.FloatField(default='0.0', verbose_name='показник')),
                ('pokazT2', models.FloatField(default='0.0', verbose_name='показник')),
                ('pokazT3', models.FloatField(default='0.0', verbose_name='показник')),
                ('date', models.DateField(verbose_name='Дата')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Private_abonent',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='О/Р')),
                ('first_name', models.CharField(max_length=20, verbose_name="Ім'я")),
                ('last_name', models.CharField(max_length=20, verbose_name='Побатькові')),
                ('sur_name', models.CharField(max_length=30, verbose_name='Прізвище')),
                ('apartament', models.IntegerField(default=0, null=True, verbose_name='Квартира')),
                ('meter_sn', models.CharField(blank=True, max_length=20, null=True, verbose_name='Лічильник №:')),
                ('phone_num', models.CharField(blank=True, max_length=13, null=True, verbose_name='Ном.телефону')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Ел. поштова скринька')),
                ('house_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='user.House', to_field='number', verbose_name='Будинок')),
            ],
            options={
                'ordering': ['account'],
            },
        ),
        migrations.CreateModel(
            name='Privelege',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privelege', models.CharField(max_length=20, verbose_name='Пільга')),
                ('limit', models.IntegerField(verbose_name='Ліміт пільг.споживання')),
                ('limit_price', models.FloatField(verbose_name='пільгова ціна')),
                ('price', models.FloatField(verbose_name='ціна')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='spozHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='місяць')),
                ('pokaz1', models.FloatField(default=0, verbose_name='поч.показник')),
                ('pokaz2', models.FloatField(default=0, verbose_name='кін.показник')),
                ('different', models.FloatField(default=0, verbose_name='спожито кВт')),
                ('uah', models.FloatField(default=0, verbose_name='грн')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'ordering': ['street_name'],
            },
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('town_name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'ordering': ['town_name'],
            },
        ),
        migrations.AddField(
            model_name='street',
            name='town',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='user.Town', to_field='town_name'),
        ),
        migrations.AddField(
            model_name='private_abonent',
            name='tariff',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.Privelege', verbose_name='Тариф'),
        ),
        migrations.AddField(
            model_name='meterdataprivate',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Private_abonent'),
        ),
        migrations.AddField(
            model_name='house',
            name='street',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='user.Street', to_field='street_name'),
        ),
        migrations.AddField(
            model_name='comercial',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='balans',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
