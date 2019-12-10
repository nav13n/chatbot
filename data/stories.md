## greet
* greet
    - utter_greet


## greet and bye
* greet
    - utter_greet
* goodbye
    - utter_goodbye
    - action_restart

## story1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"no_results": false}
    - utter_ask_send_email
* affirm
    - utter_ask_email
* affirm{"emailid": "help@gmail.com"}
    - slot{"emailid": "help@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_restart

## story1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"no_results": true}
    - utter_goodbye
    - action_restart

## story2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"no_results": false}
    - utter_ask_send_email
* affirm{"emailid": "test13455@@gmail.com"}
    - slot{"emailid": "test13455@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_restart

## story_3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search{"price": "Lesser than Rs 300"}
    - slot{"price": "Lesser than Rs 300"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"no_results": false}
    - utter_ask_send_email
* affirm{"emailid": "test345@gmail.com"}
    - slot{"emailid": "test345@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_restart

## story_4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"no_results": false}
    - utter_ask_send_email
* affirm
    - utter_ask_email
* inform{"emailid": "test1234@gmail.com"}
    - slot{"emailid": "test1234@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_restart

## story_5
* greet
    - utter_greet
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"no_results": false}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
    - utter_goodbye
    - action_restart

## story_6
* greet
    - utter_greet
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"no_results": false}
    - utter_ask_send_email
* affirm
    - utter_ask_email
* inform{"emailid": "test456@gmail.com"}
    - slot{"emailid": "test456@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_restart

## story_7
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Shimoga"}
    - slot{"location": "Shimoga"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_match": "zero"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"no_results": false}
    - utter_ask_send_email
* affirm
    - utter_ask_email
* inform{"emailid": "testest@gmail.com"}
    - slot{"emailid": "testest@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_restart
    
## story-8
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Shimoga"}
    - slot{"location": "Shimoga"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_match": "zero"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"no_results": false}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
    - utter_goodbye
    - action_restart

## story_9
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"location": "Delhi"}
    - slot{"location_match": "one"}
    - utter_ask_budget
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"no_results": false}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
    - utter_goodbye
    - action_restart

## story_9
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"location": "Delhi"}
    - slot{"location_match": "one"}
    - utter_ask_budget
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"no_results": true}
    - utter_goodbye
    - action_restart

## story_10
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "shimoga"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "shimoga"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_match": "zero"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - slot{"location_match": "one"}
    - utter_ask_budget
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"no_results": false}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
    - utter_goodbye
    - action_restart

## story-11
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Delhi", "price": "Rs 300 to 700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - slot{"price": "Rs 300 to 700"}
    - action_check_location
    - slot{"location": "Delhi"}
    - slot{"location_match": "one"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"no_results": false}
    - utter_ask_send_email
* affirm
    - utter_ask_email
* inform{"emailid": "test.test@gmail.com"}
    - slot{"emailid": "test.test@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_restart

## story_13
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price": "Rs 300 to 700"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "Rs 300 to 700"}
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"location": "Delhi"}
    - slot{"location_match": "one"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"no_results": false}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
    - utter_goodbye
    - action_restart


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price": "Rs 300 to 700"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "Rs 300 to 700"}
    - utter_ask_location
* restaurant_search{"location": "shimoga"}
    - slot{"location": "shimoga"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_match": "zero"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"location": "Delhi"}
    - slot{"location_match": "one"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"no_results": false}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "shimoga", "price": "Rs 300 to 700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "shimoga"}
    - slot{"price": "Rs 300 to 700"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_match": "zero"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"location": "Delhi"}
    - slot{"location_match": "one"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"no_results": false}
    - utter_ask_send_email
* deny
    - utter_no_email_sent
    - utter_goodbye
    - action_restart

## goodbye_1
* goodbye
    - utter_goodbye
	- action_restart

## goodbye_2
* goodbye
    - utter_goodbye
	- action_restart
    - action_restart

## goodbye_3
* goodbye
    - utter_goodbye
	- action_restart

## goodbye_4
* goodbye
    - utter_goodbye
	- action_restart

## goodbye_5
* goodbye
    - utter_goodbye
	- action_restart

## goodbye_6
* goodbye
    - utter_goodbye
	- action_restart


## deny_1
* deny
    - utter_no_email_sent
	- action_restart

## deny_2
* deny
    - utter_no_email_sent
	- action_restart

## deny_3
* deny
    - utter_no_email_sent
	- action_restart

## deny_4
* deny
    - utter_no_email_sent
	- action_restart

## deny_4
* deny
    - utter_no_email_sent
	- action_restart

## deny_5
* deny
    - utter_no_email_sent
	- action_restart

## deny_6
* deny
    - utter_no_email_sent
	- action_restart

## deny_7
* deny
    - utter_no_email_sent
	- action_restart

