from accounts.models import Profile
import math 


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

