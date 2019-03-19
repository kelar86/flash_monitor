from rest_framework import routers
from rest_api import views as api_views
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'applications', api_views.ApplicationsViewSet, 'Application')
# router.register(r'problems', api_views.ProblemsViewSet)
router.register(r'alerts', api_views.AlertsViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'problems/', api_views.ProblemsViewSet.as_view()),
    path(r'problems/<int:id>/', api_views.ProblemDetail.as_view()),
    path(r'filter-advise/', api_views.SearchFilterView.as_view()),
    path(r'top-problems/', api_views.AdviseSearchView.as_view()),
    path(r'rest-auth/', include('rest_auth.urls')),
]
