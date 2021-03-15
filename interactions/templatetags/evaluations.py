from django import template


register = template.Library()


@register.inclusion_tag('interactions/evaluation_star.html')
def evaluation_star(value):
    """Tag for displaying the rating in the form of stars.

    Args:
        value (int): Evaluation.

    Returns:
        dict: The return value as a dict for use in the template.
    """
    return {'value': value}
