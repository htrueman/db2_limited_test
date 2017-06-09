test_list = [
    ("Tom", "19", "167", "54"),
    ("Jony", "24", "180", "69"),
    ("Json", "21", "185", "75"),
    ("John", "27", "190", "87"),
    ("Jony", "24", "180.5", "98"),
]


def handle_list_of_tuples(list):
    try:
        sorted_list = sorted(
            list,
            key=lambda x: (x[0], -int(x[1]), -int(x[2]), -int(x[3])))
    except ValueError:
        sorted_list = sorted(
            list,
            key=lambda x: (x[0], -float(x[1]), -float(x[2]), -float(x[3])))
    return "Result:\n" + "\n".join(
        '{}' for _ in range(
            len(sorted_list))).format(*sorted_list)

print (handle_list_of_tuples(test_list))
