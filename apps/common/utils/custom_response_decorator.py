from rest_framework.views import APIView

def custom_response(view):
    assert issubclass(
        view, APIView
    ), f"class {view.__name__} must be subclass of APIView"

    def inner(self, request, *args, **kwargs):
        response = super(view, self).dispatch(request, *args, **kwargs)

        is_success = 200 <= response.status_code < 300

        if (
            not is_success
            and isinstance(response.data, dict)
            and "errors" in response.data
        ):
            response.data = {
                "success": False,
                "errors": response.data["errors"],
            }
            response._is_rendered = False
            return response

        formatted_response = {"success": is_success}

        if is_success:
            formatted_response["data"] = response.data
        else:
            formatted_response["errors"] = []

            if isinstance(response.data, dict):
                for field, messages in response.data.items():
                    if not isinstance(messages, list):
                        messages = [messages]
                    for msg in messages:
                        formatted_response["errors"].append(
                            {"field": field, "message": str(msg)}
                        )
            else:
                formatted_response["errors"].append(
                    {"field": None, "message": str(response.data)}
                )

        response.data = formatted_response
        response._is_rendered = False
        return response

    view.dispatch = inner
    return view
