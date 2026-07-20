# DJANGO IMPORTS


from django.shortcuts import (
    render,
    redirect,
)

from django.contrib.auth import (
    authenticate,
    login,
    logout,
)

from django.contrib.auth.decorators import (
    login_required,
)


# DJANGO REST FRAMEWORK IMPORTS

from rest_framework import (
    viewsets,
    status,
)

from rest_framework.decorators import (
    api_view,
)

from rest_framework.response import (
    Response,
)


# MODEL IMPORTS

from .models import (
    Fresher,
    DailyProgress,
    Assignment,
    Project,
)


# FORM IMPORTS

from .forms import (
    FresherForm,
    ProgressForm,
    AssignmentForm,
    ProjectForm,
)


# SERIALIZER IMPORTS

from .serializers import (
    FresherSerializer,
    ProgressSerializer,
    AssignmentSerializer,
    ProjectSerializer,
)


# MONGODB IMPORT

from .mongodb import (
    freshers_collection,
    progress_collection,
    assignments_collection,
    projects_collection,
)


# ==================================
# LOGIN
# ==================================

def login_page(request):

    message = ""

    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        password = request.POST.get(
            "password"
        )

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:

            login(
                request,
                user,
            )

            return redirect(
                "dashboard"
            )

        message = (
            "Invalid username or password"
        )

    return render(
        request,
        "login.html",
        {
            "message": message
        },
    )


# ==================================
# LOGOUT
# ==================================

def logout_page(request):

    logout(request)

    return redirect(
        "login"
    )


# ==================================
# DASHBOARD
# ==================================

@login_required
def dashboard(request):

    data = {

        "freshers":
            freshers_collection.count_documents({}),

        "progress":
            DailyProgress.objects.count(),

        "assignments":
            Assignment.objects.count(),

        "projects":
            Project.objects.count(),

    }

    return render(
        request,
        "dashboard.html",
        data,
    )


# ==================================
# FRESHER REGISTRATION
# ==================================

@login_required
def register(request):

    form = FresherForm()

    # if form.is_valid():

    #     fresher = form.save()

    #     freshers_collection.insert_one({
    #         "employee_id": fresher.employee_id,
    #         "name": fresher.name,
    #         "email": fresher.email,
    #         "phone": fresher.phone,
    #         "technology": fresher.technology,
    #         "batch": fresher.batch,
    #         "joining_date": str(fresher.joining_date),
    #     })

    #     return redirect("dashboard")

    # print(form.errors)   # <-- Add this line , To review errors

    return render(
        request,
        "register.html",
        {"form": form},
    )
# ==================================
# DAILY PROGRESS
# ==================================

@login_required
def progress(request):

    form = ProgressForm(
        request.POST or None
    )

    if form.is_valid():

        progress=form.save()
        
        progress_collection.insert_one({
            "fresher":progress.fresher.employee_id,
            "date":str(progress.date),
            "topic":progress.topic,
            "hours":progress.hours,
            "tasks":progress.tasks,
            "challenges":progress.challenges,
        })

        return redirect(
            "dashboard"
        )

    return render(
        request,
        "progress.html",
        {
            "form": form
        },
    )


# ==================================
# ASSIGNMENT
# ==================================

@login_required
def assignment(request):

    form = AssignmentForm(
        request.POST or None
    )

    if form.is_valid():

        assignment=form.save()
        assignments_collection.insert_one({
            "fresher":assignment.fresher.employee_id,
            "assignment_name":assignment.assignment_name,
            "github_link":assignment.github_link,
            "status":assignment.status,
            
        })

        return redirect(
            "dashboard"
        )

    return render(
        request,
        "assignment.html",
        {
            "form": form
        },
    )


# ==================================
# PROJECT TRACKER
# ==================================

@login_required
def project(request):

    form = ProjectForm(
        request.POST or None
    )

    if form.is_valid():

        project = form.save()
        
        projects_collection.insert_one({
            "fresher":project.fresher.employee_id,
            "project_name":project.project_name,
            "technology":project.technology,
            "progress":project.progress,
            "github_link":project.github_link,
        })

        return redirect(
            "dashboard"
        )

    return render(
        request,
        "project.html",
        {
            "form": form
        },
    )


# ==================================
# DJANGO REST APIs
# ==================================

class FresherAPI(
    viewsets.ModelViewSet
):

    queryset = (
        Fresher.objects.all()
    )

    serializer_class = (
        FresherSerializer
    )


class ProgressAPI(
    viewsets.ModelViewSet
):

    queryset = (
        DailyProgress.objects.all()
    )

    serializer_class = (
        ProgressSerializer
    )


class AssignmentAPI(
    viewsets.ModelViewSet
):

    queryset = (
        Assignment.objects.all()
    )

    serializer_class = (
        AssignmentSerializer
    )


class ProjectAPI(
    viewsets.ModelViewSet
):

    queryset = (
        Project.objects.all()
    )

    serializer_class = (
        ProjectSerializer
    )


# ==================================
# MONGODB FRESHER API
# ==================================

@api_view(
    ["GET", "POST"]
)
def mongo_fresher_api(request):

    # ------------------------------
    # POST REQUEST
    # ------------------------------

    if request.method == "POST":

        fresher_data = {

            "employee_id":
                request.data.get(
                    "employee_id"
                ),

            "name":
                request.data.get(
                    "name"
                ),

            "email":
                request.data.get(
                    "email"
                ),

            "phone":
                request.data.get(
                    "phone"
                ),

            "technology":
                request.data.get(
                    "technology"
                ),

            "batch":
                request.data.get(
                    "batch"
                ),

            "joining_date":
                request.data.get(
                    "joining_date"
                ),

        }


        # Insert the record into MongoDB

        result = (
            freshers_collection
            .insert_one(
                fresher_data
            )
        )


        # Convert MongoDB ObjectId
        # into a normal JSON string

        mongodb_id = str(
            result.inserted_id
        )


        # MongoDB automatically adds
        # _id to fresher_data.
        # Convert it into a string.

        fresher_data["_id"] = (
            mongodb_id
        )


        # Send successful response
        # back to Postman

        return Response(

            {

                "message":
                    "Fresher data stored successfully",

                "mongodb_id":
                    mongodb_id,

                "data":
                    fresher_data,

            },

            status=
                status.HTTP_201_CREATED,

        )


    # ------------------------------
    # GET REQUEST
    # ------------------------------

    freshers = []

    # Retrieve all MongoDB records
    for fresher in (

        freshers_collection.find()

    ):

        # Convert MongoDB ObjectId
        # before returning JSON

        fresher["_id"] = str(fresher["_id"] )
        freshers.append(fresher)

    return Response(

        freshers,

        status=
            status.HTTP_200_OK,

    )