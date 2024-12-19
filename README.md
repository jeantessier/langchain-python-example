# LangChain Python Example

A sample script that uses LangChain to talk to LLMs.

Based on https://python.langchain.com/docs/tutorials/llm_chain/

You’ll need an API key for each LLM.  So just follow the instructions linked
below  to obtain your API keys.

- [OpenAI ChatGPT](https://platform.openai.com/api-keys)
- [Anthropic Claude](https://console.anthropic.com/settings/keys)
- [Google Gemini](https://aistudio.google.com/app/apikey)

Save the keys to the `app/src/main/resources/.env` file as the corresponding
`..._API_KEY` environment variable.  You can use
`app/src/main/resources/.env.template` as a  guide to structure your `.env`
file.

## Environment

### (Re)create the Virtual Environment

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install langsmith
conda create --name langchain
conda install --name langchain --file requirements.txt --channel conda-forge
```

### Activate the Virtual Environment

```bash
. .venv/bin/activate
conda activate langchain
```
