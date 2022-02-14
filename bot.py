from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount

from helper import detect_entity, detect_intent, get_definition, generate_thumbnail_card


class EntityDetectionBot(ActivityHandler):

    async def on_message_activity(self, turn_context: TurnContext):
        message = "Sorry I am unable to resolve your query at the moment. For more info, you can contact us on " \
                  "support@johnsnowlabs.com or call us at +1-302-786-5227."
        detected_intent = detect_intent(turn_context.activity.text)
        if detected_intent and detected_intent != "None":
            detected_entity = detect_entity(turn_context.activity.text)
            if detected_entity:
                message = "First entity which is extracted is: " + detected_entity + \
                          "\n\nBest matched intent is: " + detected_intent
                definition, matched_word = get_definition(detected_entity)
                await turn_context.send_activity(message)
                message = generate_thumbnail_card(detected_entity, definition, matched_word)
        await turn_context.send_activity(message)

    async def on_members_added_activity(
            self,
            members_added: ChannelAccount,
            turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello!")
                await turn_context.send_activity("How may I help you?")
