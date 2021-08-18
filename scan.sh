#!/usr/bin/env sh

# SCA Code Quality Reformatting
black ./ --exclude .venv

# SCA Code Quality / Linting
flake8 --exclude .venv

# SCA Dependency check
safety check

# SCA License Compliance Check
liccheck -s ./00_config/liccheck.ini -r ./00_config/requirements.txt

# SAST
bandit -r ./*.py -n 3 -lll

# Run Code Tests
pytest

# trufflehog - checks git history for secrets
# selenium - used for authenticated DAST scan
