from denver.mobileviews.decorators import render_to

@render_to("template")
def mobile_view(request):
    return {
        "foo": "bar"
    }

