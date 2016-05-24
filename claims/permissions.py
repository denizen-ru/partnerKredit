from rest_framework import permissions
# from accounts.models import SUPER_USER, PARTNER, CREDIT_ORGANIZATION


class OfferPermission(permissions.BasePermission):
    """Composite permissions for Offer model"""

    def has_permission(self, request, view):
        user = request.user

        # Credit Organization not allowed to create or edit anything
        # if (user.user_type is CREDIT_ORGANIZATION and
        #         request.method not in permissions.SAFE_METHODS):
        #     return False

        return True

    # def has_object_permission(self, request, view, obj):
    #     # example code for safe methods
    #     if request.method in permissions.SAFE_METHODS:
    #         return True

    #     # example code: grant write access only for owner
    #     return obj.credit_organization.user == request.user
        # return True


class QuestionnairePermission(permissions.BasePermission):
    """Compsite permissions for Questionnaire model"""

    def has_permission(self, request, view):
        user = request.user

        # superuser not allowed to create Questionnaire
        # if request.method == 'POST' and user.user_type is SUPER_USER:
        #     return False

        # Credit Organization not allowed to create or edit anything
        # if (user.user_type is CREDIT_ORGANIZATION and
        #         request.method not in permissions.SAFE_METHODS):
        #     return False

        # Partner cannot delete or edit Questionnaire
        # if (user.user_type is PARTNER and
        #         request.method not in ('GET', 'HEAD', 'OPTIONS', 'POST')):
        #     return False

        return True

    def has_object_permission(self, request, view, obj):
        # if (request.user.user_type is PARTNER and
        #         obj.partner.user != request.user):
        #     return False
        return True


class ClaimPermission(permissions.BasePermission):
    """Composite permissions for Claim model"""

    def has_permission(self, request, view):
        user = request.user

        # Credit Organization not allowed to create or edit anything
        # if (user.user_type is CREDIT_ORGANIZATION and
        #         request.method not in permissions.SAFE_METHODS):
        #     return False

        # Partner can only create, list and read Claims
        # if (user.user_type is PARTNER and
        #         (request.method is not 'POST' or
        #          request.method not in permissions.SAFE_METHODS)):
        #     return False

        return True

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Credit Organization can work only with it's own Claims
        # if (user.user_type is CREDIT_ORGANIZATION and
        #         obj.offer.credit_organization.user != user):
        #     return False

        return True
