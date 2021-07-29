from django.urls import path,include
from . import views
from .views import *
urlpatterns=[
    path('',CourseListView.as_view(),name='course'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('course/new/', CourseCreateView.as_view(), name='course-create'),
    path('course/<int:pk>/update', CourseUpdateView.as_view(), name='course-update'),
    path('course/<int:pk>/module/<int:pkk>/update', ModuleUpdateView.as_view(), name='module-update'),
    path('course/<int:pk>/module/new',ModuleCreateView.as_view(), name='module-create'),
    path('course/<int:pk>/module/',ModuleListView.as_view(), name='module-list'),
    path('course/<int:pk>/module/<int:pkk>',ModuleDetailView.as_view(), name='module-detail'),
    path('search/',searchbytag, name = 'search'),
    path('course/enroll/<int:pk>',enroll, name = 'enroll'),
    path('course/study/<int:pk>/',studycourse, name = 'study'),
    path('course/<int:pk>/review',review_course,name='review'),
    path('course/<int:pk>/seereview',showreview,name='see-review'),
    path('course/module/complete/<int:pkk>/',completemodule, name = 'complete-module'),
]
