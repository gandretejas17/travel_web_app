from django.urls import path
from travelapp import views

urlpatterns =[
    path('index/',views.index_view),
    path('add/',views.add_view),
    path('register/', views.register_view),
    path('list/', views.list_view),
    path('detail/<int:id>/',views.detail_view),
    path('delete/<int:id>/', views.delete_view),
    path('update/<int:id>/', views.update_view),
    path('a/', views.a_view),
    path('b/', views.b_view),
    path('c/', views.c_view),
    path('d/', views.d_view),
    path('e/', views.e_view)

]