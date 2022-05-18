import panflute
import sys

headers = []


def levelHeader(elem, doc):
    if isinstance(elem, panflute.Header):
        if elem.level > 2:
            result = panflute.Header(panflute.Str(panflute.stringify(elem).upper()), level=elem.level)
            return result


def headerIsExisting(elem, doc):
    if isinstance(elem, panflute.Header):
        text = panflute.stringify(elem)
        if text in headers:
            sys.stderr.write("Warning: Header `" + text + "` already exists in document\n")
        else:
            headers.append(text)


def boldType(doc):
    doc.replace_keyword('BOLD', panflute.Strong(panflute.Str('BOLD')))


if __name__ == '__main__':
    panflute.run_filters([headerIsExisting, levelHeader], prepare=boldType)
