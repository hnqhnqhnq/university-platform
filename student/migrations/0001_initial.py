# Generated by Django 3.2.12 on 2023-12-08 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('activity_id', models.IntegerField(primary_key=True, serialize=False)),
                ('activity_type', models.CharField(blank=True, max_length=20, null=True)),
                ('activity_start_date', models.DateTimeField(blank=True, null=True)),
                ('activity_end_date', models.DateTimeField(blank=True, null=True)),
                ('activity_max_students', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Activities',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Activityassignments',
            fields=[
                ('assignment_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'ActivityAssignments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Authentications',
            fields=[
                ('authentication_id', models.AutoField(primary_key=True, serialize=False)),
                ('authentication_username', models.CharField(max_length=15, unique=True)),
                ('authentication_password', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'Authentications',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
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
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('course_id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(blank=True, max_length=15, null=True)),
                ('course_description', models.CharField(blank=True, max_length=100, null=True)),
                ('course_max_students', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Courses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
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
            name='Enrollments',
            fields=[
                ('enrollment_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Enrollments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('grade_id', models.IntegerField(primary_key=True, serialize=False)),
                ('grade_course', models.IntegerField(blank=True, null=True)),
                ('grade_laboratory', models.IntegerField(blank=True, null=True)),
                ('grade_seminar', models.IntegerField(blank=True, null=True)),
                ('grade_final', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Grades',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Groupactivities',
            fields=[
                ('activity_id', models.AutoField(primary_key=True, serialize=False)),
                ('activity_name', models.CharField(blank=True, max_length=50, null=True)),
                ('activity_date', models.DateTimeField(blank=True, null=True)),
                ('activity_duration', models.IntegerField(blank=True, null=True)),
                ('min_participants', models.IntegerField(blank=True, null=True)),
                ('expiration_time', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'GroupActivities',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Groupactivityregistrations',
            fields=[
                ('registration_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'GroupActivityRegistrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Groupmembers',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'GroupMembers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Groupmessages',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('message_context', models.CharField(blank=True, max_length=255, null=True)),
                ('message_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'GroupMessages',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Laboratories',
            fields=[
                ('laboratory_id', models.IntegerField(primary_key=True, serialize=False)),
                ('laboratory_name', models.CharField(blank=True, max_length=15, null=True)),
                ('laboratory_description', models.CharField(blank=True, max_length=100, null=True)),
                ('laboratory_max_students', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Laboratories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seminars',
            fields=[
                ('seminar_id', models.IntegerField(primary_key=True, serialize=False)),
                ('seminar_name', models.CharField(blank=True, max_length=15, null=True)),
                ('seminar_description', models.CharField(blank=True, max_length=100, null=True)),
                ('seminar_max_students', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Seminars',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Studygroups',
            fields=[
                ('group_id', models.AutoField(primary_key=True, serialize=False)),
                ('group_name', models.CharField(blank=True, max_length=30, null=True)),
                ('group_description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'StudyGroups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_pic', models.CharField(db_column='user_PIC', max_length=20, unique=True)),
                ('user_first_name', models.CharField(max_length=20)),
                ('user_last_name', models.CharField(max_length=20)),
                ('user_address', models.CharField(max_length=50)),
                ('user_phone_number', models.CharField(max_length=20, unique=True)),
                ('user_email', models.CharField(max_length=50)),
                ('user_iban', models.CharField(db_column='user_IBAN', max_length=30, unique=True)),
                ('user_contract_number', models.IntegerField(unique=True)),
                ('user_type', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'Users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='student.users')),
            ],
            options={
                'db_table': 'Admins',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='student.users')),
                ('student_study_year', models.IntegerField()),
                ('student_hours', models.IntegerField()),
            ],
            options={
                'db_table': 'Students',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Superadmins',
            fields=[
                ('super_admin', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='student.users')),
            ],
            options={
                'db_table': 'SuperAdmins',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='student.users')),
                ('teacher_department', models.CharField(max_length=30)),
                ('teacher_min_hours', models.IntegerField()),
                ('teacher_max_hours', models.IntegerField()),
            ],
            options={
                'db_table': 'Teachers',
                'managed': False,
            },
        ),
    ]