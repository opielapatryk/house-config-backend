from django.http import JsonResponse
from apps.users.infrastructure.repositories import DjangoUserRepository
from apps.users.application.use_cases import RegisterUser

def register_view(request):
    repo = DjangoUserRepository()
    use_case = RegisterUser(repo)
    user = use_case.execute(email="test@example.com", password="secret123")
    return JsonResponse({"id": user.id, "email": user.email})