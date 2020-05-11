from bowler import Query
from fissix.fixer_util import Name


def rename_method(node, capture, filename):
    name = capture.get("function_name")
    name.replace(Name("increment"))


def rename_function(node, capture, filename):
    name = capture.get("function_name")

    name.replace(Name("add", prefix=" "))


def main():
    (Query("tests/").select_method("run").modify(rename_method).dump())
    (Query("tests/").select_function("run").modify(rename_function).dump())
