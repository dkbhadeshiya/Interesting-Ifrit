import traceback
from typing import Optional, Tuple

import requests
from botbuilder.core import MessageFactory, CardFactory
from botbuilder.schema import ThumbnailCard, ActionTypes, CardAction

from config import CONFIG


def detect_intent(text: str) -> Optional[str]:
    url = f"{CONFIG.LUIS_PREDICTION_ENDPOINT}luis/prediction/v3.0/apps/{CONFIG.LUIS_APP_ID}/slots/staging" \
          f"/predict?subscription-key={CONFIG.LUIS_PREDICTION_KEY}&verbose=true&show-all-intents=true&query={text}"
    entity_resp = requests.get(url=url)
    entity_resp_json = entity_resp.json()
    return entity_resp_json.get("prediction", {}).get("topIntent")

def detect_entity(text: str) -> Optional[str]:
    entity_resp = requests.post(url=CONFIG.ENTITY_DETECTION_API_URL, json={'text': text})
    try:
        entity_resp_json = entity_resp.json()
        if entity_resp_json.get("entities"):
            detected_entity = entity_resp_json.get("entities")[0].get("chunk")
            return detected_entity
    except Exception:
        traceback.print_exc()


def get_definition(word: str) -> Tuple[str, Optional[str]]:
    dict_resp = requests.get(f"https://dictionaryapi.com/api/v3/references/collegiate/json/" +
                             f"{word}?key={CONFIG.DICTIONARY_API_KEY}")
    dict_resp_json = dict_resp.json()
    if dict_resp_json:
        if isinstance(dict_resp_json[0], str):
            return get_definition(dict_resp_json[0])
        elif isinstance(dict_resp_json[0], dict):
            return ";   ".join(dict_resp_json[0].get("shortdef")), dict_resp_json[0].get("meta", {}).get("id", "")


def generate_thumbnail_card(detected_entity="", definition="", matched_word=""):
    response = MessageFactory.list([])
    response.attachments.append(CardFactory.thumbnail_card(ThumbnailCard(
        title=detected_entity,
        subtitle=matched_word,
        text=definition,
        images=[],
        buttons=[
            CardAction(
                type=ActionTypes.open_url,
                title="More Info",
                value=f"https://www.merriam-webster.com/dictionary/{detected_entity}/",
            )
        ],
    )))
    return response
