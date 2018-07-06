import os
import sys
import shutil
import re
import zipfile

# Pack one testcase to a .zip file by its index.
def pack_one(index):
    fr = open('../data/templates/{0}.txt'.format(index))
    folder_dir = '../data/testcases/{0}'.format(index)
    zip_dir = '../data/packages'
    # Remove the old folder and the old .zip file.
    if os.path.exists(folder_dir):
        shutil.rmtree(folder_dir)
    if os.path.exists(zip_dir + '/' + index + '.zip'):
        os.remove(zip_dir + '/' + index + '.zip')
    # Make new folder
    os.makedirs(folder_dir)
    # Split the testcases
    cases = re.compile("\$\$\$.*\n").split(fr.read().strip())
    # Delete the '$$$...' from last test case
    if len(cases) > 0:
        idx_last = cases[-1].rfind('\n')
        cases[-1] = cases[-1][:idx_last]
    for (i, each) in enumerate(cases):
        [in_file, out_file] = each.split('&&&\n')
        with open('../data/testcases/{0}/{1}.in'.format(index, i + 1), 'w') as fw:
            fw.write(in_file)
        with open('../data/testcases/{0}/{1}.out'.format(index, i + 1), 'w') as fw:
            fw.write(out_file)
    fr.close()
    # Get all the files to be ziped, ignoring the hidden files.
    files = [ each for each in os.listdir('../data/testcases/{0}'.format(index)) if not each.startswith('.') ]
    # Zip the files 
    source_dir = os.getcwd()
    os.chdir('../data/testcases/{0}'.format(index))
    with zipfile.ZipFile('../../packages/{0}.zip'.format(index), 'w') as myzip:
        for f in files: 
            myzip.write(f)
    os.chdir(source_dir)

# Pack all the testcases in ../data/templates
def pack_all():
    # Get all the templates index, ignoring the hidden files
    templates_idx = [ each.split('.')[0] for each in os.listdir('../data/templates') if not each.startswith('.') ]
    for idx in templates_idx:
        pack_one(idx)

if __name__=='__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'all':
        pack_all()
    elif len(sys.argv) > 1:
        pack_one(sys.argv[1])
    else:
        print('''
Usage examples:
    python3 pack.py 1
        ## pack one testcase by the index. this will overwrite the folder in '../data/testcases' and the .zip file in '../data/packages'
    python3 pack.py all
        ## run above command for each template in '../data/templates'
        ''')
