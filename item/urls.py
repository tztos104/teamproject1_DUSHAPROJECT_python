from django.urls import path

from item import views

app_name = 'item'


urlpatterns = [

    path('', views.item_list, name='item_list'),
    path('<int:id>', views.item_detail, name='item_detail'),
    path('best/', views.best, name='best_item'),
    path('create/', views.item_create, name='item_create'),
    path('category/<str:slug>/', views.category_page, name='category_page'),

    ]

# urlpatterns = [
#     path('create/', ItemCreateView.as_view(), name='create'),
#     path('list/', ItemListView.as_view(), name='list'),
#     path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
#     path('update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
#     path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),
#     path('search/', ItemSearchView.as_view(), name='search'),
#     path('like/', ItemLikeView.as_view(), name='like'),
#     path('comment/', ItemCommentView.as_view(), name='comment'),
#     path('comment/delete/', ItemCommentDeleteView.as_view(), name='comment_delete'),
# ]