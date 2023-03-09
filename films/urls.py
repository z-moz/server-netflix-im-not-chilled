from django.urls import path
from .views import filter_out_one_film, filter_out_a_list 

urlpatterns = [
    path('netflix_id/<int:id>/', filter_out_one_film.as_view(),
         name='filter_out_one_film'),


 

    path('api/', filter_out_a_list.as_view(), name='filter_out_a_list'),

    # path('netflix_id/<int:id>/', FilmRetrieveById.as_view(),
    #      name="get_by_netflix_id"),
    # path('api/', FilmView.as_view(), name="get_all_films"),

    # path('title/', FilmRetrieveByTitle.as_view(), name='get_by_film_title'),
    # path('filter_for/', FilmViewFiltered.as_view(), name="filtered_film_list"),

]