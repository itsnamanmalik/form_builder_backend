from rest_framework.renderers import JSONRenderer
import json
from rest_framework.compat import INDENT_SEPARATORS, LONG_SEPARATORS, SHORT_SEPARATORS
from utils.common_methods import is_success_status_code


class CustomJsonRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        renderer_context = renderer_context or {}
        indent = self.get_indent(accepted_media_type, renderer_context)
        if indent is None:
            separators = SHORT_SEPARATORS if self.compact else LONG_SEPARATORS
        else:
            separators = INDENT_SEPARATORS
        response = renderer_context["response"]

        if is_success_status_code(response.status_code):
            try:
                message = renderer_context["view"].success_message
            except:
                message = "OK"
        else:
            try:
                message = renderer_context["view"].error_message
            except:
                message = "Some error occured!"
        if data is not None:
            my_response = {
                "status": is_success_status_code(response.status_code),
                "message": message,
                "data": data,
            }
        else:
            my_response = {
                "status": is_success_status_code(response.status_code),
                "message": message,
            }

        ret = json.dumps(
            my_response,
            cls=self.encoder_class,
            indent=indent,
            ensure_ascii=self.ensure_ascii,
            allow_nan=not self.strict,
            separators=separators,
        )

        # We always fully escape \u2028 and \u2029 to ensure we output JSON
        # that is a strict javascript subset.
        # See: https://gist.github.com/damncabbage/623b879af56f850a6ddc
        ret = ret.replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
        return ret.encode()
