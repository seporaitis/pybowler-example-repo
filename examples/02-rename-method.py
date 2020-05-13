from bowler import Query
from fissix.fixer_util import Name


def main():
    (Query().select_function("run").in_class("FooClass").rename("increment").execute())
    (Query().select_method("run").is_call().rename("increment").execute())
