from stemp import *

def test_empty_tag():
    assert unicode(p) == u'<p />'

def test_tag_with_text_content():
    assert unicode(p['asdf']) == u'<p>asdf</p>'

def test_tag_with_tag_content():
    assert unicode(p[h1]) == u'<p><h1 /></p>'

def test_tag_with_more_content():
    assert unicode(p['asdf', 'fdsa']) == u'<p>asdffdsa</p>'

def test_empty_tag_with_attrs():
    assert unicode(p(q='r')) == u'<p q="r" />'

def test_tag_with_attrs_and_content():
    assert unicode(p(q='r')['asdf']) == u'<p q="r">asdf</p>'

#def test_tag_encoding():
#    assert str(tag('a', [u'\u2030'])) == u'<a>\u2030</a>'.encode('utf-8')
#    encoding = 'shift-jis'
#    assert str(tag('a', [u'\u2030'],
#        encoding=encoding)) == u'<a>\u2030</a>'.encode(encoding)

#def test_tag_eq():
#    assert tag('a') == tag('a')
#    assert tag('a', ['b','c']) == tag('a', ['b','c'])
#    assert tag('a', ['b'], {'c':'d'}) == tag('a', ['b'], {'c':'d'})
#    #assert tag('a', encoding='ascii') == tag('a', encoding='ascii')
#    assert tag('a') != tag('b')
#    assert tag('a') != tag('a', ['b'])
#    assert tag('a') != tag('a', attrs={'b':'c'})
#    assert tag('a') != tag('a', ['b'], {'c':'d'})
#    #assert tag('a', encoding='utf-8') != tag('a', encoding='ascii')

if __name__ == '__main__':
    import nose
    nose.main()
