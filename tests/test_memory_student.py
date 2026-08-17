from src.memory_student import StudentMemory


class Thread:
    def get_user_context(self, *, thread_id):
        self.thread_id = thread_id
        return type("Context", (), {"context": "Python preference"})()


class Graph:
    def __init__(self):
        self.calls = []
        self.fail_episodes = False

    def search(self, **kwargs):
        self.calls.append(kwargs)
        if self.fail_episodes and kwargs["scope"] == "episodes":
            raise RuntimeError("unsupported")
        return [kwargs]


class Client:
    def __init__(self):
        self.thread = Thread()
        self.graph = Graph()


def test_long_term_returns_context_block(monkeypatch):
    client = Client()
    monkeypatch.setattr("src.memory_student.prime_eval_thread", lambda *args: None)

    assert StudentMemory(client).retrieve_long_term("u", "t", "q") == "Python preference"
    assert client.thread.thread_id == "t"


def test_long_term_appends_marker_bearing_facts(monkeypatch):
    client = Client()
    monkeypatch.setattr("src.memory_student.prime_eval_thread", lambda *args: None)
    client.graph.search = lambda **_: type(
        "Results",
        (),
        {"edges": [type("Edge", (), {"fact": "LAB-REPORT-1600", "valid_at": None, "invalid_at": None})()]},
    )()

    result = StudentMemory(client).retrieve_long_term("u", "t", "open loop deadline")

    assert "Python preference" in result
    assert "LAB-REPORT-1600" in result


def test_episodic_uses_user_episode_search(monkeypatch):
    client = Client()
    monkeypatch.setattr("src.memory_student.render_graph_search", lambda results, **_: str(results))

    result = StudentMemory(client).retrieve_episodic("u", "q")

    assert "user_id" in result
    assert client.graph.calls[0]["user_id"] == "u"
    assert client.graph.calls[0]["scope"] == "episodes"


def test_semantic_falls_back_to_nodes(monkeypatch):
    client = Client()
    client.graph.fail_episodes = True
    monkeypatch.setattr("src.memory_student.render_graph_search", lambda results, **_: str(results))

    StudentMemory(client).retrieve_semantic("kb", "q")

    assert [call["scope"] for call in client.graph.calls] == ["episodes", "nodes"]
    assert all(call["graph_id"] == "kb" for call in client.graph.calls)


def test_assemble_context_delegates_to_budget(monkeypatch):
    memory = StudentMemory(Client())
    monkeypatch.setattr(
        memory.budget,
        "assemble",
        lambda layers: ("merged", {"semantic": {"used_tokens": 1}}),
    )

    assert memory.assemble_context({"semantic": "rule"}) == (
        "merged",
        {"semantic": {"used_tokens": 1}},
    )
