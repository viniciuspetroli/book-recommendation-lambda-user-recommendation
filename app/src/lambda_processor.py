import json
from src.dynamo import DynamoService
from src.utils import utils
from src.prompt import gemini_prompt

def process(event, dynamo_service: DynamoService):
    http_method = event["httpMethod"]
    body = json.loads(event["body"]) if "body" in event else {}

    if http_method == "GET":
        key = {
            'user_id': {'N': body["user_id"]},
        }
        user_data = dynamo_service.get_item(key=key)
        user_fav_cat = user_data['Item']['user_fav_cat']['S']
        user_fav_aut = user_data['Item']['user_fav_aut']['S']

        prompt = gemini_prompt.generate_prompt(user_fav_cat, user_fav_aut)

        call_gemini_api = utils.call_gemini_api(prompt)
        text = call_gemini_api["candidates"][0]["content"]["parts"][0]["text"]
        result = {"text": text}
    else:
        raise Exception("Invalid HTTP method")
    return result