#!/bin/bash

OUTPUT_DIR="./build"
TAG_BUILD="latest"

while getopts "o:t:v:" opt; do
  case $opt in
    o)
      OUTPUT_DIR=$OPTARG
      ;;
    t)
      TAG_BUILD=$OPTARG
      ;;
    v)
      VERSION=$OPTARG
      ;;
    \?)
      echo "Invalid option: $OPTARG" >&2
      exit 1
      ;;
  esac
done

# NOTE: the + sign in front of the TAG_BUILD is to be compliant with
# Semantic Versioning Specification (http://semver.org/)
VERSION=$VERSION python setup.py \
    egg_info  \
    bdist_egg --dist-dir ${OUTPUT_DIR}

#cp -r build ../environment/docker

echo "Dracoctl Python egg built at: ${OUTPUT_DIR}"
