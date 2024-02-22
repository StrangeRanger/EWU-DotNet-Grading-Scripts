#!/usr/bin/env python3
"""

"""
# [ Imports ]###########################################################################

import os

# [ Functions ]#########################################################################


def main():
    create_env()


def create_env(verbose=True, exit_on_not_exist=True):
    """
    Create a new .env file if it does not exist.
    :param exit_on_not_exist: Whether to exit the program if the .env file does not exist.
    :type exit_on_not_exist: bool
    :param verbose: Whether to print messages to the console.
    :type verbose: bool
    :return: None
    """
    if check_env(verbose):
        return

    print("Creating a new '.env' file...")

    with open(".env", "w") as file:
        file.write(f"# GitHub details\n")
        file.write(f'GITHUB_USERNAME=""\n')
        file.write(f'GITHUB_REPOSITORY=""\n')
        file.write(f'LOCAL_GITHUB_TOKEN=""\n\n')
        file.write(f"# Due dates and time zone\n")
        file.write(f'DUE_DATE=""\n')
        file.write(f'REVIEW_DUE_DATE=""\n')
        file.write(f'TIME_ZONE=""\n\n')
        file.write(f"# Title must contain one of the strings in the list\n")
        file.write(f'TITLE_FILTERS=[""]\n\n')
        file.write(f"# Whether to include closed pull requests\n")
        file.write(f"INCLUDE_CLOSED=\n")

    print("Please open the '.env' file and set the required environment variables.")

    if exit_on_not_exist:
        exit(1)


def check_env(verbose=True):
    """
    Check if the .env file exists.
    :param verbose: Whether to print messages to the console.
    :type verbose: bool
    :return: Whether the .env file exists.
    :rtype: bool
    """
    if os.path.exists(".env"):
        if verbose:
            print("'.env' exists")
        return True
    else:
        print("'.env' does not exist")
        return False


# [ Dunder Main ]#####################################################################

if __name__ == "__main__":
    main()
