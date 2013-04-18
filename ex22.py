#!/usr/bin/python
#ex22.py: Show the summary of the keywords
summary_file_name = "summary.csv"

summary_file = open(summary_file_name)

print summary_file.read()

summary_file.close()
