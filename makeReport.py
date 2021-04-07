import os


rep_name = input('Input report(dir) name: ')
# rep_name = 'report_23-03'
path = './'+rep_name+'/'
with open('test.txt', 'r') as tmp:
    tmp = tmp.readlines()

exp_list = os.listdir(path + 'img/')
print(exp_list)

th = '\t\t<tr><th>N</th>'
for exp in exp_list:
    th = th+'<th><p>{}</p></th>'.format(exp)
th = th+'</tr>\n'
tmp.append(th)

im_list = os.listdir(path + 'img/' + exp_list[0])

i = 1
print(im_list)
for im in im_list:
    if not im.isascii():
        continue
    td = '\t\t<tr><td>{}</td>'.format(i)
    for exp in exp_list:
        td = td + '<td><img src="img/{0}/{1}"></td>'.format(exp, im)
    td += '</tr>\n'
    tmp.append(td)
    i+=1


with open(path + 'index.txt', 'w') as out:
    tmp.append('\t</table>\n')
    tmp.append('</body>')
    out.writelines(tmp)

