import zipfile
import os
import pandas as pd
import shutil

root_dir = r'\\ma2vwfp01\HPC_Group\Engineering\EE_Testing\High Performance Testers\TCR_Testing\Test Data\TCR-3 AWS Q56 DVP Testing\MEL-1034 Low Temp Storage\Zips'
os.mkdir(os.path.join(root_dir,'fixed_zips'))
for zip_file in os.listdir(root_dir):
    if zip_file != 'fixed_zips':
        zf = zipfile.ZipFile(os.path.join(root_dir,zip_file))
        dstfile = os.path.join(root_dir,'fixed_zips',zip_file)
        shutil.make_archive(zip_file, 'zip', os.path.join(root_dir,'fixed_zips'))
        outzip = zipfile.ZipFile(dstfile, "w")
        # Iterate the input files
        for inzipinfo in zf.infolist():
            infile = zf.open(inzipinfo)
            if inzipinfo.filename == "BERT-DATA.csv":
                df = pd.read_csv(zf.open('BERT-DATA.csv'))
                df['tested_ber'] = df['errors'] / df['bits']
                df.to_csv("BERT-DATA.csv", index=None, sep=",", header=True, encoding='utf-8-sig')
                outzip.write(inzipinfo.filename, "BERT-DATA.csv")
            else:  # Other file, dont want to modify => just copy it
                content = infile.read()
                outzip.writestr(inzipinfo.filename, content)
        zf.close()
        outzip.close()