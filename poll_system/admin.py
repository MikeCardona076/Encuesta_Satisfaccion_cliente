from django.contrib import admin
from .models import Test
from import_export import resources
from import_export.admin import ImportExportModelAdmin



# Register your models here.
class PollResource(resources.ModelResource):
    class Meta:
        model = Test
        skip_unchanged = True
        report_skipped = False
        fields = ('id', 
        'question1',
        'question2',
        'question3',
        'question4',
        'question5',
        'question6', 
        'question7',
        'sexo',
        'edad',
        'option1'
        ,
        'option2')

class TestAdmin(ImportExportModelAdmin):
    resource_class = PollResource
 

admin.site.register(Test,TestAdmin)