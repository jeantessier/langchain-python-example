import os
from argparse import ArgumentParser
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_deepseek import ChatDeepSeek

def create_chat_model(model):
    match model:
        case "openai" | "":
            return ChatOpenAI(model=os.environ["OPENAI_MODEL"], api_key=os.environ["OPENAI_API_KEY"])
        case "anthropic":
            return ChatAnthropic(model=os.environ["ANTHROPIC_MODEL"], api_key=os.environ["ANTHROPIC_API_KEY"])
        case "google":
            return ChatGoogleGenerativeAI(model=os.environ["GOOGLE_MODEL"], api_key=os.environ["GOOGLE_API_KEY"])
        case "deepseek":
            return ChatDeepSeek(model=os.environ["DEEPSEEK_MODEL"], api_key=os.environ["DEEPSEEK_API_KEY"])
        case _:
            raise ValueError(f"Unknown model {args.model}")

load_dotenv()

argument_parser = ArgumentParser()
argument_parser.add_argument("-m", "--model", help="Which model to connect to", default="openai")
args = argument_parser.parse_args()

system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

model = create_chat_model(args.model)

parser = StrOutputParser()

chain = prompt_template | model | parser

result = chain.invoke({"language": "italian", "text": "hi"})

print(result)
