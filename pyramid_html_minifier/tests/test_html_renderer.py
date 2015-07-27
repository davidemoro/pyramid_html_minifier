import sys


class BaseRenderer:

    def _getTemplatePath(self, name):
        import os
        here = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(here, 'fixtures', name)

    def _getTargetClass(self):
        from pyramid_html_minifier import ZPTTemplateRenderer
        return ZPTTemplateRenderer

    def _makeOne(self, *arg, **kw):
        klass = self._getTargetClass()
        return klass(*arg, **kw)

    def _callFUT(self, info):
        from pyramid_html_minifier import renderer_factory
        return renderer_factory(info)


class TestIncludeme:

    def test_includeme(self):
        from pyramid import testing
        with testing.testConfig() as config:
            config.include('pyramid_html_minifier')


class TestHtmlRenderer(BaseRenderer):

    def test_it(self):
        # this test is way too functional
        from pyramid_html_minifier import ZPTTemplateRenderer
        info = DummyInfo()
        result = self._callFUT(info)
        assert result.__class__ == ZPTTemplateRenderer

    def test_instance_implements_ITemplateRenderer(self):
        from zope.interface.verify import verifyObject
        from pyramid_chameleon.interfaces import ITemplateRenderer
        path = self._getTemplatePath('minimal.pt')
        lookup = DummyLookup()
        verifyObject(ITemplateRenderer, self._makeOne(path, lookup))

    def test_class_implements_ITemplateRenderer(self):
        from zope.interface.verify import verifyClass
        from pyramid_chameleon.interfaces import ITemplateRenderer
        verifyClass(ITemplateRenderer, self._getTargetClass())

    def test_call(self):
        minimal = self._getTemplatePath('minimal.html')
        lookup = DummyLookup()
        instance = self._makeOne(minimal, lookup)
        result = instance({}, {})
        from pyramid.compat import text_type
        assert isinstance(result, text_type)
        assert result.rstrip('\n') == '<div xmlns="http://www.w3.org/1999/xhtml">\n</div>'

    def test_macro_supplied(self):
        minimal = self._getTemplatePath('withmacro.html')
        lookup = DummyLookup()
        instance = self._makeOne(minimal, lookup, macro='foo')
        result = instance.implementation()()
        assert result == '\n  Hello!\n'

    def test_macro_notsupplied(self):
        minimal = self._getTemplatePath('withmacro.html')
        lookup = DummyLookup()
        instance = self._makeOne(minimal, lookup)
        result = instance.implementation()()
        assert result == '<html>\nOutside macro\n\n  Hello!\n\n</html>\n\n'

    def test_macro_template_reload(self):
        minimal = self._getTemplatePath('withmacro.html')
        lookup = DummyLookup()
        instance = self._makeOne(minimal, lookup, macro='foo')
        result = instance.implementation()()
        assert result == '\n  Hello!\n'
        instance.template.cook(
            '<html>\nOutside macro\n\n  Hello!\n\n</html>\n\n'
            )
        result = instance.implementation()()
        assert result == '\n  Hello!\n'


class TestHtmlAppDistRenderer(BaseRenderer):

    def _getTemplatePath(self, name):
        import os
        here = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(here, 'fixtures', '{0}', name)

    def _makeOneDist(self, *arg, **kw):
        import mock
        with mock.patch('pyramid_html_minifier.get_current_registry') as get_current_registry:
            get_current_registry.return_value = mock.Mock(
                settings={'pyramid_html_minifier.placeholder': 'mydist'}
                )
            klass = self._getTargetClass()
            return klass(*arg, **kw)

    def test_macro_supplied_default(self):
        minimal = self._getTemplatePath('withmacro.html')
        lookup = DummyLookup()
        instance = self._makeOne(minimal, lookup, macro='foo')
        implementation = instance.implementation()
        result = implementation()
        assert result == '\n  Hello!\n'

    def test_macro_supplied_dist(self):
        minimal = self._getTemplatePath('withmacro.html')
        lookup = DummyLookup()
        instance = self._makeOneDist(minimal, lookup, macro='foo')
        implementation = instance.implementation()
        result = implementation()
        assert result == 'Hello!'


class DummyLookup(object):
    auto_reload = True
    debug = True

    def translate(self, msg):
        pass


class DummyRegistry(object):
    def queryUtility(self, iface, name):
        self.queried = iface, name
        return None

    def registerUtility(self, impl, iface, name):
        self.registered = impl, iface, name


class DummyInfo(object):
    def __init__(self):
        self.registry = DummyRegistry()
        self.registry.settings = {}
        self.type = '.html'
        self.name = 'fixtures/minimal.html'
        self.package = sys.modules[__name__]
        self.settings = {}
