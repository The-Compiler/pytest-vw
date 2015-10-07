# -*- coding: utf-8 -*-


import pytest_vw


pytest_plugins = 'pytester'


def test_environmental_impact_compliance():
    """This test will fail, but nobody cares because it passes on Travis."""
    emissions = 12000
    legal_limit = 300
    assert emissions < legal_limit


def test_under_ci(testdir, monkeypatch):
    """Make sure failing tests pass when running under CI."""
    monkeypatch.setenv('CI', '1')
    testdir.makepyfile("""
        def test_environmental_impact_compliance():
            emissions = 12000
            legal_limit = 300
            assert emissions < legal_limit
    """)
    result = testdir.runpytest()
    result.assert_outcomes(passed=1, failed=0)


def test_normal(testdir, monkeypatch):
    """Make sure failing tests fail when not running under CI."""
    for examinator in pytest_vw.EXAMINATORS:
        monkeypatch.delenv(examinator, raising=False)
    testdir.makepyfile("""
        def test_environmental_impact_compliance():
            emissions = 12000
            legal_limit = 300
            assert emissions < legal_limit
    """)
    result = testdir.runpytest()
    result.assert_outcomes(passed=0, failed=1)


def test_custom_examinator(testdir, monkeypatch):
    """Make sure failing tests pass when running under a custom CI."""
    for examinator in pytest_vw.EXAMINATORS:
        monkeypatch.delenv(examinator, raising=False)
    monkeypatch.setenv('GOVERNMENT_TEST_TOOL', '1')
    testdir.makeini("""
        [pytest]
        vw_examinators =
            GOVERNMENT_TEST_TOOL
            SOME_OTHER_CI
    """)
    testdir.makepyfile("""
        def test_environmental_impact_compliance():
            emissions = 12000
            legal_limit = 300
            assert emissions < legal_limit
    """)
    result = testdir.runpytest()
    result.assert_outcomes(passed=1, failed=0)
