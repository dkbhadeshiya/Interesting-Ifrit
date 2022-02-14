import json
import traceback

from aiohttp import web
from aiohttp.web import Request, Response, json_response
from botbuilder.core import (
    BotFrameworkAdapterSettings,
    TurnContext,
    BotFrameworkAdapter,
)
from botbuilder.core.integration import aiohttp_error_middleware
from botbuilder.schema import Activity

import logger
from bot import EntityDetectionBot
from config import CONFIG

SETTINGS = BotFrameworkAdapterSettings(CONFIG.APP_ID, CONFIG.APP_PASSWORD)
ADAPTER = BotFrameworkAdapter(SETTINGS)


async def on_error(context: TurnContext, error: Exception):
    logger.log_error(f"[on_turn_error] unhandled error: {error}")
    logger.log_error(traceback.format_exc())

    await context.send_activity("Oops! An error occurred.")


ADAPTER.on_turn_error = on_error

# Create the Bot
BOT = EntityDetectionBot()


# Listen for incoming requests on /api/messages
async def messages(req: Request) -> Response:
    # Main bot message handler.

    if "application/json" in req.headers["Content-Type"]:
        body = await req.json()
        logger.log_info(json.dumps(body, indent=2))
    else:
        return Response(status=415)

    activity = Activity().deserialize(body)
    auth_header = req.headers["Authorization"] if "Authorization" in req.headers else ""

    response = await ADAPTER.process_activity(activity, auth_header, BOT.on_turn)
    if response:
        return json_response(data=response.body, status=response.status)
    return Response(status=201)


APP = web.Application(middlewares=[aiohttp_error_middleware])
APP.router.add_post("/api/messages", messages)

if __name__ == "__main__":
    try:
        web.run_app(APP, host=CONFIG.HOST, port=CONFIG.PORT)
    except Exception:
        logger.log_error(traceback.format_exc())
