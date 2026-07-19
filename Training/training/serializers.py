from rest_framework import serializers

from .models import (

    Fresher,

    DailyProgress,

    Assignment,

    Project

)


class FresherSerializer(

    serializers.ModelSerializer

):

    class Meta:

        model = Fresher

        fields = "__all__"



class ProgressSerializer(

    serializers.ModelSerializer

):

    class Meta:

        model = DailyProgress

        fields = "__all__"



class AssignmentSerializer(

    serializers.ModelSerializer

):

    class Meta:

        model = Assignment

        fields = "__all__"



class ProjectSerializer(

    serializers.ModelSerializer

):

    class Meta:

        model = Project

        fields = "__all__"