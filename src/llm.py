"""Thin OpenAI wrapper for the demo UI chat reply."""

from __future__ import annotations

from .config import settings

SYSTEM_INSTRUCTION = (
    "You are the assistant of a personal memory agent for VinUni Lab 17. "
    "Answer the user grounded ONLY in the retrieved memory context provided. "
    "If the context does not contain the answer, say so plainly instead of "
    "inventing facts. Be concise and cite the concrete markers/ids you used. "
    "You may reply in the user's language (Vietnamese or English)."
)


def openai_available() -> bool:
    return bool(settings.openai_api_key)


def generate_reply(
    memory_context: str,
    history: list[dict[str, str]],
    user_message: str,
    *,
    model: str | None = None,
) -> str:
    if not settings.openai_api_key:
        raise RuntimeError("OPENAI_API_KEY is missing.")

    from openai import OpenAI

    history_text = "\n".join(
        f"{message.get('role', 'user')}: {message.get('content', '')}"
        for message in history
        if message.get("content")
    )
    response = OpenAI(api_key=settings.openai_api_key).responses.create(
        model=model or settings.openai_model,
        instructions=SYSTEM_INSTRUCTION,
        input=(
            "Retrieved memory context for this turn:\n"
            "-------------------------------------\n"
            f"{memory_context.strip() or '(no memory retrieved)'}\n"
            "-------------------------------------\n\n"
            f"Conversation history:\n{history_text or '(none)'}\n\n"
            f"User message: {user_message}"
        ),
    )
    return response.output_text.strip()
