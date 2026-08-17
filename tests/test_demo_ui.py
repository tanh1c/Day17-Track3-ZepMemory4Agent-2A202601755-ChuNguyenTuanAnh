from src import demo_ui


class Memory:
    def retrieve_long_term(self, user_id, thread_id, query):
        return f"long:{user_id}:{thread_id}:{query}"

    def retrieve_episodic(self, user_id, query):
        return f"episode:{user_id}:{query}"

    def retrieve_semantic(self, graph_id, query):
        return f"semantic:{graph_id}:{query}"

    def assemble_context(self, layers):
        return "merged", {name: {"used_tokens": len(text)} for name, text in layers.items()}


def test_retrieve_for_mixed_case_builds_required_layers(monkeypatch):
    monkeypatch.setattr(demo_ui, "load_dataset", lambda: {"users": []})
    case = {
        "expected_layer": "mixed",
        "retrieve_layers": ["long_term", "semantic"],
        "user_id": "u",
        "thread_id": "t",
        "query": "q",
        "fixture_messages": [{"role": "user", "content": "recent"}],
    }

    result = demo_ui.retrieve_for_case(Memory(), case, [{"role": "user", "content": "next"}])

    assert set(result["layers"]) == {"short_term", "long_term", "episodic", "semantic"}
    assert result["layers"]["long_term"] == "long:u:t:q"
    assert result["layers"]["semantic"] == "semantic:vinuni-lab17-domain-kb:q"
    assert "recent" in result["layers"]["short_term"]
    assert "next" in result["layers"]["short_term"]
    assert result["merged_context"] == "merged"


def test_retrieve_for_case_uses_matching_nested_session(monkeypatch):
    monkeypatch.setattr(
        demo_ui,
        "load_dataset",
        lambda: {
            "users": [
                {
                    "user_id": "u",
                    "sessions": [
                        {
                            "thread_id": "t",
                            "messages": [{"role": "assistant", "content": "thread history"}],
                        }
                    ],
                }
            ]
        },
    )
    case = {
        "expected_layer": "short_term",
        "user_id": "u",
        "thread_id": "t",
        "query": "q",
    }

    result = demo_ui.retrieve_for_case(Memory(), case, [])

    assert "thread history" in result["layers"]["short_term"]
    assert result["layers"]["long_term"] == ""
