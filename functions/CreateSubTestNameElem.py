from chope import *
from chope.css import *

def CreateSubTestNameElem(row):
    rowVerdict = 'PASS' if 'PASS' in row else 'FAILED'
    subTestName = row.split(rowVerdict)[0]
    passOrFailedClass = 'pass' if rowVerdict == 'PASS' else 'failed'
    subTestHead = [           
        div(class_='sub-test-name')[subTestName],
        div(class_=f'verdict {passOrFailedClass}')[rowVerdict]                        
    ]
    return subTestHead
    
 