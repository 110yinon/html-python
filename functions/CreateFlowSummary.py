import re
from chope import *
from chope.css import *
from functions.CreateSubTestNameElem import CreateSubTestNameElem


def CreateFlowSummary(flowDataString):
    summaryContent = []
    # split into sub tests
    subTests = re.split(r" (\d)+\. ",flowDataString)
    for subTest in subTests:
        # print(f'x------{subTest}')

        subTestContent = []
        subTestHead = []
        categoriesContent = []
        valuesRows = []

        # determine how much cols will be in the .iterates-categories, .iterate-values div's
        # default will be 6
        DEFAULT_GRID_COLS = 6
        gridColsNum = DEFAULT_GRID_COLS
        gridStyle = ''
        verdictValueStyle = ''


        # split the subTest paragrph into rows
        subTestRows = subTest.split('\n')
        for row in subTestRows:
            # print(f'x--- {row}')
            
            isVerdict = 'PASS' in row or 'FAILED' in row
            isVerticalBar = '|' in row

            testHeaderRow = isVerdict and not isVerticalBar
            testCategoriesRow = isVerdict is False and isVerticalBar
            istestValuesRow = isVerdict is True and isVerticalBar
            
            if testHeaderRow:
                # print(f'x--Header-- {row}')
                subTestHead = CreateSubTestNameElem(row)

            if testCategoriesRow:
                # print(f'x--CAT-- {row}')
                # seperates the categories in the row
                categories = row.split('|')
                # determine how much columns will be in the current subTest .iterates-categories, .iterate-values div's
                # the default is 6 - so if the no. cats will be greater so grid col num will be change
                numOfCats = categories.__len__()
                gridColsNum = numOfCats if numOfCats > DEFAULT_GRID_COLS else DEFAULT_GRID_COLS
                gridStyle = (
                    f'grid-template-columns: repeat({gridColsNum}, 1fr);'
                    # f'background-color:red'
                )
                verdictValueStyle=(
                    f'grid-column: {gridColsNum};'
                    # f'background-color:red'
                )

                for cat in categories:
                    catName = cat.strip()
                    categoriesContent += [
                            div(class_='category')[catName]
                    ]

            if istestValuesRow:
                # print(f'x--VAL-- {row}')
                # seperates the values in the row
                values = row.split('|')
                valuesRow = []
                
                for val in values:
                    value = val.strip()
                    isVerdictValue =  value == 'PASS' or value == 'FAILED'
                    className = 'value sub-test-verdict' if isVerdictValue else 'value'
                    valuesRow += [
                            div(class_=className, style=verdictValueStyle if isVerdictValue else '')[value]
                    ]
                    # end of a values row
                    if(value == 'PASS' or value == 'FAILED'):
                        passOrFailedClass = 'pass' if value == 'PASS' else 'failed'
                        valuesRows +=  [div(class_=f'iterate-values {passOrFailedClass}', style=gridStyle)[*valuesRow]]                         
            


        subTestContent = [
            div(class_='sub-test')[
                *subTestHead,
                div(class_='summary-subtest invisible')[
                    div(class_='iterates-categories', style=gridStyle)[*categoriesContent],
                    *valuesRows
                ]
            ]
        ]
        summaryContent += [*subTestContent]

        subTestHead=[]
        categoriesContent=[]
        valuesRows = []
        subTestContent = []

    return summaryContent