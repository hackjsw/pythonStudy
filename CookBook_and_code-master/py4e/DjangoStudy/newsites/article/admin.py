from django.contrib import admin
from .models import Article

# Register your models here.
@admin.register(Article)#ע�ᵽadmin
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content','author', 'is_deleted','created_time', 'last_updated_time')#��ʾ����
    ordering = ('id',)#����˳��
    pass

#admin.site.register(Article,ArticleAdmin)#ע�ᵽadmin