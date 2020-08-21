from django.urls import path
from . import views
urlpatterns = [
	path('', views.BlogListView.as_view(), name="blog_list" ),
	path('create_category/', views.CategoryCreateView.as_view(), name="category_create" ),
	path('create_blog/', views.BlogCreateView.as_view(), name="blog_create" ),
	path('update_category/<int:pk>/', views.CategoryUpdateView.as_view(), name="update_category"),
	path('update_blog/<int:pk>/', views.BlogUpdateView.as_view(), name="update_blog"),
	path('category_all', views.CategoryListView.as_view(), name="category_all"),
	path('filter', views.BlogFilterView.as_view(), name='blog_filter'),
	path('filter_category', views.CategoryFilterTemplateView.as_view(), name='category_filter'),
	# path('form/', views.BlogFormView.as_view(), name='form'),
]