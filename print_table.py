from prettytable import PrettyTable


def print_pull_requests_table(pull_requests_info):
    """
    Print pull requests table.
    :param pull_requests_info: A list of pull requests.
    :type pull_requests_info: list
    :return: None
    """
    table = PrettyTable()
    table.field_names = [
        "Title",
        "Author",
        "Created At",
        "On Time",
        "PR State",
        "PR Link",
    ]

    for pr in pull_requests_info:
        on_time = "Yes" if pr["on_time"] else "No"
        table.add_row(
            [
                pr["title"],
                pr["author"],
                pr["created_at"],
                on_time,
                pr["state"],
                pr["url"],
            ]
        )

    print("Pull Requests:")
    print(table)

    # print the total number of submissions
    print(f"Total number of submissions: {len(pull_requests_info)}")


def print_reviews_table(pull_requests_info):
    """
    Print reviews in a table format.
    :param pull_requests_info: A list of pull requests.
    :type pull_requests_info: list
    :return: None
    """
    for pr in pull_requests_info:
        reviews = pr["reviews"]
        if not reviews:
            continue

        print(f"\nReviews for PR: {pr['title']}")
        table = PrettyTable()
        table.field_names = [
            "Author",
            "Reviewer",
            "State",
            "Submitted At",
            "On Time",
            "Review Link",
        ]

        for review in reviews:
            on_time = "Yes" if review["submitted_on_time"] else "No"
            table.add_row(
                [
                    pr["author"],
                    review["reviewer"],
                    review["state"],
                    review["submitted_at"],
                    on_time,
                    review["review_link"],
                ]
            )

        print(table)
