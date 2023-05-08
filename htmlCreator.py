import os
import subprocess
import re
from chope import *
from chope.css import *
from functions.CreateSubTestNameElem import CreateSubTestNameElem
from functions.CreateFlowSummary import CreateFlowSummary


f = open("report.log.txt", "r")
fileContent = f.read()
# removing the duration string ('02.254 sec')
output_ = re.sub(r'(\d+)(\.)*(\d*) sec','', fileContent)
output_ = output_.replace('Duration Time:','')
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
    # print(f'x-----{row}')

    # separate the verdict and the '[test description]'from the test name header
    testName = row.split('Pass')[0].split('Failed')[0].split('[')[0]
    verdict = 'PASS' if 'Pass' in row else 'FAILED'

    if 'Flow File' in row:
        # print(row)

        # removing the 'running ...[] false\n' (the first line)
        # adding back the '1.' after remove it on split
        offTrailingRow = row.split(' 1.',1)[1].replace(' ', ' 1. ',1)
        # print(offTrailingRow)

        # summaryContent = []
        summaryContent = CreateFlowSummary(offTrailingRow)        

        
        content += [div(class_='flow-test')[
                div(class_='test-name')[testName],
                div(class_='verdict')[verdict],
                div(class_='summary invisible')[
                    *summaryContent
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
    ],
    '<script src="index.js"></script>'
]
page = page.render()
# print(page)

f = open('index.html', 'w')
f.write(page)
f.close()


# wd = os.getcwd()
# result = subprocess.run('node bb', shell=True, capture_output=True, text=True, cwd=wd)
