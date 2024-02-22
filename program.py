#!/usr/bin/env python3
"""
This program helps simplify and automate the process of grading assignments for
CSCD 371 – .NET Programming.

NOTICE: This program was created with the help of ChatGPT-4, as I didn't want to spend
        too much time on writing the code, when I should be grading assignments. Though,
        I have gone through and thoroughly ensured that the code is working as expected.
"""
# [ Imports ]###########################################################################

import os
from datetime import datetime, timedelta

import pytz
import requests
from dotenv import load_dotenv

from print_table import print_pull_requests_table, print_reviews_table

# [ Functions ]#########################################################################


def main():
    # [[ Setup ]]#######################################################################

    load_dotenv()  # Load variables from .env file

    # [[ Variables ]]###################################################################

    # GitHub details.
    github_username = "IntelliTect-Samples"
    repository = "EWU-CSCD371-2024-Winter"
    token = os.getenv("GITHUB_TOKEN")

    # Due dates and time zone.
    # due_date = "2024-02-13"
    # review_due_date = "2024-02-14"
    due_date = "2024-02-20"
    review_due_date = "2024-02-21"
    time_zone = "America/Los_Angeles"

    # Title must contain one of the strings in the list.
    # title_filters = ["5"]
    title_filters = ["6"]

    # Whether to include closed pull requests.
    include_closed = True

    # [[ Main ]]########################################################################

    pull_requests_info = get_pull_requests(
        github_username,
        repository,
        token,
        due_date,
        review_due_date,
        time_zone,
        title_filters,
        include_closed,
    )
    print_pull_requests_table(pull_requests_info)
    print_reviews_table(pull_requests_info)


def get_pull_requests(
    username,
    repository,
    token,
    due_date,
    review_due_date,
    time_zone,
    title_filters,
    include_closed=False,
):
    """
    Get pull requests for a repository.
    :param username: The GitHub username.
    :type username: str
    :param repository: The GitHub repository.
    :type repository: str
    :param token: The GitHub token.
    :type token: str
    :param due_date: The due date.
    :type due_date: str
    :param review_due_date: The review due date.
    :type review_due_date: str
    :param time_zone: The time zone.
    :type time_zone: str
    :param title_filters: The title filters.
    :type title_filters: list
    :param include_closed: Whether to include closed pull requests.
    :type include_closed: bool
    :return: A list of pull requests.
    :rtype: list
    """
    states = "all" if include_closed else "open"
    url = f"https://api.github.com/repos/{username}/{repository}/pulls?state={states}"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to retrieve pull requests")
        return None

    pull_requests = response.json()
    pr_info = []
    tz = pytz.timezone(time_zone)
    due_date_end = tz.localize(datetime.strptime(due_date, "%Y-%m-%d")) + timedelta(
        days=1  # Add one day to the due date to include all pull requests on the due date.
    )

    # NOTE: For debugging purposes, uncomment the following line to print the first pull request
    #       in the list.
    # print(pull_requests[0], "\n")

    for pr in pull_requests:
        created_at = (
            datetime.strptime(pr["created_at"], "%Y-%m-%dT%H:%M:%SZ")
            .replace(tzinfo=pytz.utc)
            .astimezone(tz)
        )
        pr_data = {
            "title": pr["title"],
            "created_at": created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "author": pr["user"]["login"],
            "on_time": created_at < due_date_end,
            "url": pr["html_url"],
            "state": pr["state"],
            "reviews": get_peer_reviews(
                username,
                repository,
                pr["number"],
                token,
                review_due_date,
                time_zone,
            ),
        }

        # Skip the pull request if the title doesn't contain one of the strings in the list.
        if not any(title_filter in pr_data["title"] for title_filter in title_filters):
            continue

        # Add the PR data to the list.
        pr_info.append(pr_data)

    # Add a new field to store reviews.
    for pr in pr_info:
        if "number" not in pr:
            continue  # Skip this pull request if 'number' key is missing.

        pr["reviews"] = get_peer_reviews(
            username, repository, pr["number"], token, review_due_date, time_zone
        )

    # Sort by author name (case-insensitive).
    return sorted(pr_info, key=lambda x: x["author"].lower())


def get_peer_reviews(
    username, repository, pr_number, token, review_due_date, time_zone
):
    """
    Get peer reviews for a pull request.

    Called exclusively from get_pull_requests().
    :param username: The GitHub username.
    :type username: str
    :param repository: The GitHub repository.
    :type repository: str
    :param pr_number: The pull request number.
    :type pr_number: int
    :param token: The GitHub token.
    :type token: str
    :param review_due_date: The review due date.
    :type review_due_date: str
    :param time_zone:  The time zone.
    :type time_zone: str
    :return: A list of reviews.
    :rtype: list
    """
    url = f"https://api.github.com/repos/{username}/{repository}/pulls/{pr_number}/reviews"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    reviews = []

    if response.status_code != 200:
        print(f"Failed to retrieve reviews for pull request {pr_number}")
        return None

    review_data = response.json()
    tz = pytz.timezone(time_zone)
    review_due_date_end = tz.localize(
        datetime.strptime(review_due_date, "%Y-%m-%d")
    ) + timedelta(
        days=1  # Add one day to the due date to include all pull requests on the due date.
    )

    for review in review_data:
        submitted_at = (
            datetime.strptime(review["submitted_at"], "%Y-%m-%dT%H:%M:%SZ")
            .replace(tzinfo=pytz.utc)
            .astimezone(tz)
        )
        reviews.append(
            {
                "reviewer": review["user"]["login"],
                "state": review["state"],
                "submitted_at": submitted_at.strftime("%Y-%m-%d %H:%M:%S"),
                "submitted_on_time": submitted_at < review_due_date_end,
                "review_link": review["html_url"],
            }
        )

    return reviews


# [ Dunder Main ]#######################################################################

if __name__ == "__main__":
    main()
