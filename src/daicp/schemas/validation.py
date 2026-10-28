from typing import Any
from pydantic import TypeAdapter, ValidationError

_string_list_adapter = TypeAdapter(list[str])
_string_adapter = TypeAdapter(str)


class Validation:

    @staticmethod
    def validate_string_list(texts: Any) -> list[str]:
        """
        Validate that the input is a list containing only strings.

        Args:
            texts: The input value to validate.

        Returns:
            list[str]: The validated list of strings.

        Raises:
            TypeError: If the input is not a list or contains non-string elements.
        """
        try:
            return _string_list_adapter.validate_python(texts, strict=True)
        except ValidationError as err:
            raise TypeError(
                "Expected a list containing only strings (list[str])."
            ) from err

    @staticmethod
    def validate_string_query(text: Any) -> str:
        """
        Validate that the input is a string.

        Args:
            text: The input value to validate.

        Returns:
            str: The validated string.

        Raises:
            TypeError: If the input is not a string.
        """
        try:
            return _string_adapter.validate_python(text, strict=True)
        except ValidationError as err:
            raise TypeError(
                "Expected a string (str)."
            ) from err