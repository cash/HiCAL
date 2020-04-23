from config.settings.base import DOCUMENTS_URL
from config.settings.base import PARA_URL
from datetime import date
import traceback
import re
import requests

import httplib2
from lxml import etree

try:
    # For c speedups
    from simplejson import loads
except ImportError:
    from json import loads


LEAD_PARA_REGEX = re.compile(r'<p>\s*LEAD:.*?</p>')


def exec_xpath(tree, xpath):
    try:
        val = tree.xpath(xpath)[0]
        val_str = etree.tostring(val, encoding="unicode")
        return val_str
    except:
        traceback.print_exc()
        return ""


def get_date(tree, xpath):
    try:
        d = tree.xpath(xpath)[0]
        year = int(d[:4])
        month = int(d[4:6])
        day = int(d[6:8])
        d = date(year, month, day)
        return d.strftime("%A %d. %B %Y")
    except:
        traceback.print_exc()
        return "N/A"


def get_documents(doc_ids, query=None):
    """
    :param query:
    :param doc_ids: the ids of documents to return
    :return: documents content
    """
    result = []
    for doc_id in doc_ids:
        url = '{}/{}'.format(DOCUMENTS_URL, doc_id)
        content = requests.get(url).text
        title = content.split('\n\n')[0][:256]
        content = content.replace('\n', '<br />')
        if len(content) == 0:
            if len(title) == 0:
                title = '<i class="text-warning">The document title is empty</i>'
            content = '<i class="text-warning">The document content is empty</i>'
        else:
            if len(title) == 0:
                title = content[:32]

        document = {
            'doc_id': doc_id,
            'title': title,
            'content': content,
            'date': 'N/A'
        }
        result.append(document)

    return result


def get_documents_with_snippet(doc_ids, query):
    h = httplib2.Http()
    url = "{}/{}"
    doc_ids_unique = []
    doc_ids_set = set()
    for doc_id in doc_ids:
        if doc_id['doc_id'] not in doc_ids_set:
            doc_ids_set.add(doc_id['doc_id'])
            doc_ids_unique.append(doc_id)

    doc_ids = doc_ids_unique

    result = get_documents([doc['doc_id'] for doc in doc_ids], query)
    for doc_para_id, doc in zip(doc_ids, result):
        if 'para_id' not in doc_para_id:
            doc['snippet'] = u'N/A'
            continue
        try:
            para_id = doc_para_id['doc_id'] + '.' + doc_para_id['para_id']
            resp, content = h.request(url.format(PARA_URL, para_id),
                                      method="GET")
            doc['snippet'] = content.decode('utf-8')
        except:
            traceback.print_exc()
            doc['snippet'] = u'N/A'
    return result
