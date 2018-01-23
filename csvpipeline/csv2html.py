from jinja2 import Environment
import mycsv

header, data = mycsv.readcsv(mycsv.getdata())

HTML = """<html>
<body>
<table>
<tr>{% for item in header %}<th>{{item}}</th>{% endfor %}</tr>{% for list in data %}
<tr>{% for item in list %}<td>{{item}}</td>{% endfor %}</tr>{% endfor %}
</table>
</body>
</html>"""


print Environment().from_string(HTML).render(header=header, data=data)