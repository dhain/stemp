from itertools import imap

class doc(object):
    def __init__(self, parts=[], encoding='utf-8'):
        self.parts = parts
        self.encoding = encoding
    
    def __eq__(self, other):
        return (self.parts == other.parts
            and self.encoding == other.encoding)
    
    def __str__(self):
        return unicode(self).encode(self.encoding)
    
    def __unicode__(self):
        return u''.join(imap(unicode, self.parts))

class tag(object):
    def __init__(self, name, content=None, attrs=None):
        self.name = name
        self.attrs = {} if attrs is None else attrs
        self.content = [] if content is None else content
    
    def __unicode__(self):
        return u''.join(self._parts())
    
    def __eq__(self, other):
        return (self.name == other.name
            and self.attrs == other.attrs
            and self.content == other.content)
    
    def _parts(self):
        yield u'<'
        yield self.name
        for x in self.attrs.iteritems():
            yield u' %s="%s"' % x
        if self.content:
            yield u'>'
            for x in self.content:
                yield unicode(x)
            yield u'</'
            yield self.name
            yield u'>'
        else:
            yield u' />'

class doctype(tag):
    def __init__(self, *args):
        self.args = args
    
    def __eq__(self, other):
        return (self.args == other.args)
    
    def _parts(self):
        yield u'<!DOCTYPE'
        for a in self.args:
            yield u' '
            yield unicode(a)
        yield u'>'

def html(title, head=[], body=[], doctype=None):
    d = []
    if doctype:
        d.append(doctype)
    h = tag('head', [
        tag('title', [title])])
    h.content.extend(head)
    d.append(tag('html', [h, tag('body', body)]))
    return doc(d)

if __name__ == '__main__':
    print html('Test document',
        [tag('link', attrs={'rel':'stylesheet', 'href':'style.css'})],
        ['This is some body stuff.'])
