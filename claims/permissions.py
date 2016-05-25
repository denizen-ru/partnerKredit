from rest_framework import permissions


class OfferPermission(permissions.BasePermission):
    """Composite permissions for Offer model"""

    def has_permission(self, request, view):
        user = request.user

        # Credit Organization not allowed to create or edit anything
        if (hasattr(user, 'creditorganization') and
                request.method not in permissions.SAFE_METHODS):
            return False

        return True


class QuestionnairePermission(permissions.BasePermission):
    """Compsite permissions for Questionnaire model"""

    def has_permission(self, request, view):
        user = request.user

        # superuser not allowed to create Questionnaire
        if request.method == 'POST' and hasattr(user, 'superuser'):
            return False

        # Credit Organization not allowed to create or edit anything
        if (hasattr(user, 'creditorganization') and
                request.method not in permissions.SAFE_METHODS):
            return False

        # Partner cannot delete or edit Questionnaire
        if (hasattr(user, 'partner') and
                request.method not in ('GET', 'HEAD', 'OPTIONS', 'POST')):
            return False

        return True

    def has_object_permission(self, request, view, obj):
        if (hasattr(request.user, 'partner') and
                obj.partner.user != request.user):
            return False
        return True


class ClaimPermission(permissions.BasePermission):
    """Composite permissions for Claim model"""

    def has_permission(self, request, view):
        user = request.user

        # Credit Organization not allowed to create or edit anything
        if (hasattr(user, 'creditorganization') and
                request.method not in permissions.SAFE_METHODS):
            return False

        # Partner can only create, list and read Claims
        if (hasattr(user, 'partner') and
                (request.method is not 'POST' or
                 request.method not in permissions.SAFE_METHODS)):
            return False

        return True

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Credit Organization can work only with it's own Claims
        if (hasattr(user, 'creditorganization') and
                obj.offer.credit_organization.user != user):
            return False

        return True
