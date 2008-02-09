from template import *

def test_empty_tag():
    assert unicode(tag('a')) == u'<a />'

def test_tag_with_text_content():
    assert unicode(tag('b', ['asdf'])) == u'<b>asdf</b>'

def test_tag_with_tag_content():
    assert unicode(tag('c', [tag('d')])) == u'<c><d /></c>'

def test_tag_with_more_content():
    assert unicode(tag('b', ['asdf', 'fdsa'])) == u'<b>asdffdsa</b>'

def test_empty_tag_with_attrs():
    assert unicode(tag('a', attrs={'q':'r'})) == u'<a q="r" />'

def test_tag_with_attrs_and_content():
    assert unicode(tag('a', ['asdf'], {'q':'r'})) == u'<a q="r">asdf</a>'

def test_tag_encoding():
    assert str(tag('a', [u'\u2030'])) == u'<a>\u2030</a>'.encode('utf-8')
    encoding = 'shift-jis'
    assert str(tag('a', [u'\u2030'],
        encoding=encoding)) == u'<a>\u2030</a>'.encode(encoding)

def test_tag_eq():
    assert tag('a') == tag('a')
    assert tag('a', ['b','c']) == tag('a', ['b','c'])
    assert tag('a', ['b'], {'c':'d'}) == tag('a', ['b'], {'c':'d'})
    assert tag('a', encoding='ascii') == tag('a', encoding='ascii')
    assert tag('a') != tag('b')
    assert tag('a') != tag('a', ['b'])
    assert tag('a') != tag('a', attrs={'b':'c'})
    assert tag('a') != tag('a', ['b'], {'c':'d'})
    assert tag('a', encoding='utf-8') != tag('a', encoding='ascii')

if __name__ == '__main__':
    import nose
    nose.main()
