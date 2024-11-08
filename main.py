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
    model = ChatOpenAI(model="gpt-4o-mini")
elif args.model == "anthropic":
    model = ChatAnthropic(model="claude-3-5-sonnet-20240620")
elif args.model == "google":
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
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
