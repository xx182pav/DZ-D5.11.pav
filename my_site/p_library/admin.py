from django.contrib import admin
from p_library.models import Book, Author, Redaction, Friend


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ['title', 'author_full_name',]
    fields = ['ISBN', 'title', 'description', 'year_release', 'author', 'price']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = ['full_name',]
    fields = ['full_name', 'birth_year', 'country',]

@admin.register(Redaction)
class RedactionAdmin(admin.ModelAdmin):
    pass
@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):

    list_display = ['friend_name',]
    fields = ['friend_name', 'borrowed_books',]
# Register your models here.