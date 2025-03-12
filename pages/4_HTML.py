import streamlit as st
import streamlit.components.v1 as components
from jinja2 import Template

def main():
    # Your dynamic data
    with st.echo(code_location="below"):
        st.markdown("## Reading an HTML File\nThe source file is stored in `streamlit/lec17/data/template.html`")

        app_title = "Using HTML in Streamlit"
        items = ["Item 1", "Item 2", "Item 3"]

        # Load the Jinja2 template
        with open("./lec17/data/template.html", "r") as template_file:
            template_content = template_file.read()
            jinja_template = Template(template_content)

        # Render the template with dynamic data
        rendered_html = jinja_template.render(title=app_title, items=items)

        # Display the HTML in Streamlit app
        components.html(rendered_html, height=200, scrolling=True)

if __name__ == '__main__':
    main()

st.divider()

"""## HTML Source Code
Located at `streamlit/lec17/data/template.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body style="background-color:powderblue;">
    <div>
        <h1>{{ title }}</h1>
        <p>This is a simple Streamlit app with a Jinja2 template.</p>
        <ul>
            {% for item in items %}
                <li>{{ item }}</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
```
"""