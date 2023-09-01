from django.contrib import admin
from django.urls import path
from test.views import TestListCreateView, TestDetailView, TestStatsView, QuestionListCreateView, QuestionDetailView, AnswerListCreateView, AnswerDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/test/', TestListCreateView.as_view(), name='test-list'),
    path('api/v1/test/<int:pk>/', TestDetailView.as_view(), name='test-detail'),
    path('api/v1//test/<int:pk>/stats/', TestStatsView.as_view(), name='test-stats'),

]
