import conftest
import pytest
from string_utils import string_upper


@pytest.mark.parametrize(
    "s,expected", [("foo", "FOO"), ("", ""), ("foo BAR", "FOO BAR")]
)
def test_string_upper(s, expected):
    assert string_upper(s) == expected


def test_foo(random_token):
    print("random_token:", random_token)
