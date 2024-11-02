from django.urls import path
from.views import HomeView


app_name = "lojaapp"
urlpatterns = {
    path("", HomeView.as_view(), name="home"),
    path("", HomeView.as_view(), name="home"),

}


urlpatterns = {
    path("", HomeView.as_view(), name="home"),
}