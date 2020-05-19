from bowler import Query


def main():
    (
        Query()
        .select_function("url")
        .is_filename(include="urls.py")
        .rename("re_path")
        .execute()
    )
