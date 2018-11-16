"""
CSS Helper extension for Python-Markdown
=========================================

Markdown extension that allows applying a custom span to match
certain keywords.

@abstract -- applies abstract class
@const -- applies const class
@static -- applies static class
@extends -- applies extends class
@d.keyword -- applies the "declaration" class to "keyword"
@p.keyword -- applies the "parameter" class to "keyword"

"""

import markdown
from markdown import Extension
from markdown.preprocessors import Preprocessor
from markdown.inlinepatterns import Pattern

CUSTOM_CLS_RE = r'@(?P<type>(?:abstract|const|static|extends|d\.|p\.))(?P<text>\w*)'


class CssHelperExtension(Extension):
    """ Extension class for markdown """

    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns["csshelper"] = CssHelperPattern(CUSTOM_CLS_RE, md)


class CssHelperPattern(Pattern):

    def handleMatch(self, matched):

        cls = matched.group("type")
        text = matched.group("text")

        if cls == "p.":
            cls = "parameter"
        elif cls == "d.":
            cls = "declaration"
        else:
            text = cls

        elem = markdown.util.etree.Element("span")
        elem.set("class", cls)
        elem.text = markdown.util.AtomicString(text)
        return elem


def makeExtension(*args, **kwargs):
    return CssHelperExtension(*args, **kwargs)
