#!/usr/bin/env python
"""
Generate 'works' and 'timeline' from files in content/works
"""


from collections import defaultdict
import datetime
import os

TIMELINE_TOP = """Title: Timeline
Date: %s
Authors: 3
"""

WRITINGS_TOP = """Title: Writings
Date: %s
Authors: 2
"""
TIMELINE_PAGE='content/pages/timeline.md'
TIMELINE_INDEX_SHTML='content/pages/timeline_index.shtml'
WRITINGS_PAGE='content/pages/writings.md'
WRITINGS_INDEX_SHTML='content/pages/writings_index.shtml'

def rec_dd():
    return defaultdict(rec_dd)

def get_filepaths(directory):
    """
    This function will generate the file names in a directory
    tree by walking the tree either top-down or bottom-up. For each
    directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

def get_header(name, filelines):
    try:
        thing = [i for i in filelines if i.find(name) == 0]
        thing = thing[0].split(":")[1].strip()
    except:
        print("Failed to get_header %s" % name)
        raise
    assert len(thing), "Could not find %s in %r" % (name, filelines)
    return thing

def load_data():
    works_cats = rec_dd()
    path = 'content/works'
    files = [f for f in get_filepaths(path) if f.endswith('.md')]
    years = rec_dd()
    TITLE = 'Title:'
    PUBDATE = 'PubDate:'
    SLUG = 'Slug:'
    for f in files:
        try:
            lines = open(f, 'r').readlines(1024)
            pubdate = get_header(PUBDATE, lines)
            title = get_header(TITLE, lines)
            slug = get_header(SLUG, lines)
            y, m, _ = pubdate.split('-')
            months = years[y]
            titles = months[m]
            title_info = titles[title]
            title_info['date'] = pubdate
            title_info['summary'] = ''
            title_info['title'] = title
            title_info['slug'] = slug
            title_info['href'] = '/%s.html' % slug
            # parse slug
            cats = slug.split('/')[:-1]
            assert len(cats), "%s: slug must contain category: %s, %s" % (f, slug, len(cats))
            sub = works_cats[cats[0]]
            for cat in cats[1:]:
                sub = sub[cat]
            title_info = sub[title]
            title_info['date'] = pubdate
            title_info['title'] = title
            title_info['summary'] = ''
            title_info['slug'] = slug
            title_info['href'] = '/%s.html' % slug
        except:
            print("Failed to process file: %s" % f)
    return works_cats, years

def gen_timeline(years):
    timeline = open(TIMELINE_PAGE, 'w')
    timeline_index = open(TIMELINE_INDEX_SHTML, 'w')
    timeline.write(TIMELINE_TOP % datetime.datetime.now())
    timeline.write('<!--#include virtual="/pages/timeline_index.shtml" -->')
    timeline_index.write('<p>')
    for y in sorted(years.keys()):
        timeline_index.write('<a href="/pages/timeline.html#%s">%s</a> ' % (y, y))
    timeline_index.write('</p>')

    timeline.write('<div class="timeline"><hr style="margin-top: 50px; margin-bottom: 30px"/>')
    for y in sorted(years.keys()):
        timeline.write('<span id="%s"></span><br/><br/>' % (y))
        timeline.write('<h2>%s</h2><ul>' % (y))
        months = years[y]
        for m in sorted(months.keys()):
            titles = months[m]
            for t in sorted(titles.keys()):
                info = titles[t]
                timeline.write('<li><a href="%s">%s<span class="date">[%s]</span></a></li>' % (info['href'], t, info['date']))
        timeline.write('</ul>')
    timeline.write('</div>')

def get_display_title(l):
    if l == "recently-discovered":
        return "Recently attributed"
    if l == 'questionable-authorship':
        return "Works removed from the Paine cannon"
    return ' '.join(l.split('-')).title()

def get_work_order(work):
    work_order = {'major-works': 1,
                  'essays': 2,
                  'letters' : 3,
                  'questionable-authorship': 4,
                  'recently-discovered': 5}
    if work not in work_order:
        raise Exception("Unkown work type: %s" % work)
    return work_order[work]

def output_works(writings, works):
    writings.write('<ul>')
    for work in sorted(works.keys()):
        more_works = works[work]
        disp = get_display_title(work)
        if 'href' in more_works:
            disp = '<a href="%s">%s</a>' % (more_works['href'], more_works['title'])
            writings.write('<li>%s' % (disp))
        else:
            writings.write('<li>%s' % (get_display_title(work)))
            output_works(writings, more_works)
        writings.write('</li>')
    writings.write('</ul>')

def gen_works(works_cats):
    writings = open(WRITINGS_PAGE, 'w')
    writings_index = open(WRITINGS_INDEX_SHTML, 'w')
    writings_index.write('<p>')
    writings.write(WRITINGS_TOP % datetime.datetime.now())
    writings.write('<!--#include virtual="/pages/writings_index.shtml" -->')
    for cat in sorted(works_cats.keys(), key=get_work_order):
        display_cat = get_display_title(cat)
        writings_index.write('<a href="/pages/writings.html#%s">%s</a><br/>' % (cat, display_cat))
    writings_index.write('</p>')
    writings.write('<div><hr style="margin-top: 50px; margin-bottom: 30px"/><ul>')
    for cat in sorted(works_cats.keys(), key=get_work_order):
        works = works_cats[cat]
        display_cat = get_display_title(cat)
        writings.write('<span id="%s"><span><br/><br/>' % (cat))
        writings.write('<li><h3>%s<h3>' % (display_cat))
        output_works(writings, works)
        writings.write('</li>')
    writings.write('</ul></div>')


