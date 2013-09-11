#/usr/bin/python

import re
import sys

filename = sys.argv[1]
html = open(filename).read()

counters = [0,0,0]
targets  = {}

# Loop over H3, H4, H5 tags
for header in re.findall('<h[3-5].*?</h[3-5]>', html):
    id = '#' + re.findall('id="(.*?)"', header)[0]
    # <H3>
    if header[2] == '3':
        counters[0] += 1
        counters[1]  = 0
        counters[2]  = 0
        targets[id]  = "ARTICLE {0}".format(*counters)
        label = "<div class='index bold'>ARTICLE {0}</div>".format(*counters)
    # <H4>
    if header[2] == '4':
        counters[1] += 1
        counters[2]  = 0
        targets[id]  = "Section {0}.{1}".format(*counters)
        label = "<div class='index'>Section {0}.{1}</div>".format(*counters)
    # <H5>
    if header[2] == '5':
        counters[2] += 1
        targets[id]  = "Section {0}.{1}.{2}".format(*counters)
        label = "<div class='index padded'>Section {0}.{1}.{2}</div>".format(*counters)
    # Prepend the label
    html = re.sub(header, label+header, html)

# Clean up hyperlins
for anchor in re.findall('<a href=".*?">.*?</a>', html):
    href, text = re.findall('<a href="(.*?)">(.*?)</a>', anchor)[0]
    old = '<a href="{0}">{1}</a>'.format(href, text)
    new = '<a href="{0}">{1}</a>'.format(href, targets[href])
    html = re.sub(old, new, html)

# Output the modified html
with open(filename, 'w') as f_handle:
    f_handle.write(html)
