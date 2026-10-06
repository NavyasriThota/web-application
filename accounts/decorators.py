from functools import wraps

from django.shortcuts import redirect


def role_required(*allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')

            if request.user.role not in allowed_roles:
                if request.user.is_admin_user:
                    return redirect('admin_dashboard')
                return redirect('student_dashboard')

            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator


admin_required = role_required('admin')
student_required = role_required('student')
