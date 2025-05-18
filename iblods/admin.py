from django.contrib import admin
from .models import category, Post
# Register your models here.



class categoryAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'Tittle', 'url', 'add_date')
    search_fields = ('Tittle',)
    list_filter = ('add_date',)
    list_per_page=5

class PostAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'Tittle', 'Content', 'url', 'cart')
    search_fields = ('Tittle',)
    list_filter = ('cart',)
    list_per_page=5

admin.site.register(category, categoryAdmin)
admin.site.register(Post, PostAdmin)