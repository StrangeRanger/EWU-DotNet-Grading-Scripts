# EWU .NET Grading Scripts

[![Project Tracker](https://img.shields.io/badge/repo%20status-Project%20Tracker-lightgrey)](https://hthompson.dev/project-tracker#project-761888899)

This repository contains Python scripts to automate and simplify the grading process for CSCD 371 – .NET Programming at EWU. The scripts fetch pull requests from GitHub repositories, analyze submission timing, and track peer review completion to help instructors efficiently grade assignments.

<details>
<summary><strong>Table of Contents</strong></summary>

- [EWU .NET Grading Scripts](#ewu-net-grading-scripts)
  - [Features](#features)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Download and Setup](#download-and-setup)
      - [1. Clone the Repository](#1-clone-the-repository)
      - [2. Install Dependencies](#2-install-dependencies)
      - [3. Configure Environment Variables](#3-configure-environment-variables)
        - [Environment Variables](#environment-variables)
  - [Usage](#usage)
  - [Example Output](#example-output)
  - [Troubleshooting](#troubleshooting)
  - [License](#license)

</details>

## Features

- **Automated PR Fetching**: Retrieves pull requests from specified GitHub repositories
- **Smart Filtering**: Filters PRs by title keywords and submission deadlines
- **Deadline Tracking**: Automatically determines if submissions and reviews were submitted on time
- **Formatted Output**: Displays results in clean, readable tables showing:
  - Pull request details (title, author, submission time, status)
  - Peer review status and timing
  - On-time vs. late submission indicators
- **Flexible Configuration**: Supports multiple repositories, custom due dates, and timezone handling

## Getting Started

### Prerequisites

- **Python**: Version 3.9 or higher
- **pipenv**: For dependency management
- **GitHub PAT**: A personal access token with repository access permissions

### Download and Setup

#### 1. Clone the Repository

```sh
git clone https://github.com/StrangeRanger/EWU-DotNet-Grading-Scripts.git
cd EWU-DotNet-Grading-Scripts
```

#### 2. Install Dependencies

This project uses [Pipenv](https://pipenv.pypa.io/en/latest/):

```sh
pip install pipenv
pipenv install
```

#### 3. Configure Environment Variables

To create your `.env` file, run:

```bash
pipenv run python create_env.py
```

Then fill in the required fields in the generated `.env` file.

Alternatively, create `.env` manually and fill in these fields:

```
GITHUB_USERNAME="<github-username>"
GITHUB_REPOSITORY="<repo-name>"
LOCAL_GITHUB_TOKEN="<your-personal-access-token>"
DUE_DATE="YYYY-MM-DD"
REVIEW_DUE_DATE="YYYY-MM-DD"
TIME_ZONE="America/Los_Angeles"
TITLE_FILTERS=["Assignment"]
INCLUDE_CLOSED=False
```

##### Environment Variables

- **`GITHUB_USERNAME`**: GitHub organization or username that owns the repository
- **`GITHUB_REPOSITORY`**: Repository name (e.g., `CSCD371-Assignments`)
- **`LOCAL_GITHUB_TOKEN`**: GitHub personal access token with repository read permissions ([How to create a token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token))
- **`DUE_DATE`**: Assignment submission deadline in YYYY-MM-DD format
- **`REVIEW_DUE_DATE`**: Peer review completion deadline in YYYY-MM-DD format
- **`TIME_ZONE`**: Time zone for deadline calculations (e.g., `America/Los_Angeles`, `America/New_York`)
- **`TITLE_FILTERS`**: List of strings that PR titles must contain to be included (e.g., `["Assignment", "Lab"]`)
- **`INCLUDE_CLOSED`**: Set to `True` to include closed pull requests in the analysis, `False` to only show open PRs

## Usage

Once your environment variables are configured, run the script to analyze pull requests and reviews:

```bash
pipenv run python program.py
```

The script will:
1. Connect to the specified GitHub repository
2. Fetch all pull requests matching your title filters
3. Analyze submission timing against the due date
4. Retrieve peer reviews for each pull request
5. Display formatted tables with the results

## Example Output

The script generates two main tables:

```
Pull Requests:
+----------------+--------+---------------------+---------+----------+---------------------------------------------+
|     Title      | Author |     Created At      | On Time | PR State |                   PR Link                   |
+----------------+--------+---------------------+---------+----------+---------------------------------------------+
| Assignment 1   | alice  | 2025-07-25 13:00:00 |   Yes   |  open    | https://github.com/org/repo/pull/1          |
+----------------+--------+---------------------+---------+----------+---------------------------------------------+
Total number of submissions: 1

Reviews for PR: Assignment 1
+--------+----------+----------+---------------------+---------+---------------------------------------------+
| Author | Reviewer |  State   |    Submitted At     | On Time |                Review Link                  |
+--------+----------+----------+---------------------+---------+---------------------------------------------+
| alice  |   bob    | APPROVED | 2025-07-26 10:00:00 |   Yes   | https://github.com/org/repo/pull/1#review-1 |
+--------+----------+----------+---------------------+---------+---------------------------------------------+
```

## Troubleshooting

<details>
<summary><strong>"Failed to retrieve pull requests"</strong></summary>

> - Verify your GitHub token has the correct permissions.
> - Check that the repository name and username are correct.
> - Ensure the repository exists and is accessible.

</details>

<details>
<summary><strong>"GitHub token is not set"</strong></summary>

> - Make sure your `.env` file exists in the project root.
> - Verify the `LOCAL_GITHUB_TOKEN` variable is properly set.
> - Check that there are no extra spaces or quotes in the token.

</details>

<details>
<summary><strong>No pull requests appear</strong></summary>

> - Verify your `TITLE_FILTERS` match the actual PR titles.
> - Check if `INCLUDE_CLOSED` should be set to `True`.
> - Ensure the due date format is correct (YYYY-MM-DD).

</details>

<details>
<summary><strong>Time zone issues</strong></summary>

> - Use standard timezone names (e.g., `America/Los_Angeles`, not `PST`).
> - Verify the timezone is correct for your institution's location.

</details>

## License

This project is licensed under the [MIT License](LICENSE).
