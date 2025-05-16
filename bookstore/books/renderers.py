from rest_framework.renderers import BaseRenderer
import dicttoxml

class XMLRenderer(BaseRenderer):

    def render(self, data, accopted_media_type=None,renderer_context=None):
        if data is None:
            return '' 
        