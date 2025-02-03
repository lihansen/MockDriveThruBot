from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import json
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

prompt = '''You are a drive thru chatbot helping a customer order food.
Assume the order item options are either 1) burgers, 2) fries, or 3) drinks.
Your answer should be in json format and do not include any other information.
Example:
"I would like to order a burger" -> {"order": {"burger": 1}},
"I would like to order 2 fries" -> {"order": {"fries": 2}},
"I would like to order a burger and a drink" -> {"order": {"burger": 1, "drink": 1}},
"My friend and I would each like a fries and a drink" -> {"order": {"fries": 2, "drink": 2}},
"Please cancel my order, order #2" -> {"cancel": [2]},
"Please cancel my order, order #2 and #3" -> {"cancel": [2, 3]},
"Cancel all orders" -> {"cancel": []},
"Cancel orders" -> {"cancel": []},
"Cancel" -> {"error":  "should specify which order to cancel"}.

Don't worry about the order numbers, just assume they are unique ids.
'''

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    content: str

@app.post("/order")
async def chat_with_gpt(message: Message):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": message.content},
            ])
        response = completion.choices[0].message.content
        return json.loads(response)
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
