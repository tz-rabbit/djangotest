from django.contrib import admin

# Register your models here.

from .models import UserProfile
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role','phone', 'bio','avatar','datetime','isok')
    # search_fields = ('title','explain','isok') #模糊搜索
    # list_filter = ('title', 'explain', 'details','datetime','isok') #字段搜索
admin.site.register(UserProfile, UserProfileAdmin)  # 向admin注册表