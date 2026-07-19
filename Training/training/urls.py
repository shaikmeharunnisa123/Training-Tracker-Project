from django.urls import (

    path,

    include

)


from rest_framework.routers import (

    DefaultRouter

)


from . import views


router = DefaultRouter()


router.register(

    "freshers",

    views.FresherAPI

)


router.register(

    "progress",

    views.ProgressAPI

)


router.register(

    "assignments",

    views.AssignmentAPI

)


router.register(

    "projects",

    views.ProjectAPI

)


urlpatterns = [

    path(

        "",

        views.login_page,

        name="login"

    ),


    path(

        "logout/",

        views.logout_page,

        name="logout"

    ),


    path(

        "dashboard/",

        views.dashboard,

        name="dashboard"

    ),


    path(

        "register/",

        views.register,

        name="register"

    ),


    path(

        "progress/",

        views.progress,

        name="progress"

    ),


    path(

        "assignment/",

        views.assignment,

        name="assignment"

    ),


    path(

        "project/",

        views.project,

        name="project"

    ),


    path(

        "api/",

        include(

            router.urls

        )

    ),

]
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


# Existing REST API router

router = DefaultRouter()


router.register(
    "freshers",
    views.FresherAPI
)


router.register(
    "progress",
    views.ProgressAPI
)


router.register(
    "assignments",
    views.AssignmentAPI
)


router.register(
    "projects",
    views.ProjectAPI
)


urlpatterns = [

    # Login page

    path(
        "",
        views.login_page,
        name="login"
    ),


    # Logout

    path(
        "logout/",
        views.logout_page,
        name="logout"
    ),


    # Dashboard

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),


    # Fresher registration page

    path(
        "register/",
        views.register,
        name="register"
    ),


    # Daily progress page

    path(
        "progress/",
        views.progress,
        name="progress"
    ),


    # Assignment page

    path(
        "assignment/",
        views.assignment,
        name="assignment"
    ),


    # Project tracker page

    path(
        "project/",
        views.project,
        name="project"
    ),


    # Existing Django REST Framework APIs

    path(
        "api/",
        include(router.urls)
    ),


    # New MongoDB API

    path(
        "api/mongo/freshers/",
        views.mongo_fresher_api,
        name="mongo-fresher-api"
    ),
    

]