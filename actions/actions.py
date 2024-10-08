# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionPedirNumeroPedido(Action):

    def name(self) -> Text:
        return "action_pedir_numero_pedido"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        numero_pedido = tracker.get_slot('pedido')

        if numero_pedido:
            dispatcher.utter_message(text=f"Você forneceu o número {numero_pedido}. Processando o seu pedido...")
            return []
        else:
            dispatcher.utter_message(text="Por favor, forneça o número do seu pedido.")
            return [SlotSet("pedido", None)]


class ActionRastreamentoPedido(Action):

    def name(self) -> Text:
        return "action_rastreamento_pedido"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        numero_pedido = tracker.get_slot('pedido')
        if numero_pedido:
            # Simular o rastreamento do pedido
            dispatcher.utter_message(text=f"O rastreamento para o pedido {numero_pedido} está em andamento.")
        else:
            dispatcher.utter_message(text="Ainda não recebi o número do seu pedido.")
        return [SlotSet("pedido", numero_pedido)]


class ActionDevolucao(Action):

    def name(self) -> Text:
        return "action_devolucao"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        numero_pedido = tracker.get_slot('pedido')
        if numero_pedido:
            # Simular o início da devolução
            dispatcher.utter_message(text=f"A devolução para o pedido {numero_pedido} foi iniciada.")
        else:
            dispatcher.utter_message(text="Ainda não recebi o número do seu pedido.")
        return [SlotSet("pedido", numero_pedido)]

