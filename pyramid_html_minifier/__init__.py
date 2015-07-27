from zope.interface import implementer

from pyramid.threadlocal import get_current_registry

from pyramid_chameleon.interfaces import ITemplateRenderer
from pyramid_chameleon import renderer
from pyramid_chameleon.zpt import (
    ZPTTemplateRenderer as OriginalZPTTemplateRenderer,
    )

from .util import convert_path


def renderer_factory(info):
    info.name = convert_path(info.name, info.registry.settings)
    return renderer.template_renderer_factory(info, ZPTTemplateRenderer)


@implementer(ITemplateRenderer)
class ZPTTemplateRenderer(OriginalZPTTemplateRenderer):

    def __init__(self, path, lookup, macro=None):
        registry = get_current_registry()
        settings = getattr(registry, 'settings')
        path = convert_path(path, settings)
        super(ZPTTemplateRenderer, self).__init__(path, lookup, macro)


def includeme(config):
    # add html renderer (chameleon based)
    config.add_renderer(
        name='.html',
        factory='pyramid_html_minifier.renderer_factory')
