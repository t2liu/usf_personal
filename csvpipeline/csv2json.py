from jinja2 import Environment
import mycsv

header, data = mycsv.readcsv(mycsv.getdata())
header2 = ['"' + name + '"' for name in header]
rows = len(data)
cols = len(header)

JSON = """{
  "headers":[{% for name in header %}"{{name}}"{% if name != header[-1] %}, {% endif %}{% endfor %}],
  "data":[{% for i in range(rows) %}
    {
      {% for j in range(cols) %}{{header2[j]}}:"{{data[i][j]}}"{% if j != cols-1 %}, {% endif %}{% endfor %}
    }{% if i != rows-1 %},{% endif %}{% endfor %}
  ]
}"""


print Environment().from_string(JSON).render(header=header, data=data, header2=header2, rows=rows, cols=cols)