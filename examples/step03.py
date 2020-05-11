from bowler import Query


def main():
    (Query("tests/").select_method("run").dump())
