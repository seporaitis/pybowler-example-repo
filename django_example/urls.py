from django.urls import url

from foo import views

urlpatterns = [
    url(r"^all/$", views.all_view, name="all"),
    url(r"^update/$", views.update_view, name="update"),
    url(r"^mark/$", views.mark_view, name="mark"),
    url(r"^mark-all/$", views.mark_all_view, name="mark_all"),
    url(r"^delete/$", views.delete_view, name="delete"),
    url(r"^redirect/(?P<obj_id>[\d]+)/$", views.redirect_view, name="redirect"),
]
