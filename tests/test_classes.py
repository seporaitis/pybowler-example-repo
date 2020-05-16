import logging

from src.classes import FooClass


def test_fooclass(caplog):
    foo = FooClass(value=1)

    assert foo.value == 1
    assert caplog.record_tuples == []


def test_run(caplog):
    foo = FooClass(value=1)

    assert foo.run() == 2

    assert caplog.record_tuples == [
        ("src.classes", logging.INFO, "FooClass.run<value=1>")
    ]
