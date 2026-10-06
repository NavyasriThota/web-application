from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer


@login_required
@require_POST
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('login')


@login_required
def profile_view(request):
    profile = getattr(request.user, 'student_profile', None)
    return render(request, 'profile.html', {'profile': profile, 'user': request.user})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user_api(request):
    return Response(UserSerializer(request.user).data)
