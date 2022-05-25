#!/bin/sh -e
set -x

# src
autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place src --exclude=__init__.py
black src tests
isort src tests