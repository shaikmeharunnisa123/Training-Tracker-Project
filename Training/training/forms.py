from django.forms import ModelForm

from .models import (

    Fresher,

    DailyProgress,

    Assignment,

    Project

)


class FresherForm(ModelForm):

    class Meta:

        model = Fresher

        fields = "__all__"



class ProgressForm(ModelForm):

    class Meta:

        model = DailyProgress

        fields = "__all__"



class AssignmentForm(ModelForm):

    class Meta:

        model = Assignment

        fields = "__all__"



class ProjectForm(ModelForm):

    class Meta:

        model = Project

        fields = "__all__"