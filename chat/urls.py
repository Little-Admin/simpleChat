from django.urls import path
from chat import views

urlpatterns = [
    path('', views.chat, name='chat_index'),
    path('c/<str:friendName>/', views.chat, name='chat_index'),
    path('addFriend/', views.add_friend, name='addFriend'),
    path('send_friend_request/<int:FriendID>', views.send_friend_request, name='send friend request'),
    path('accept_friend_request/<int:requestID>', views.accept_friend_request, name='accept friend request'),
    path('accept_friend_request/<int:requestID>/<int:deny>', views.accept_friend_request, name='deny friend request'),
]