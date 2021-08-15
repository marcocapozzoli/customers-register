from django.urls import path
from django.views.i18n import JavaScriptCatalog
from . import views


urlpatterns = [
    
    # Style Django-Admin
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
    
    path('', views.home, name='home'),
    #path('business', views.business, name='business'),
    # path('tasks', views.tasks, name='tasks'),
    path('contacts', views.contacts, name='contacts'),
]