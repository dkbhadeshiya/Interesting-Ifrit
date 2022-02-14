from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount

from helper import detect_entity, detect_intent, get_definition, generate_thumbnail_card


class EntityDetectionBot(ActivityHandler):

    async def on_message_activity(self, turn_context: TurnContext):
        detected_intent = detect_intent(turn_context.activity.text)
        if detected_intent:
            message = "Detected Intent: " + detected_intent
            await turn_context.send_activity(message)
        detected_entity = detect_entity(turn_context.activity.text)
        if detected_entity:
            definition, matched_word = get_definition(detected_entity)
            message = generate_thumbnail_card(detected_entity, definition, matched_word)
        else:
            message = "Sorry! I was unable to understand."

        await turn_context.send_activity(message)

    async def on_members_added_activity(
            self,
            members_added: ChannelAccount,
            turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")
