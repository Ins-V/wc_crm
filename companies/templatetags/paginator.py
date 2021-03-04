from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def page_replace(context, value):
    """Replaces or adds the page number to form the pagination url.

    Example:
        if you're on the page ``/company/list/?sorted=created&page=5``,
        then
            <a href="/company/list/?{% page_replace 3 %}">Page 3</a>

        would expand to
            <a href="/company/list/?sorted=created&page=3">Page 3</a>
    """
    query = context['request'].GET.copy()
    query['page'] = value
    return query.urlencode()


@register.inclusion_tag('companies/pagination.html', takes_context=True)
def pagination(context):
    """Includes a pagination template."""
    return context
