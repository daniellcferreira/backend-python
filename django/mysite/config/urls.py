from config.admin import admin_site
from django.urls import include, path

urlpatterns = [
    path("admin/", admin_site.urls),  # Custom admin site
    path("polls/", include("polls.urls")),  # Polls app
    path("contacts/", include("contacts.urls")),  # Contacts app
    path("accounts/", include("accounts.urls")),  # Accounts app
]
