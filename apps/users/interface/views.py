from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponseNotAllowed
import json

from apps.users.infrastructure.repositories import DjangoUserRepository
from apps.users.application.use_cases import RegisterUser

@csrf_exempt
def register_view(request: HttpRequest):
    if request.method == "GET":
        return render(request, "users/register.html")

    elif request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        username = request.POST.get("username")

        try:
            repo = DjangoUserRepository()
            use_case = RegisterUser(repo)
            user = use_case.execute(email=email, password=password, username=username)

            return JsonResponse({
                "id": user.id,
                "email": user.email,
                "username": user.username
            }, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    else:
        return HttpResponseNotAllowed(["GET", "POST"])