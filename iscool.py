# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

pages_folder = 'pages/'
post_viewstate = '/wEPDwUIMjU3MTQzOTcPZBYGZg8WAh4EVGV4dAU+PCFET0NUWVBFIEhUTUwgUFVCTElDICItLy9XM0MvL0RURCBIVE1MIDQuMCBU \
                  cmFuc2l0aW9uYWwvL0VOIj5kAgEPZBYMAgEPFgIeB1Zpc2libGVoZAICDxYCHgdjb250ZW50BSLXk9eUINep15zXmdeYINeX15gi \
                  16Ig16jXl9eV15HXldeqZAIDDxYCHwIFIteT15Qg16nXnNeZ15gg15fXmCLXoiDXqNeX15XXkdeV16pkAgQPFgIfAgUg15vXnCDX \
                  lNeW15vXldeZ15XXqiDXqdee15XXqNeV16pkAgUPFgQfAmQfAWhkAgYPFgIfAgUi15PXlCDXqdec15nXmCDXl9eYIteiINeo15fX \
                  ldeR15XXqmQCAg9kFgJmD2QWAgIED2QWAmYPZBYGAgIPZBYCZg8PFgYeCENzc0NsYXNzBQtza2luY29sdHJvbB4EXyFTQgICHwFo \
                  ZGQCAw9kFgJmDw8WBh8DBQtza2luY29sdHJvbB8ABRfXm9eg15nXodeUINec157Xoteo15vXqh8EAgJkZAIKD2QWAgICD2QWCAIB \
                  Dw8WAh8BaGRkAgMPDxYCHwFoZGQCBQ9kFgICAg8WAh8BaGQCBw9kFgICAQ9kFgICAQ9kFggCBg9kFgJmD2QWDAICDxYCHgVjbGFz \
                  cwUKSGVhZGVyQ2VsbGQCBA8WAh8FBQpIZWFkZXJDZWxsZAIGDxYCHwUFCkhlYWRlckNlbGxkAggPFgIfBQUKSGVhZGVyQ2VsbGQC \
                  Cg8WAh8FBQpIZWFkZXJDZWxsZAIMDxYCHwUFEEhlYWRlckNlbGxCdXR0b25kAgcPEGQQFQAVABQrAwBkZAIMD2QWAmYPZBYeZg9k \
                  FgICAQ8QZBAVHgvXmSAxINee15HXqATXmSAyBNeZIDME15kgNATXmSA1BNeZIDYE15kgNwTXmSA4BNeZIDkJ15kgMTAgYXNkDdeZ \
                  15AgMSDXnteR16gG15nXkCAyBteZ15AgMwbXmdeQIDQG15nXkCA1BteZ15AgNgbXmdeQIDcG15nXkCA4BteZ15AgOQfXmdeQIDEw \
                  C9eZ15AgMTEgYXNkDdeZ15EgMSDXnteR16gG15nXkSAyBteZ15EgMwbXmdeRIDQG15nXkSA1BteZ15EgNgbXmdeRIDcG15nXkSA4 \
                  BteZ15EgORUeATMBNQE2ATcBOAE5AjEwAjExAjQwAjQ5AjEzAjE0AjE1AjE2AjE3AjE4AjE5AjIwAjQ0AjQ4AjQ2AjIyAjIzAjI0 \
                  AjI1AjI2AjI3AjI4AjI5AjQxFCsDHmdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZxYBAhhkAgIPFgQfBQUKSGVhZGVyQ2Vs \
                  bB8BaGQCAw8WAh8BaGQCBA8WAh8FBQpIZWFkZXJDZWxsZAIGDxYCHwUFCkhlYWRlckNlbGxkAggPFgIfBQUKSGVhZGVyQ2VsbGQC \
                  Cg8WAh8FBQpIZWFkZXJDZWxsZAIMDxYEHwUFCkhlYWRlckNlbGwfAWhkAg0PFgIfAWhkAg4PFgIfBQUKSGVhZGVyQ2VsbGQCEA8W \
                  BB8FBQpIZWFkZXJDZWxsHwFoZAIRDxYCHwFoZAISDxYEHwUFCkhlYWRlckNlbGwfAWhkAhMPFgIfAWhkAhQPFgIfBQUQSGVhZGVy \
                  Q2VsbEJ1dHRvbmQCDw8PFgIfAAU7157XoteV15PXm9efINecOiAwMi4xMi4yMDE5LCDXqdei15Q6IDA2OjQ5LCDXnteh15o6IEEz \
                  MTEzOTZkZGQrAF1uagsNnzUhswtfflythWXMAw=='
classes = dict()


def getsoup(classnum=0):  # !!! DONT USE UNLESS LOCAL FILES ARE MISSING (use opensoup() instead) !!!
    r = requests.post('http://deshalit.iscool.co.il/default.aspx',
                      data={'__EVENTTARGET': 'dnn$ctr11396$TimeTableView$btnChangesTable',
                            '__VIEWSTATE': post_viewstate,
                            'dnn$ctr11396$TimeTableView$ClassesList': str(classnum)})
    return BeautifulSoup(r.text, 'html.parser')


def opensoup(classnum, folder=pages_folder):
    if not (folder.endswith('/') or folder.endswith('\\')):
        folder += '/'
    with open(folder + str(classnum) + '.html') as f:
        return BeautifulSoup(f.read())


def update_pages(folder=pages_folder):
    if not (folder.endswith('/') or folder.endswith('\\')):
        folder += '/'
    _classes = classes
    if not _classes:
        _classes = extract_classes(getsoup())
    for classnum in _classes.keys():
        with open(folder + str(classnum) + '.html', 'x') as f:
            f.write(getsoup(classnum).prettify())


def extract_classes(soup):
    select = soup.find('select', id='dnn_ctr11396_TimeTableView_ClassesList')
    return {option['value']: option.text for option in select.findChildren('option')}


def extract(soup):
    table = soup.find('div', id='dnn_ctr11396_TimeTableView_PlaceHolder').find('table')
    rows = table.findChildren('tr', recursive=False)
    return [[col.findAll('div', {'class': 'TTLesson'}) for col in row.findChildren('td', recursive=False)[1:]]
            for row in rows[1:]]


def find(data, teacher):
    """:returns: [('hour', 'info')]"""
    result = []
    for rownum, row in enumerate(data):
        for colnum, col in enumerate(row):
            if teacher in str(col):
                result.append((rownum, col))
    return result


classes = extract_classes(getsoup())
update_pages()
