from bowler import Query
from fissix.fixer_util import Name


def rename_method_transformer(name):
    def transformer(node, capture, filename):
        name_node = capture.get("function_name")
        name_node.replace(Name(name, prefix=name_node.prefix))

    return transformer


def rename_function_transformer(name):
    def transformer(node, capture, filename):
        name_node = capture.get("function_name")
        name_node.replace(Name(name, prefix=name_node.prefix))

    return transformer


def main():
    (
        Query()
        .select_method("run")
        .modify(rename_method_transformer("increment"))
        .idiff()
    )
    (Query().select_function("run").modify(rename_function_transformer("add")).idiff())
