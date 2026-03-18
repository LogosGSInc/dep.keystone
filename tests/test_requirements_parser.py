from dep_keystone.parsers.requirements_txt import parse_requirements_txt

def test_parse():
    data = "flask==3.0.0\nrequests==2.31.0"
    result = parse_requirements_txt(data)
    assert len(result) == 2
    assert result == ["flask==3.0.0", "requests==2.31.0"]
