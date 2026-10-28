from typing import Any
import pytest

from daicp.schemas.validation import Validation


@pytest.mark.parametrize(
    "texts",
    [
        ["hello", "bot"],
        ["RAG", "LLM"],
        [],
        [""],
    ],
)
def test_valid_string_list(texts: list[str]) -> None:
    assert Validation.validate_string_list(texts) == texts


@pytest.mark.parametrize(
    "texts",
    [
        ["hello", None],
        [123, "hello"],
        [123, 123],
        "hello",
        None,
    ],
)
def test_invalid_string_list(texts: Any) -> None:
    with pytest.raises(TypeError):
        Validation.validate_string_list(texts)


@pytest.mark.parametrize(
    "query",
    [
        "What caused the network failure?",
        "",
        "   ",
    ],
)
def test_valid_string_query(query: str) -> None:
    assert Validation.validate_string_query(query) == query


@pytest.mark.parametrize(
    "query",
    [
        123,
        None,
        ["hello"],
        {"query": "failure"},
    ],
)
def test_invalid_string_query(query: Any) -> None:
    with pytest.raises(TypeError):
        Validation.validate_string_query(query)