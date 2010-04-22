from jinja2 import Environment, PackageLoader
from django.http import HttpResponse

env = Environment(loader=PackageLoader("mobileviews", "templates"))

def jinja_render_to_response(template_file, context):
    """use Jinja2 to render the template"""
    template = env.get_template(template_file)
    return HttpResponse(template.render(**context))


def determine_phone_intelligence(request):
    ua = request.META["HTTP_USER_AGENT"].strip()
    if any(i in ua for i in ["dumb", "smart", "brilliant"]):
        parsed = [s.strip() for s in ua.split(";")]
        return parsed[0], parsed[1:]
    return "default", []


# decorator from django-annoying project
# http://bitbucket.org/offline/django-annoying/src/tip/annoying/decorators.py
from functools import wraps
def render_to(template=None, mimetype="text/html"):
    def renderer(function):
        @wraps(function)
        def wrapper(request, *args, **kwargs):
            output = function(request, *args, **kwargs)
            if not isinstance(output, dict):
                return output
            tmpl = output.pop('TEMPLATE', template)
            intelligence, quirks = determine_phone_intelligence(request)
            output["phone"] = {
                "intelligence": intelligence,
                "quirks": quirks,
            }
            return jinja_render_to_response("%s.%s.html" % \
                                                (tmpl, intelligence), output)
        return wrapper
    return renderer
