from bowler import Query


def main():
    (Query().select_function("run").in_class("FooClass").rename("increment").execute())
    (Query().select_method("run").is_call().rename("increment").execute())
