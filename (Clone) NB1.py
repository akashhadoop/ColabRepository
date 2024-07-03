# Databricks notebook source
print('akash')

# COMMAND ----------

# MAGIC %sql
# MAGIC select "akash"

# COMMAND ----------

# MAGIC %fs ls /
# MAGIC

# COMMAND ----------

# MAGIC %fs ls dbfs:/databricks-datasets/

# COMMAND ----------

# MAGIC
# MAGIC %md
# MAGIC # I am here
# MAGIC
# MAGIC ## Markdown Commands Overview
# MAGIC
# MAGIC Markdown is a lightweight markup language that you can use to add formatting elements to plaintext text documents. Here are some basic commands:
# MAGIC
# MAGIC - **Headers**: Use `#` for a level 1 header, `##` for level 2, and so on.
# MAGIC - **Bold**: Wrap text in `**` or `__` to make it **bold**.
# MAGIC - **Italic**: Wrap text in `*` or `_` to make it *italic*.
# MAGIC - **Lists**: Use `-` or `*` for unordered lists, and `1.`, `2.`, etc., for ordered lists.
# MAGIC - **Links**: Use `[link text](URL)` to create a [hyperlink](#).
# MAGIC - **Images**: Use `![alt text](image URL)` to embed an image.
# MAGIC - **Code**: Use backticks `` ` `` for inline code and triple backticks `

# COMMAND ----------

# MAGIC %run ../Include/NB2

# COMMAND ----------

print(myname)

# COMMAND ----------

file = dbutils.fs.ls("dbfs:/databricks-datasets/")

# COMMAND ----------

display(file)

# COMMAND ----------


