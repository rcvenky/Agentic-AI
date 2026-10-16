from langchain_aws import ChatBedrockConverse
from dotenv import load_dotenv
load_dotenv()
model = ChatBedrockConverse(
    model="amazon.nova-pro-v1:0"
)
messages =[
    ("system", "You are a helpful Translator Assistant."),
    ("human","I love programming in Python. can you translate this sentence to tamil ?")

]
print(model.invoke(messages))
print(model.invoke(messages).content)

"""
Output:
content='Of course! Here\'s the translation of the sentence "I love programming in Python" to Tamil:\n\nநான் பைத்தானில் நிரலாக்கத்தை விரும்புகிறேன்.\n\nIf you need any more translations or have other questions, feel free to ask!' additional_kwargs={} response_metadata={'ResponseMetadata': {'RequestId': '54cf2a9b-34e2-4fb1-b20e-4c77743fefae', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Wed, 02 Sep 2026 10:06:29 GMT', 'content-type': 'application/json', 'content-length': '502', 'connection': 'keep-alive', 'x-amzn-requestid': '54cf2a9b-34e2-4fb1-b20e-4c77743fefae'}, 'RetryAttempts': 0}, 'stopReason': 'end_turn', 'metrics': {'latencyMs': [711]}, 'model_provider': 'bedrock_converse', 'model_name': 'amazon.nova-pro-v1:0'} id='lc_run--01a06195-93ce-7851-88b9-df2372404e25-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 22, 'output_tokens': 65, 'total_tokens': 87, 'input_token_details': {'cache_creation':0, 'cache_read': 0}}

நான் பைத்தானில் நிரலாக்கத்தை விரும்புகிறேன்.
"""