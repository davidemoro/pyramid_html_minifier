from .config import DEFAULT_PLACEHOLDER


def convert_path(path, settings):
    """ Convert a path with {0} to app or dist
        depending on settings
    """
    if '{0}' in path:
        placeholder = DEFAULT_PLACEHOLDER
        if settings:
            placeholder = settings.get(
                'pyramid_html_minifier.placeholder',
                DEFAULT_PLACEHOLDER
                )
        path = path.format(placeholder)
    return path
