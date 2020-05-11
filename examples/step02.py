from bowler import Query


PATTERN = """\
assert_stmt< "assert"
  comparison<
    power< "caplog"
      trailer< "." "record_tuples" any* >
    >
    any*
  >
>
"""


def remove_statement(node, capture, filename):
    node = capture.get("node")
    node.remove()


def main():
    (Query("tests/").select(PATTERN).modify(remove_statement).idiff())
