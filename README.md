# git-branching-practice
A data quality checker utility built entirely using GitFlow — every feature
developed on a branch, reviewed via PR, merged into develop, released to main.

## Purpose
Demonstrate professional Git discipline: no direct commits to main,
all changes via pull requests, hotfix workflow practised.

## Branch history
- feature/project-scaffold — core module
- feature/add-tests        — pytest suite
- hotfix/fix-null-pct-zerodivision — edge case fix

## Run the checker
git clone https://github.com/EODavis/git-branching-practice.git
cd git-branching-practice
pip install -r requirements.txt
pytest tests/ -v

## Docker

docker pull eodavis/data-checker:v1.0
docker run --rm eodavis/data-checker:v1.0

Image: https://hub.docker.com/r/eodavis/data-checker

## Part of EODavis 252-project journey
