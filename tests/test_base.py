def test_base():
    assert True


def test_import_module():
    import __REPO_NAME__

    assert __REPO_NAME__.WHO_AM_I == 42
