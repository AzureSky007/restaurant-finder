# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.events import Restarted, SlotSet, EventType, Form, FormValidation
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionRecommendRestaurant(Action):
    def name(self) -> Text:
        return "action_recommend_restaurant"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        cuisine_type =tracker.get_slot("cuisine_type")
        size = tracker.get_slot("size")
        location = tracker.get_slot("location")

        api_key = "AIzaSyB16K-9sljPE0fuykKw4qGVXpAuRf1aYJo"
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        params = {
            "key": api_key,
            "query": "{} restaurant in {}".format(cuisine_type, location)
        }
        response = requests.get(url, params = params)

        if response.status_code == 200:
            results = response.json().get("results", [])
            if results:
                restaurant_names = [result.get("name") for result in results]
                restaurant_addresses = [result.get("formatted_address") for result in results]
                restaurant_info = "\n".join(["{} - {}".format(name, address) for name, address in zip(restaurant_names, restaurant_addresses)])
                message = "Here are some restaurant recommendations for {} cuisine in {}:\n{}".format(cuisine_type, location, restaurant_info)
            else:
                message = "Sorry, I couldn't find any restaurants for {} cuisine in {}.".format(cuisine_type, location)
        else:
            message = "Oops! Something went wrong while retrieving restaurant recommendations."

        dispatcher.utter_message(text=message)

        return []

# class ActionDeactivateLoop(Action):
#     def name(self) -> Text:
#         return "action_deactivate_loop"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         return [DeactivateForm("restaurant_form")]

class ActionReset(Action):
    def name(self) -> Text:
        return "action_reset"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [Restarted()]


class ValidateMainMenuForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_restaurant_form"

    def validate_cuisine_type( self,
        slot_value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        message = "How many people will be eating?"
        dispatcher.utter_message(text=message)
        return {"cuisine_type":slot_value}

    def validate_size( self,
        slot_value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        message = "The location you're looking for?"
        dispatcher.utter_message(text=message)
        return {"size":slot_value}

    def validate_location( self,
        slot_value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        cuisine_type = tracker.slots.get('cuisine_type')
        size = tracker.slots.get('size')
        location = tracker.slots.get('location')

        api_key = ""                                                                              ## Add in your API Key at this location
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        parameters = {
            "key": api_key,
            "query": "{} restaurant in {}".format(cuisine_type, location)
        }
        response = requests.get(url, params = parameters)

        if response.status_code == 200:
            results = response.json().get("results", [])
            if len(results) > 0:
                restaurant_info = ""
                for result in results:
                    name = result.get("name")
                    address = result.get("formatted_address")
                    rating = result.get("rating", "N/A")
                    restaurant_info += f"{name} - {address} (Rating: {rating})"
                    print()

                message = f"Here are some restaurant recommendations for {cuisine_type} cuisine in {location}:\n{restaurant_info}"


            # if results:
            #     restaurant_names = [result.get("name") for result in results]
            #     restaurant_addresses = [result.get("formatted_address") for result in results]
            #     restaurant_info = "\n".join(["{} - {}".format(name, address) for name, address in zip(restaurant_names, restaurant_addresses)])
            #     message = "Here are some restaurant recommendations for {} cuisine in {}:\n{}".format(cuisine_type, location, restaurant_info)
            else:
                message = "Sorry, I couldn't find any restaurants for {} cuisine in {} for {} people.".format(cuisine_type, location, size)
        else:
            message = "Oops! Something went wrong while retrieving restaurant recommendations."

        dispatcher.utter_message(text=message)
        return []