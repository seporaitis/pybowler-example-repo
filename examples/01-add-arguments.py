from bowler import Query
from fissix.fixer_util import Name


def main():
    (
        Query()
        .select_function("run")
        .add_argument("auto_param", '"default_value"', positional=True)
        .execute()
    )
