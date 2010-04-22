DENVER
======

Experimenting with somewhat intelligent Django views & templates based on the user's user agent string (for now).

* returns a context variable dictionary from views
* decorator chooses best template
* jinja2 allows for more complex logic in the templates for specific mobile rendering

Example:
--------

    from denver.mobileviews.decorators import render_to
    
    @render_to("template")
    def mobile_view(request):
        return {
            "foo": "bar"
        }
    

The `render_to` is adapted from `django-annnoying` to render jinja2 templates
and to pick a template on some predetermined values. It's sloppy but you get the idea.
