# Generated by Django 4.1.1 on 2022-10-20 02:37

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "cod_user",
                    models.AutoField(default=None, primary_key=True, serialize=False),
                ),
                ("nickname", models.CharField(max_length=50, unique=True)),
                ("email", models.EmailField(max_length=50)),
                ("genre_pref", models.CharField(max_length=50)),
                ("user_biography", models.TextField(max_length=2000)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name_plural": "Users",
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Author",
            fields=[
                ("name_author", models.CharField(max_length=100)),
                ("author_biography", models.CharField(max_length=2000)),
                ("cod_author", models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                "verbose_name_plural": "Authors",
            },
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                ("resume", models.CharField(max_length=2000, null=True)),
                ("name_book", models.CharField(max_length=100)),
                ("cod_book", models.AutoField(primary_key=True, serialize=False)),
                ("pages", models.IntegerField(null=True)),
            ],
            options={
                "verbose_name_plural": "Books",
            },
        ),
        migrations.CreateModel(
            name="Bookshelf",
            fields=[
                ("bookshelf_name", models.CharField(max_length=100)),
                ("booshelf_desc", models.CharField(max_length=500, null=True)),
                ("cod_bookshelf", models.AutoField(primary_key=True, serialize=False)),
                (
                    "cod_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Bookshelf",
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                ("name_genre", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=500)),
                ("cod_genre", models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                "verbose_name_plural": "Genres",
            },
        ),
        migrations.CreateModel(
            name="Writes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cod_author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="core.author"
                    ),
                ),
                (
                    "cod_book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="core.book"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Writes",
            },
        ),
        migrations.CreateModel(
            name="Type",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cod_book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="core.book"
                    ),
                ),
                (
                    "cood_genre",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="core.genre"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Type",
            },
        ),
        migrations.CreateModel(
            name="Own",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cod_book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="core.book"
                    ),
                ),
                (
                    "cod_bookshelf",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="core.bookshelf"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Own",
            },
        ),
        migrations.AddField(
            model_name="user",
            name="cod_bookshelf",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="core.bookshelf",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
    ]
