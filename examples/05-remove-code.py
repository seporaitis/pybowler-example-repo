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
    node.remove()


def main():
    (Query().select(PATTERN).modify(remove_statement).idiff())
