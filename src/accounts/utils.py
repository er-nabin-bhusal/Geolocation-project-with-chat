from accounts.models import Profile
import math 
from chats.models import ChatClass


def comparelocation(obj1,obj2,*args,**kwargs):
	lat1 = float(obj1.latitude)
	long1 = float(obj1.longitude)
	lat2 = float(obj2.latitude)
	long2 = float(obj2.longitude)
	radlat1 = math.radians(lat1)
	radlat2 = math.radians(lat2)
	thetaa = long1 - long2 
	theta = abs(thetaa)
	radtheta = math.radians(theta)
	dist = math.sin(radlat1)*math.sin(radlat2) + math.cos(radlat1)*math.cos(radlat2)*math.cos(radtheta)
	dist = math.acos(dist)
	dist = math.degrees(dist)
	dist = dist * 60 * 1.1515
	dist = dist*1.609344*1000
	return float(dist) 
def calculation(profile,*args,**kwargs):
	user = profile.user
	users_profile = Profile.objects.get(user=user)
	as_owner = ChatClass.objects.filter(owner=user)
	as_opponent = ChatClass.objects.filter(opponent=user)

	fren_user_list = [] #it stores all the users which are matched

	for i in as_owner:
		user1 = i.opponent
		fren_user_list.append(user1)
	for i in as_opponent:
		user2 = i.owner
		fren_user_list.append(user2)

	fren_profile_list = [] # profiles of all the opposite gender friends

	for i in fren_user_list:
		temp = Profile.objects.get(user=i)
		if temp.gender != users_profile.gender:
			fren_profile_list.append(temp)
	return fren_profile_list

def recommendation(user,*args,**kwargs):
	logged_in_user_profile = Profile.objects.get(user=user) #profile of logged in user
	as_owner = ChatClass.objects.filter(owner=user)
	as_opponent = ChatClass.objects.filter(opponent=user)
	fren_user_list = []
	for i in as_owner:
		user1 = i.opponent
		fren_user_list.append(user1)
	for i in as_opponent:
		user2 = i.owner
		fren_user_list.append(user2)

	fren_profile_list = [] # profiles of all the oppose gender friends
	for i in fren_user_list:
		temp = Profile.objects.get(user=i)
		if temp.gender != logged_in_user_profile.gender:
			fren_profile_list.append(temp)

	same_gender_profiles = [] #it stores all the friends of friends of same gender as logged in user(in the different list)
	for profile in fren_profile_list:
		some = calculation(profile)
		same_gender_profiles.append(some)
	
	same_gender_profiles_only = []  #it stores all the friends of same gender 

	for some in same_gender_profiles:
		for i in some:
			if user != i.user:
				same_gender_profiles_only.append(i)

	all_required_profiles = [] # list of all required profiles in different lists
	for profile in same_gender_profiles_only:
		temp = calculation(profile)
		all_required_profiles.append(temp)


	not_fren_not_user_only_opposite = [] # it stores all opposite gender come after third level where no user and frens 

	for some in all_required_profiles:
		for i in some:
			if user != i.user:
				if not i.user in fren_user_list:
					not_fren_not_user_only_opposite.append(i)


	not_repeated_profiles = []
	repeated_profiles = []

	for i in not_fren_not_user_only_opposite:
		if i in not_repeated_profiles:
			if not i in repeated_profiles:
				repeated_profiles.append(i)
		else:
			not_repeated_profiles.append(i)

	repeat_first_then_non_repeat = []

	for i in repeated_profiles:
		repeat_first_then_non_repeat.append(i)
	for i in not_repeated_profiles:
		repeat_first_then_non_repeat.append(i)

	all_recommendations = []

	for i in repeat_first_then_non_repeat:
		if not i in all_recommendations:
			all_recommendations.append(i)

	actual_recommend = []
	count = 0
	for i in all_recommendations:
		count = count + 1
		actual_recommend.append(i)
		if count > 2: 
			break

	return actual_recommend














