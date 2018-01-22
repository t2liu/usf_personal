import jinja2 as j
import mycsv

header, data = mycsv.readcsv(mycsv.getdata())

t = """<html>
<body>
<table>
<tr>{% for h in headers %}<th>{{h}}</th>{% endfor %}</tr>{% for line in data %}
<tr>{% for l in line %}<td>{{l}}</td>{% endfor %}</tr>{% endfor %}
</table>
</body>
</html>"""

def print_html_doc():
    print j.Environment().from_string(t).render(headers=header, data=data)

if __name__ == '__main__':
    print_html_doc()