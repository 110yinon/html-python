import os
import subprocess

st = 'running from the'
kuni = st.split('running')
print(kuni.__len__())
for i in kuni:
    print(i)


# my spread operator
# bb = [1,2,3]
# print(bb)
# sara = []
# for i in bb:
#     sara += [i]

# print(sara)



# wd = os.getcwd()
# result = subprocess.run('node bb', shell=True, capture_output=True, text=True, cwd=wd)
# print(result)