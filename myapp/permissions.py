from rest_framework import permissions

class IsStudent(permissions.BasePermission):
    """Студент бачить лише свої курси та ДЗ, може здавати ДЗ."""
    def has_permission(self, request, view):
        # Перевіряє, чи користувач автентифікований і є студентом
        return request.user.is_authenticated and request.user.role == 'student'

    def has_object_permission(self, request, view, obj):
        # Доступ лише до своїх домашніх завдань
        return obj.student == request.user  # Припускаємо, що об'єкт має поле student


class IsTeacher(permissions.BasePermission):
    """Викладач бачить курси, де викладає, і може ставити оцінки."""
    def has_permission(self, request, view):
        # Перевіряє, чи користувач автентифікований і є викладачем
        return request.user.is_authenticated and request.user.role == 'teacher'

    def has_object_permission(self, request, view, obj):
        # Доступ лише до курсів, де викладачем є поточний користувач
        return obj.course.teacher == request.user  # Припускаємо, що об'єкт має поле course з полем teacher


class IsAdmin(permissions.BasePermission):
    """Адмін має повний доступ."""
    def has_permission(self, request, view):
        # Перевіряє, чи користувач автентифікований і є адміністратором (staff)
        return request.user.is_authenticated and request.user.is_staff
