from django.contrib import admin
from .models import Tags, Pattern, Group, Sentence, Verb, Resource, Artefact
# Register your models here.

class TagsAdmin(admin.ModelAdmin):
    pass

class PatternAdmin(admin.ModelAdmin):
    pass

class GroupAdmin(admin.ModelAdmin):
    pass

class SetenceAdmin(admin.ModelAdmin):
    pass

class VerbAdmin(admin.ModelAdmin):
    pass

class ResourceAdmin(admin.ModelAdmin):
    pass
 
class ArtefactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tags, TagsAdmin)
admin.site.register(Pattern, PatternAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Verb, VerbAdmin)
admin.site.register(Sentence, SetenceAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Artefact, ArtefactAdmin)
