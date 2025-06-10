from django import template

register = template.Library()

@register.filter(name='add_attrs')
def add_attrs(field, css):
    """Agrega atributos personalizados a los campos."""
    attrs = {}
    definitions = css.split(',')
    for definition in definitions:
        key, value = definition.split('=')
        attrs[key.strip()] = value.strip()
    return field.as_widget(attrs=attrs)