from jinja2 import Environment
import mycsv

header, data = mycsv.readcsv(mycsv.getdata())

XML = """<?xml version="1.0"?>
<file>
  <headers>{% for name in header %}{{name}}{% if name != header[-1] %},{% endif %}{% endfor%}</headers>
  <data>{% for list in data %}
    <record> 
      {% for item in list -%}
      <{{header[loop.index0].replace(" ", "_")}}>{{item}}</{{header[loop.index0].replace(" ", "_")}}>
      {%- endfor %}
    </record>{% endfor %}
  </data>
</file>"""


print Environment().from_string(XML).render(header=header, data=data)