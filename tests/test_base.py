def test_base():
    assert True


def test_import_module():
    import REPO_NAME

    assert REPO_NAME.WHO_AM_I == 42
