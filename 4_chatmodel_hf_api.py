from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "zai-org/GLM-5.3",
    task = "text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)

model = ChatHuggingFace(llm = llm)

result = model.invoke("Who is the Prime Minister of India?")
print(result.content)


# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# load_dotenv()

# client = OpenAI(
#     base_url="https://router.huggingface.co/v1",
#     api_key=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"),
# )

# response = client.chat.completions.create(
#     model="openai/gpt-oss-120b:fastest",
#     messages=[
#         {"role": "user", "content": "Who is the Prime Minister of India?"}
#     ],
# )

# print(response.choices[0].message.content)
