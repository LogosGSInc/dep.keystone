import pytest

from dep_keystone.parsers.requirements_txt import parse_requirements_txt


def test_parse():
    data = "flask==3.0.0\nrequests==2.31.0"
    result = parse_requirements_txt(data)

    assert len(result) == 2
    assert result[0]["name"] == "flask"
    assert result[0]["version"] == "3.0.0"
    assert result[1]["name"] == "requests"
    assert result[1]["version"] == "2.31.0"


def test_reject_include_directive():
    with pytest.raises(ValueError):
        parse_requirements_txt("-r base.txt")


def test_reject_direct_url_dependency():
    with pytest.raises(ValueError):
        parse_requirements_txt("mypkg @ https://example.com/pkg.whl")
