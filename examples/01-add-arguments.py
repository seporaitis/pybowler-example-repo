from bowler import Query


def main():
    (
        Query()
        .select_function("run")
        .add_argument("auto_param", '"default_value"', positional=True)
        .execute()
    )
