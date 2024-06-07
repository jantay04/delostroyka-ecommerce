# api/schema.py
from drf_spectacular.openapi import AutoSchema


class CustomAutoSchema(AutoSchema):
    def get_tags(self, request=None):
        # Derive tags from the view's module name
        app_name = self.view.__module__.split('.')[0]
        return [app_name] if app_name else super().get_tags(request)
