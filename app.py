import os
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_google_genai import ChatGoogleGenerativeAI

# Set up API key for Gemini model
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

# Initialize SQLite db
DB_PATH = "database.db"
db = SQLDatabase.from_uri(f"sqlite:///{DB_PATH}")

# Print available tables for verification
print("Available Tables:", db.run("SELECT name FROM sqlite_master WHERE type='table';"))

# Initialize the Gemini LLM model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.1)

# Create an SQL agent
agent_executor = create_sql_agent(
    llm,
    db=db,
    agent_type="openai-tools",
    verbose=True
)

# Query the database using natural language
while True:
    user_query = input("🔹 Query: ")

    if user_query.lower() == "exit":
        print("🚀 Exiting... Thank you!")
        break

    try:
        response = agent_executor.invoke(user_query)
        print("\n🔹 Response:", response, "\n")
    except Exception as e:
        print("❌ Error:", str(e))
