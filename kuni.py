import os
import subprocess
import re
from chope import *
from chope.css import *

f = open("read2.txt", "r")
output_ = f.read()
# print(repr(output_))
# print(output_)


# rows = output_.split('Running')
# print(rows.__len__())

# for row in rows:
#     row = 'Running' + row
#     print(row)


rows = output_.split('Running')
content = []
for row in rows:
    # adding back the 'Running' after remove it on split()
    row = row.replace(' ', 'Running ', 1)
    # print(row)

    # separate the verdict and the '[test description]'from the test name header
    testName = row.split('Pass')[0].split('Failed')[0].split('[')[0]
    verdict = 'PASS' if 'Pass' in row else 'FAILED'

    if 'Flow File' in row:
        content += [div(class_='flow-test')[
                div(class_='test-name')[testName],
                div(class_='verdict')[verdict],
                div(class_='summary')[
                    'Summ'
                ]
            ]
        ]
        continue

    if 'Running' in row:
        # print(testName)
        content += [
            div(class_='test')[
                div(class_='test-name')[testName],
                div(class_='verdict')[verdict]
            ]
        ]
        continue
    # # check for the row like '3. 802.11ac Transmitter Test....'
    # if re.search(r" \d\.", row) is not None:
    #     print(row)


# print(content)
head_ = (
    '<meta charset="UTF-8">'
    '<meta http-equiv="X-UA-Compatible" content="IE=edge">'
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
    '<title>Document</title>'
    '<link rel="stylesheet" href="log.css">'
)
# print(flowTestContent[0].render())
# print(content)
page = html[
    head[head_],
    body[
        div(class_='log')[
            div(class_='details')['LOG DEMO REPORT'],
            *content
        ]
    ]
]
page = page.render()
# print(page)

f = open('index.html', 'w')
f.write(page)
f.close()


# wd = os.getcwd()
# result = subprocess.run('node bb', shell=True, capture_output=True, text=True, cwd=wd)
