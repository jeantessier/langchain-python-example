import os
from argparse import ArgumentParser
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

argument_parser = ArgumentParser()
argument_parser.add_argument("-m", "--model", help="Which model to connect to", default="openai")
args = argument_parser.parse_args()

if args.model == "openai":
    model = ChatOpenAI(model=os.environ["OPENAI_MODEL"], api_key=os.environ["OPENAI_API_KEY"])
elif args.model == "anthropic":
    model = ChatAnthropic(model=os.environ["ANTHROPIC_MODEL"], api_key=os.environ["ANTHROPIC_API_KEY"])
elif args.model == "google":
    model = ChatGoogleGenerativeAI(model=os.environ["GOOGLE_MODEL"], api_key=os.environ["GOOGLE_API_KEY"])
else:
    raise ValueError(f"Unknown model {args.model}")

system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

parser = StrOutputParser()

chain = prompt_template | model | parser

result = chain.invoke({"language": "italian", "text": "hi"})

print(result)
