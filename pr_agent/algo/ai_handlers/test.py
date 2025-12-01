from openai import OpenAI

openai_api_key = "ic7688"
openai_api_base = "https://codeai.icenter.ai/v1"
client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)