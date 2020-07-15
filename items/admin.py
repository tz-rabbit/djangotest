from django.contrib import admin
from .models import ItemInfo,PartInfo,ProblemInfo,AnswerInfo
# Register your models here.
class ItemInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','title', 'explain', 'details','datetime','isok')
    search_fields = ('title','explain','isok') #模糊搜索
    list_filter = ('title', 'explain', 'details','datetime','isok') #字段搜索

class PartInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'name', 'skill','experience','requirement','datetime','isok')

class ProblemInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'questioner', 'problem', 'datetime', 'isok')

class AnswerInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'problem', 'respondent', 'answer', 'datetime', 'isok')


admin.site.register(ItemInfo,ItemInfoAdmin)#向admin注册表
admin.site.register(PartInfo,PartInfoAdmin)
admin.site.register(ProblemInfo,ProblemInfoAdmin)
admin.site.register(AnswerInfo,AnswerInfoAdmin)
admin.site.site_header = '管理'#修改admin一些显示
admin.site.site_title = '后台管理'
admin.site.index_title = '后台管理'
