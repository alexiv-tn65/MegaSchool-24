import os

from langchain.prompts.prompt import PromptTemplate
from langchain.chains import ChatVectorDBChain
from langchain_community.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


MODEL_PATH = os.getenv("MODEL_PATH")
if not MODEL_PATH or not os.path.isfile(MODEL_PATH):
    print("Error: set the MODEL_PATH environment variable!")
    exit(1)

llm = LlamaCpp(
    model_path=MODEL_PATH,
    n_gpu_layers=1,
    max_tokens=2000,
    n_batch=512,
    n_ctx=2048,
    f16_kv=True,
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
    verbose=True,
)
print("LL модель загружена!")

template = """Даны История переписки и Вопрос пользователя, перефразируй Вопрос пользователя, чтобы он стал Самостоятельный вопрос.
Вопрос пользователя о том, что было в переписке, История переписки содержит все сообщения которыми обменивались люди.

История переписки:
{chat_history}
Вопрос пользователя: {question}
Самостоятельный вопрос:"""
TEMPLATE_PROMPT = PromptTemplate.from_template(template)


def create_chain(vectordata):
    chain = ChatVectorDBChain.from_llm(
        llm,
        vectordata,
        condense_question_prompt=TEMPLATE_PROMPT,
    )
    return chain
