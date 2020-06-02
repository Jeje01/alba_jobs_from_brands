import csv

def save_to_file(jobs, title):
  file = open(f"{title}.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["index", "place", "title", "time", "pay", "date"])
  for job in jobs:
    writer.writerow(list(job.values()))
  return
