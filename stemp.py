from itertools import imap

__all__ = ['htmldoc']

def htmldoc(doctype, html, encoding='utf-8'):
    return ''.join(('<!DOCTYPE ',' '.join(imap(str, doctype)),'>',
        unicode(html).encode(encoding)))

class htmltag(object):
    name = u''
    attrs = {}
    
    def _parts(self, args):
        yield u'<'
        yield self.name
        for x in self.attrs.iteritems():
            yield u' %s="%s"' % x
        if args:
            yield u'>'
            for a in args:
                yield a
            yield u'</'
            yield self.name
            yield u'>'
        else:
            yield u' />'
    
    def _render(self, args=()):
        return u''.join(self._parts(args))
    
    @classmethod
    def __call__(cls, **kw):
        i = cls()
        i.attrs = dict((k.rstrip('_'), v) for k, v in kw.iteritems())
        return i
    
    def __unicode__(self):
        return self._render()
    
    def __getitem__(self, args):
        if isinstance(args, basestring):
            a = (unicode(args),)
        else:
            try:
                a = imap(unicode, args)
            except TypeError:
                a = (unicode(args),)
        return self._render(a)

def _mktag(name_):
    class a(htmltag):
        name = name_
    a.__name__ = name_
    return name_, a()

tags = ('html','head','title','body','link','script','h1','p')
locals().update(dict(imap(_mktag, tags)))
__all__.extend(tags)

if __name__ == '__main__':
    print html[
        head[
            title['the title!'],
            link(href='/styles.css', rel='stylesheet')
        ],
        body(class_='the_class')[1]
    ]
