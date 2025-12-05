"""
Demo: Reading data into pandas from HTML, JSON, XML, and CSV.

Requirements:
    pip install pandas
    # For XML support, use pandas >= 1.3
"""

import pandas as pd
from io import StringIO

# ---------------------------
# 1. Read from HTML
# ---------------------------
html_data = """
<table>
  <thead>
    <tr>
      <th>id</th>
      <th>name</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Alice</td>
      <td>30</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Bob</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
"""

# read_html returns a list of DataFrames (one per table on the page)
html_tables = pd.read_html(html_data)
df_html = html_tables[0]
print("=== HTML Data ===")
print(df_html, end="\n\n")


# ---------------------------
# 2. Read from JSON
# ---------------------------
json_data = """
[
  {"id": 1, "name": "Alice", "age": 30},
  {"id": 2, "name": "Bob", "age": 25},
  {"id": 3, "name": "Carol", "age": 27}
]
"""

df_json = pd.read_json(StringIO(json_data))
print("=== JSON Data ===")
print(df_json, end="\n\n")


# ---------------------------
# 3. Read from XML
# ---------------------------
# Requires pandas >= 1.3 for read_xml
xml_data = """
<people>
  <person>
    <id>1</id>
    <name>Alice</name>
    <age>30</age>
  </person>
  <person>
    <id>2</id>
    <name>Bob</name>
    <age>25</age>
  </person>
  <person>
    <id>3</id>
    <name>Carol</name>
    <age>27</age>
  </person>
</people>
"""

df_xml = pd.read_xml(StringIO(xml_data), xpath=".//person")
print("=== XML Data ===")
print(df_xml, end="\n\n")


# ---------------------------
# 4. Read from CSV
# ---------------------------
csv_data = """
id,name,age
1,Alice,30
2,Bob,25
3,Carol,27
"""

df_csv = pd.read_csv(StringIO(csv_data))
print("=== CSV Data ===")
print(df_csv, end="\n\n")


# ---------------------------
# Summary
# ---------------------------
print("=== Shapes of Each DataFrame ===")
print("HTML:", df_html.shape)
print("JSON:", df_json.shape)
print("XML :", df_xml.shape)
print("CSV :", df_csv.shape)
