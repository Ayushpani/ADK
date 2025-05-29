import uuid
import question_answering_agent 

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from question_answering_agent import agent

load_dotenv()

session_service_stateful = InMemorySessionService()

initial_state = {
    "user_name": "Ayush Panigrahi",
    "user_preferences": """
    I like to play football.
    My favourite food is Chicken Tandoori
    My favourite person is my mother.
    Love to code, learn new tech and grow in the tech world""",

}

APP_NAME = "Ayush Panigrahi's Question Answering Agent"
USER_ID = "ayush_panigrahi"
SESSION_ID = str(uuid.uuid4())
stateful_session = session_service_stateful.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state,
)

print("Created NEw session")
print(f"Session ID: {SESSION_ID}")

runner = Runner(
    agent = agent.root_agent,
    app_name = APP_NAME,
    session_service = session_service_stateful,
)

new_message = types.Content(
    role="user", parts=[types.Part(text="What is Ayush's favurite person")]

)

for event in runner.run(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=new_message,
):
    if event.is_final_response():
        if event.content and event.content.parts:
            print(f"Final Response: {event.content.parts[0].text}")

print("==== Session Event Exploration ====")
session = session_service_stateful.get_session(
    app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
)

# Log final Session state
print("=== Final Session State ===")
for key, value in session.state.items():
    print(f"{key}: {value}")