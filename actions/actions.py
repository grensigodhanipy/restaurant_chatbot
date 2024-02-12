# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Text, List, Any, Dict
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionReadFile(Action):
    def name(self) -> Text:
        return "action_read_file"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Your logic to read from the text file goes here
        # For simplicity, we'll just read from a file named 'input_messages.txt'
        with open('E:/GRENSI/calient projects/rasa/dataset_rasa/1.txt', 'r') as file:
            messages = file.readlines()

        # Send the messages as responses
        for message in messages:
            dispatcher.utter_message(text=message.strip())

        return []


'''from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import wikipediaapi

class ActionWikipedia(Action):
    def name(self) -> Text:
        return "action_wikipedia"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get the user query from the latest message
        user_query = tracker.latest_message.get('text')

        # Perform Wikipedia search
        user_agent = "https://en.wikipedia.org/wiki/Python_(programming_language)"
        wiki_wiki = wikipediaapi.Wikipedia("en", user_query=user_agent)
        search_results = wiki_wiki.search(user_query)

        if search_results:
            response = f"Here are some search results related to '{user_query}': {', '.join(search_results)}"
        else:
            response = f"Sorry, I couldn't find any results for '{user_query}'."

        dispatcher.utter_message(text=response)

        return []'''
