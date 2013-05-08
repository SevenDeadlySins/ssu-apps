#######################################
# Automatic pagination                #
#######################################

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.tag()
def paginate(parser, token):
    """
Creates a pretty and functional pagination bar.

Syntax::
{% paginate <current_page> <num_pages> [<append_url>] %}

The current page and total number of pages are required. The append_url
option is used if the pagination needs to redirect to another URL before
generating the page.
"""
    bits = token.split_contents()[1:]

    # Only accepts either 2 or 3 arguments.
    if len(bits) < 2:
        raise template.TemplateSyntaxError("%r tag requires at least two arguments" % token.contents.split()[0])
    elif len(bits) > 3:
        raise template.TemplateSyntaxError("%r tag received too many arguments" % token.contents.split()[0])
    return PaginateNode([parser.compile_filter(bit) for bit in bits])


class PaginateNode(template.Node):
    def __init__(self, vars):
        self.vars = vars

    def render(self, context):
        current_page = self.vars[0].resolve(context)
        num_pages = self.vars[1].resolve(context)
        # Third option may not be present, use empty string in that case
        try:
            append_link = self.vars[2].resolve(context)
        except IndexError:
            append_link = ''
        url = context['request'].path + append_link
        querydict = context['request'].GET.copy()
        html = "<div class='pagination pagination-centered'>"
        html += "<ul>"

        if current_page == 1:
            # No previous page for 1.
            html += '<li class="disabled"><span>Prev</span></li>'
        else:
            # Anything else, activate Prev button.
            querydict['page'] = current_page - 1
            html += '<li><a href="%s?%s">Prev</a></li>' % (url, querydict.urlencode(safe=':'))

        if num_pages < 9:
            # If there's less than 9 pages, just display them all.
            for page in range(1, num_pages + 1):
                querydict['page'] = page
                html += '<li%s><a href="%s?%s">%s</a></li>' % ((' class="active"' if page == current_page else ''), url, querydict.urlencode(safe=':'), str(page))
        else:
            # Display the first 3 pages.
            for page in range(1, 4):
                querydict['page'] = page
                html += '<li%s><a href="%s?%s">%s</a></li>' % ((' class="active"' if page == current_page else ''), url, querydict.urlencode(safe=':'), str(page))

            if current_page > 4:
                # There must be some pages between the current page and the first 3.
                html += '<li><span>...</span></li>'

            if current_page in range(4, num_pages - 2):
                # Show the current page in the middle.
                querydict['page'] = current_page
                html += '<li class="active"><a href="%s?%s">%s</a></li>' % (url, querydict.urlencode(safe=':'), str(current_page))

            if current_page < num_pages - 3:
                # There must be some pages between the current page and the last 3.
                html += '<li><span>...</span></li>'

            # Display the last 3 pages.
            for page in range(num_pages - 2, num_pages + 1):
                querydict['page'] = page
                html += '<li%s><a href="%s?%s">%s</a></li>' % ((' class="active"' if page == current_page else ''), url, querydict.urlencode(safe=':'), str(page))

        if current_page == num_pages:
            # We must be on the last page, no next page.
            html += '<li class="disabled"><span>Next</span></li>'
        else:
            # Not on the last page, activate the Next link.
            querydict['page'] = current_page + 1
            html += '<li><a href="%s?%s">Next</a></li>' % (url, querydict.urlencode(safe=':'))

        html += "</ul>"
        html += "</div><!-- pagination -->"
        return mark_safe(html)