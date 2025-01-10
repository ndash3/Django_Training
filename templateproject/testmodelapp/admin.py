from django.contrib import admin
from testmodelapp.models import StudentModel

# admin.site.register(StudentModel)
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'roll', 'mark', 'name_length', 'is_student_pass')
    search_fields = ('name',)
    list_filter = ('name', 'age')
    ordering = ('-mark',)
    list_editable = ('mark',)


    def name_length(self, obj):
        return len((obj.name))

    def is_student_pass(self, obj):
        return obj.mark > 300


admin.site.register(StudentModel, StudentAdmin)
