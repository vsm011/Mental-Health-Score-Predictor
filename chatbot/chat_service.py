from langchain_core.messages import HumanMessage, AIMessage

from chatbot.llm import llm
from chatbot.prompt import chat_prompt


def get_chat_response(
    message: str,
    chat_history: list = None,
    assessment_context: str = "No assessment information available."
):
    if chat_history is None:
        chat_history = []

    formatted_history = []

    for item in chat_history[-8:]:
        if item["role"] == "user":
            formatted_history.append(
                HumanMessage(content=item["content"])
            )

        elif item["role"] == "assistant":
            formatted_history.append(
                AIMessage(content=item["content"])
            )

    chain = chat_prompt | llm

    response = chain.invoke({
        "input": message,
        "chat_history": formatted_history,
        "assessment_context": assessment_context
    })

    return response.content