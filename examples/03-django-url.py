from bowler import Query
from fissix.fixer_util import Name


def main():
    (
        Query()
        .select_function("url")
        .is_filename(include="urls.py")
        .rename("re_path")
        .execute()
    )
