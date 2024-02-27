from rest_framework import routers
from rentals import views as rental_views
router = routers.DefaultRouter()

router.register(r'friends', rental_views.FriendViewSet)
router.register(r'belongings', rental_views.BelongingViewSet)
router.register(r'borrowings', rental_views.BorrowedViewSet)
Operation HTTP method Endpoint type
Create POST list
Retrieve many GET list
Retrieve one GET detail
Update PUT / PATCH detail
Delete DELETE detail
