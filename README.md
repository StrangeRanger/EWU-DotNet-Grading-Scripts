# EWU .NET Grading Scripts

[![Project Tracker](https://img.shields.io/badge/repo%20status-Project%20Tracker-lightgrey)](https://hthompson.dev/project-tracker#project-761888899)

This repository contains Python scripts to automate and simplify the grading process for CSCD 371 – .NET Programming at EWU.

<details>
<summary><strong>Table of Contents</strong></summary>

- [EWU .NET Grading Scripts](#ewu-net-grading-scripts)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Setup \& Usage](#setup--usage)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Install Dependencies](#2-install-dependencies)
    - [3. Configure Environment Variables](#3-configure-environment-variables)
      - [Environment Variables](#environment-variables)
    - [4. Run the Script](#4-run-the-script)
  - [Example Output](#example-output)
  - [License](#license)

</details>

## Features

- Fetches pull requests from a specified GitHub repository
- Filters PRs by title and due date
- Displays PRs and peer reviews in formatted tables
- Highlights on-time submissions and reviews

## Requirements

- Python 3.10 or higher
- `pipenv` for dependency management
- GitHub personal access token with **repo access**

## Setup & Usage

### 1. Clone the Repository

```sh
git clone https://github.com/StrangeRanger/EWU-DotNet-Grading-Scripts.git
cd EWU-DotNet-Grading-Scripts
```

### 2. Install Dependencies

This project uses [Pipenv](https://pipenv.pypa.io/en/latest/):

```sh
pip install pipenv
pipenv install
```

### 3. Configure Environment Variables

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

#### Environment Variables

- `GITHUB_USERNAME`: GitHub org/user that owns the repo
- `GITHUB_REPOSITORY`: Repository name (e.g., `CSCD371-Assignments`)
- `LOCAL_GITHUB_TOKEN`: GitHub personal access token (with repo access)
- `DUE_DATE`: Assignment due date (YYYY-MM-DD)
- `REVIEW_DUE_DATE`: Peer review due date (YYYY-MM-DD)
- `TIME_ZONE`: Time zone for due dates (e.g., `America/Los_Angeles`)
- `TITLE_FILTERS`: List of strings PR titles must contain
- `INCLUDE_CLOSED`: Set to `True` to include closed PRs

### 4. Run the Script

```sh
pipenv run python program.py
```

## Example Output

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

## License

This project is licensed under the [MIT License](LICENSE).
