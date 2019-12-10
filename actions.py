from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import Restarted
import zomatopy
import json
import pandas as pd
import smtplib
from email.message import EmailMessage
from threading import Thread
from time import sleep

ZOMATO_CONFIG={ "user_key":"6480d8611c99c6b5ff80ebe72d2c0539"}

class ActionSearchRestaurants(Action):
	"""
	Finds best resturants serving a particular cuisine, under a specified budget around a given location.
	Returns the results in the desceding order of their ranking.
	"""

	def name(self):
		return 'action_search_restaurants'
	
		
	def run(self, dispatcher, tracker, domain):

		# get location
		location = tracker.get_slot('location')

		# get cuisine
		cuisine = tracker.get_slot('cuisine')
		
		# get budget
		budget = tracker.get_slot('price')
		budget1 = budget.lower()
		
		# use the zomato API and get lat, lon
		zomato = zomatopy.initialize_app(ZOMATO_CONFIG)
		location_detail=zomato.get_location(location, 1)

		location_detail = json.loads(location_detail)
		lat=location_detail["location_suggestions"][0]["latitude"]
		lon=location_detail["location_suggestions"][0]["longitude"]


		cuisines_dict={'chinese':25,'italian':55,'north_indian':50,'south_indian':85, 'american': 1, 'mexican': 73}

		# get restaurants for the given lat lon and cuisine
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 200)

		results = json.loads(results)
		restaurants = results['restaurants']
		response = "" 

		# global restaurant dataframe
		global restaurants_df
		restaurants_df = pd.DataFrame([{'restaurant_name': restaurant['restaurant']['name'], \
						'restaurant_address': restaurant['restaurant']['location']['address'], \
						'average_cost_for_two': restaurant['restaurant']['average_cost_for_two'], \
						'restaurant_average_rating': restaurant['restaurant']['user_rating']['aggregate_rating']}
						 for restaurant in restaurants])
		
		# lambda function for budget
		def budgetize(row):
			if row['average_cost_for_two'] < 300:
                		return 'lesser than rs 300'
			elif row['average_cost_for_two'] > 700:
                		return 'more than 700'
			else:
                		return 'rs 300 to 700'

		## create a new column budget 
		restaurants_df['budget'] = restaurants_df.apply(lambda row: budgetize(row), axis=1)

		## filter on budget
		restaurants_df = restaurants_df[(restaurants_df['budget'] == budget1)]

		## sort the dataframe based on rating
		restaurants_df = restaurants_df.sort_values(['restaurant_average_rating'], ascending = 0)
		
		# get five restaurants
		five_restaurants = restaurants_df[:5]
		
	
		# send response
		response = "Here are the top results for you: "+ "\n" + "\n"

		no_results = True		
		if len(restaurants_df) == 0:
			response= "Oops! No results for your query. Please try with a different location or a higher budget.\n"
			dispatcher.utter_message(response)
			
		else:
			no_results = False
			pos = 0
			five_restaurants = restaurants_df[:5]
			for _, restaurant in five_restaurants.iterrows():
				pos += 1
				formatted_result = "{}. {} in {} has been rated {}\n\n".format(str(pos), \
					restaurant['restaurant_name'], \
					restaurant['restaurant_address'], \
					str(restaurant['restaurant_average_rating']))
				response = response + formatted_result
					
			dispatcher.utter_message(response)
		
		return [SlotSet('location',location), SlotSet('no_results',no_results)]
			

class ActionCheckLocation(Action):
	"""
	Validates that the identified location entity is a serviceable area.
	"""
	def __init__(self):

		# service area list containing tier I and tier II cities		
		self.service_areas = ['bangalore','chennai','delhi','hyderabad','Kolkata','mumbai','ahmedabad','pune', 'cochi',
      'agra','ajmer','aligarh','amravati','amritsar','asansol','aurangabad','bareilly','belgaum',
      'bhavnagar','bhiwandi','bhopal','bhubaneswar','bikaner','bilaspur','bokaro Steel City',
      'chandigarh','coimbatore','nagpur','cuttack','dehradun','dhanbad','bhilai','durgapur',
      'erode','faridabad','firozabad','ghaziabad','gorakhpur','gulbarga','guntur','gwalior',
      'gurgaon','guwahati','hamirpur','hubli–Dharwad','hubli','dharwad','indore','jabalpur',
      'jaipur','jalandhar','jammu','jamnagar','jamshedpur','jhansi','jodhpur','kakinada',
      'kannur','kanpur','kottayam','kolhapur','kollam','kozhikode','kurnool','ludhian',
      'lucknow','madurai','malappuram','mathura','goa','mangalore','meerut','moradabad',
      'mysore','nanded','nashik','nellore','noida','palakkad','patna','perinthalmanna',
      'pondicherry','purulia Prayagraj','raipur','rajkot','rajahmundry','ranchi','rourkela',
      'salem','sangli','shimla','siliguri','solapur','srinagar','thiruvananthapuram','thrissur',
      'tiruchirappalli','tirur','tirupati','tirunelveli','tiruppur','tiruvannamalai','ujjain',
      'bijapur','vadodara','varanasi','vasai-Virar City','vijayawada','vellore','warangal',
      'surat','visakhapatnam']

	def name(self):
		return 'action_check_location'

	def run(self, dispatcher, tracker, domain):
		location = tracker.get_slot('location')
		if location is not None:
			if type(location) == str:
				if location.lower() in self.service_areas:
					return [SlotSet('location', location),SlotSet('location_match','one')]
		return [SlotSet('location', None), SlotSet('location_match','zero')]


class ActionSendEmail(Action):
	"""
	Sends top 10 search results to the user specified mail. 
	"""

	def name(self):
		return 'action_send_email'

	def sendEmail(self, email_id):
		
		msg = EmailMessage()
		
		ten_restaurants = restaurants_df[:10]

		# create email body
		response = " Showing you top rated restaurants \n\n"
		pos = 0
		for _, restaurant in ten_restaurants.iterrows():
			pos += 1
			formatted_result = "{}. {} in {} has been rated {}. Average cost for two people is approx {}. \n\n".format(str(pos), \
				restaurant['restaurant_name'], \
				restaurant['restaurant_address'], \
				str(restaurant['restaurant_average_rating']), \
				str(restaurant['average_cost_for_two'])) 
			response = response + formatted_result

		# setup email 
		msg.set_content(response)
		msg['Subject'] = f'Top 10 Restaurants'
		msg['From'] = 'testemail@gmail.com'
		msg['To'] = str(email_id)

		s = smtplib.SMTP('64.233.184.108',587)
		try:
			s.starttls()
			s.login("testemail@gmail.com","passwd")
			s.send_message(msg)
		except Exception as e:
			print(str(e))

		s.quit()

	def run(self, dispatcher, tracker, domain):
		# start a thread to send mail
		recipient = tracker.get_slot('emailid')
		thread1 = Thread(target=self.sendEmail,args=(recipient,))
		thread1.start()
		thread1.join()

class ActionRestarted(Action): 
	"""
	Restart the conversation.
	"""	
	def name(self):
		return 'action_restart'
	def run(self, dispatcher, tracker, domain):
		return[Restarted()]
		

class ActionSlotReset(Action): 
	"""
	Reset all slots.
	"""
	def name(self): 
		return 'action_slot_reset' 
	def run(self, dispatcher, tracker, domain): 
		return[AllSlotsReset()]