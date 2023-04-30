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
        # print(row)

        # removing the 'running ...[] false\n' (the first line)
        # adding back the '1.' after remove it on split
        offTrailingRow = row.split(' 1.',1)[1].replace(' ', '  1. ',1)
        # print(sara)

        summaryContent = []

        # split into sub tests
        subTests = re.split(r" \d\. ",offTrailingRow)
        for subTest in subTests:
            # print(subTest)

            subTestContent = []
            subTestHead = []
            categoriesContent = []
            valuesContent = []

            # split the subTest paragrph into rows
            subTestRows = subTest.split('\n')
            for row in subTestRows:
                # print(f'x--- {row}')
                
                isVerdict = 'PASS' in row or 'FAILED' in row
                isVerticalBar = '|' in row

                testHeaderRow = isVerdict and not isVerticalBar
                testCategoriesRow = isVerdict is False and isVerticalBar
                testValuesRow = isVerdict is True and isVerticalBar
                
                if testHeaderRow:
                    # print(f'x--Header-- {row}')
                    rowVerdict = 'PASS' if 'PASS' in row else 'FAILED'
                    subTestName = row.split(rowVerdict)[0]
                    subTestHead = [                        
                        div(class_='sub-test-name')[subTestName],
                        div(class_='verdict')[rowVerdict]                        
                    ]

                if testCategoriesRow:
                    # print(f'x--CAT-- {row}')
                    # seperates the categories in the row
                    categories = row.split('|')
                    
                    for cat in categories:
                        catName = cat.strip()
                        categoriesContent += [
                                div(class_='category')[catName]
                        ]

                if testValuesRow:
                    # print(f'x--VAL-- {row}')
                    # seperates the values in the row
                    values = row.split('|')
                    
                    for val in values:
                        valuesContent += [
                                div(class_='value')[val.strip()]
                        ] 


                subTestContent = [
                    div(class_='sub-test')[
                        *subTestHead,
                        div(class_='iterates-categories')[*categoriesContent],
                        div(class_='iterate-values')[*valuesContent]
                    ]
                ]
                summaryContent += [*subTestContent]

                subTestHead=[]
                categoriesContent=[]
                valuesContent=[]
                subTestContent = []
                continue

        
        content += [div(class_='flow-test')[
                div(class_='test-name')[testName],
                div(class_='verdict')[verdict],
                div(class_='summary')[
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
    ]
]
page = page.render()
# print(page)

f = open('index.html', 'w')
f.write(page)
f.close()


# wd = os.getcwd()
# result = subprocess.run('node bb', shell=True, capture_output=True, text=True, cwd=wd)
