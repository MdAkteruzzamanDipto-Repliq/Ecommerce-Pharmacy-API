from django.urls import path, include



from . import views

urlpatterns = [
    path('', views.CreateOrganizationView.as_view(), name='create'),
    path('all', views.ListOrganizationView.as_view(), name='list_organizations'),
    path('public/all', views.ListOrganizationPublicView.as_view(), name='list_public_organizations'),
    path('me', views.ListMeOrganizationView.as_view(), name='me_organizations'),
]