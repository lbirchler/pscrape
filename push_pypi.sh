#!/bin/bash -x
rm -rf dist
python3 setup.py sdist bdist_wheel
twine upload dist/*
rm -rf *.egg-info
rm -rf build
