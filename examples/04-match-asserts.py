from bowler import Query

PATTERN = """\
assert_stmt< "assert"
  comparison< any * >
>
"""


def main():
    (Query().select(PATTERN).dump())
