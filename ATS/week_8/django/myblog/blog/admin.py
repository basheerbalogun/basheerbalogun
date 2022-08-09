from django.contrib import admin
from .models import Post,CommentPost,Profile,Author

# Register your models here.


admin.site.register(Post)
admin.site.register(CommentPost)
admin.site.register(Profile)
admin.site.register(Author)