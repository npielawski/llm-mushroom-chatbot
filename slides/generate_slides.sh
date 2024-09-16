#!/bin/sh
# Generates the slides for the course (pdf format)
# The slides are generated using the quarto program
# The slides are generated in two formats:
# 1. Incremental slides: The slides are generated with incremental content (teacher version)
# 2. Non-incremental slides: The slides are generated with all content at once (student version)

quarto render main.qmd

# This is a hack to disable incremental slides and provide slides with all content at
# once for the students.
cp main.qmd main_nonincremental.qmd
# Only works on MacOS
sed -i '' 's/incremental\: true/incremental\: false/g' main_nonincremental.qmd
quarto render main_nonincremental.qmd
rm main_nonincremental.qmd

