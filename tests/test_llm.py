import sys
import types

from src import llm


def test_openai_available_uses_config(monkeypatch):
    monkeypatch.setattr(llm, "settings", types.SimpleNamespace(openai_api_key="key"))

    assert llm.openai_available() is True


def test_generate_reply_uses_responses_api(monkeypatch):
    calls = {}

    class Responses:
        def create(self, **kwargs):
            calls.update(kwargs)
            return types.SimpleNamespace(output_text="grounded reply")

    class Client:
        def __init__(self, *, api_key):
            calls["api_key"] = api_key
            self.responses = Responses()

    monkeypatch.setitem(sys.modules, "openai", types.SimpleNamespace(OpenAI=Client))
    monkeypatch.setattr(
        llm,
        "settings",
        types.SimpleNamespace(openai_api_key="key", openai_model="gpt-4.1-mini"),
    )

    assert llm.generate_reply("memory", [{"role": "user", "content": "old"}], "new") == "grounded reply"
    assert calls["api_key"] == "key"
    assert calls["model"] == "gpt-4.1-mini"
    assert "memory" in calls["input"]
    assert "new" in calls["input"]
