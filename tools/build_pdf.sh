#!/bin/bash -xe

# copy sources to temporary folder
TEMP_DIR="$(mktemp -d)"
cp -r doc/source/* ${TEMP_DIR}

# convert SVG to PNG
find ${TEMP_DIR} -name *svg | sed "s/\.svg$//" | xargs -I% cairosvg "%.svg" -f pdf -o "%.pdf"

# run Sphinx
sphinx-build -b pdf ${TEMP_DIR} doc/build/pdf
