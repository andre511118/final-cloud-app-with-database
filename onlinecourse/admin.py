from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 3


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'grade']
    inlines = [ChoiceInline]
    

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text', 'is_correct']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
