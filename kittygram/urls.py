# Обновлённый urls.py
from django.urls import include, path
from cats.views import CatViewSet
from rest_framework.routers import SimpleRouter

# Создаётся роутер
router = SimpleRouter()
# Вызываем метод .register с нужными параметрами
router.register('cats', CatViewSet)
# В роутере можно зарегистрировать любое количество пар "URL, viewset":
# например
# router.register('owners', OwnerViewSet)
# Но нам это пока не нужно

# router.register('cats', CatViewSet, basename='tiger')

urlpatterns = [
    # Все зарегистрированные в router пути доступны в router.urls
    # Включим их в головной urls.py
    path('', include(router.urls)),
]

# from rest_framework.routers import SimpleRouter
# from django.urls import path, include
# from posts.views import PostViewSet

# router = SimpleRouter()
# router.register('posts', PostViewSet)

# urlpatterns = [
#        path('api/v1/posts/', include(router.urls)),
# ]


# urlpatterns = [
#     path('cats/', CatList.as_view()),
#     path('cats/<int:pk>/', CatDetail.as_view()),
# ]

# from django.urls import include, path

# from cats.views import cat_list

# urlpatterns = [
#    path('cats/', cat_list),
# ]

# from django.urls import include, path

# from cats.views import APICat

# urlpatterns = [
#     path('cats/', APICat.as_view()),
# ]
