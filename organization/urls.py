from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.CreateOrganizationView.as_view(), name='create'),
    path('all', views.ListOrganizationView.as_view(), name='list_organizations'),
    path('public/all', views.ListOrganizationPublicView.as_view(), name='list_public_organizations'),
    path('me', views.ListMeOrganizationView.as_view(), name='me_organizations'),
    path('me/internals', views.ListOrganizationInternalMembersView.as_view(), name='me_organizations_internals'),
    path('me/owner/create-internal', views.OwnerCreateOrganizationUserView.as_view(), name='owner_create_internals'),
    path('me/admin/create-internal', views.AdminCreateOrganizationUserView.as_view(), name='admin_create_internals'),
    path('me/manager/create-internal', views.ManagerCreateOrganizationUserView.as_view(), name='manager_create_internals'),
]