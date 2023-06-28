from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import AddFriendForm
from .models import Friends, Friend_Request, Message

# Create your views here.
@login_required(login_url='Login')
def chat(request, friendName = False):
    friendsObj, __ = Friends.objects.get_or_create(user = request.user)
    friendsList = friendsObj.friends.all()
    room_code = 0
    messages = []

    if friendName:
        friendObj = User.objects.get(username = friendName)
        ids = sorted([friendObj.id, request.user.id])
        room_code = f"{ids[0]}_{ids[1]}"

        # Get messages
        messages = Message.objects.all().filter(friends_room = room_code)

    else :
        friendName = ''
    
    return render(request, 'chat.html', {
        'username' : request.user.username,
        'friends' : friendsList,
        'friend_name' : friendName,
        'room_code' : room_code,
        'messages' : messages
    })
    
@login_required(login_url='Login')
def add_friend(request):
    # Get friends requests
    friend_requests = Friend_Request.objects.all().filter(to_user = request.user)
    
    form = AddFriendForm()

    if request.method == 'POST':
        form = AddFriendForm(request.POST)
        if form.is_valid():
            try:
                FriendID = User.objects.get(username =form.cleaned_data['friendName']).id

                # Check if they are friends

                user_friendsObj, __ = Friends.objects.get_or_create(user = request.user)
                user_friends_list = user_friendsObj.friends.all()
                friendObj = User.objects.get(id = FriendID)
                if friendObj in user_friends_list:
                    messages.error(request, 'You are already friends')
                    return redirect('addFriend')
            
                return redirect('send friend request', FriendID = FriendID)
            except User.DoesNotExist:
                messages.error(request, 'User not found')
                return redirect('addFriend')
        
    return render(request, 'addFriend.html', {
        'form' : form,
        'friend_requests' : friend_requests
    })

@login_required(login_url = 'Login')
def send_friend_request(request, FriendID):
    from_user = request.user
    to_user = User.objects.get(id = FriendID)

    if from_user == to_user:
        messages.error(request, 'You cant send a friend request to yourself')
        return redirect('addFriend')

    friend_request, created = Friend_Request.objects.get_or_create(
    from_user = from_user, to_user = to_user)
    if created:
        messages.success(request, 'Friend request have been sent')
    else:
        messages.error(request, 'You already have sent a friend request')
    return redirect('addFriend')
    
@login_required(login_url = 'Login')
def accept_friend_request(request, requestID, deny = False):
    friend_request = Friend_Request.objects.get(id = requestID)

    if deny:
        friend_request.delete()

    elif friend_request.to_user == request.user:
        # Get Friend model
        to_userFriendObj, __ = Friends.objects.get_or_create(user = friend_request.to_user)
        from_userFriendObj, __ = Friends.objects.get_or_create(user = friend_request.from_user)

        print(to_userFriendObj, type(to_userFriendObj))
        to_userFriendObj.friends.add(friend_request.from_user)
        from_userFriendObj.friends.add(friend_request.to_user)
        friend_request.delete()
        messages.success(request, 'Friend request accepted')
    else:
        messages.success(request, 'Friend request denied')

    return redirect('addFriend')