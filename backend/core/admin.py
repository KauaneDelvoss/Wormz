from django.contrib import admin

from core.models import Author, Book, Bookshelf, Genre, User, Review, Form, Question, Resolves, Answer, AnswerAssociativa


# Register your models here.

from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    #"nickname",
                    "email",
                    "genre_pref",
                    "user_biography",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Bookshelf)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Form)
admin.site.register(Resolves)
admin.site.register(AnswerAssociativa)


#admin.site.register(Own)
#admin.site.register(Type)
#admin.site.register(Writes)

