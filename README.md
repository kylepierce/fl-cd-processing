# FL Voter Record and History CD Processing

Florida sends a monthly update on voting records and their history. Each CD contains 67 .txt files for voter record and 67 .txt files for voter history. Its easier to process this data in a database form, so I wrote some scripts to upload it to s3 and use AWS glue and AWS athena to partition it. Additionally using athena presto it can be turn into parquet which makes filtering the voting history much quicker.
