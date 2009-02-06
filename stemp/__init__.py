from itertools import imap


def _collapse(it):
    if isinstance(it, basestring):
        yield it
    else:
        try:
            for it2 in imap(_collapse, it):
                for el in it2:
                    yield el
        except TypeError:
            yield it


class _striter(object):
    def __init__(self, it):
        self.it = it
    
    def next(self):
        return self.it.next()
    
    def __iter__(self):
        return self.it
    
    def __unicode__(self):
        return u''.join(imap(unicode, self.it))
    
    def __str__(self):
        return ''.join(imap(str, self.it))


__all__ = ['htmldoc']


class htmldoc(object):
    def __init__(self, doctype, html, encoding='utf-8'):
        self.doctype = doctype
        self.html = html
        self.encoding = encoding
    
    def __iter__(self):
        yield u'<!DOCTYPE ' + u' '.join(imap(unicode, self.doctype)) + u'>'
        for part in self.html:
            yield part
    
    def __unicode__(self):
        return u''.join(self)
    
    def __str__(self):
        return unicode(self).encode(self.encoding)


class htmltag(object):
    name = u''
    
    def __init__(self, attrs=None):
        self.attrs = {} if attrs is None else attrs
    
    def _open(self, empty=False):
        yield u'<'
        yield self.name
        for x in self.attrs.iteritems():
            yield u' %s="%s"' % x
        if empty:
            yield u' />'
        else:
            yield u'>'
    
    def render(self, children=()):
        yield u''.join(self._open(not children))
        if children:
            for part in _collapse(children):
                yield unicode(part)
            yield u'</' + self.name + '>'
    
    @classmethod
    def __call__(cls, **kw):
        return cls(dict((k.rstrip('_'), v) for k, v in kw.iteritems()))
    
    def __unicode__(self):
        return u''.join(self)
    
    def __getitem__(self, children):
        if isinstance(children, basestring):
            children = ((unicode(children),),)
        return _striter(self.render(children))
    
    def __iter__(self):
        return self.render()


def _mktag(name_):
    class a(htmltag):
        name = name_.rstrip('_')
    a.__name__ = a.name
    return name_, a()


tags = ('html head title body link script span form input_ textarea '
        'h1 h2 h3 h4 h5 h6 p a ul ol li img div br label'.split())
locals().update(dict(imap(_mktag, tags)))
__all__.extend(tags)


if __name__ == '__main__':
    print ''.join(htmldoc(('html', 'PUBLIC', '"-//W3C//DTD HTML 4.01//EN"',
                           '"http://www.w3.org/TR/html4/strict.dtd"'),
        html[
            head[
                title['the title!'],
                link(href='/styles.css', rel='stylesheet'),
                link(href='/main.css', rel='stylesheet')
            ],
            body(class_='the_class')[1]
        ]
    ))
