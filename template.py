class tag(object):
    def __init__(self, name, content=None, attrs=None, encoding='utf-8'):
        self.name = name
        self.attrs = {} if attrs is None else attrs
        self.content = [] if content is None else content
        self.encoding = encoding
    
    def __eq__(self, other):
        return (self.name == other.name
            and self.attrs == other.attrs
            and self.content == other.content
            and self.encoding == other.encoding)
    
    def __str__(self):
        return unicode(self).encode(self.encoding)
    
    def __unicode__(self):
        parts = [u'<', self.name]
        if self.attrs:
            parts.append(u' ')
            parts.append(u' '.join(u'%s="%s"' % x
                for x in self.attrs.iteritems()))
        if self.content:
            parts.append(u'>')
            parts.extend(unicode(x) for x in self.content)
            parts.append(u'</')
            parts.append(self.name)
            parts.append(u'>')
        else:
            parts.append(u' />')
        return u''.join(parts)

def html(title, head=[], body=[]):
    h = tag('head', [
        tag('title', [title])])
    h.content.extend(head)
    return tag('html', [h,
        tag('body', body)])

if __name__ == '__main__':
    print html('Test document',
        [tag('link', attrs={'rel':'stylesheet', 'href':'style.css'})],
        ['This is some body stuff.'])
