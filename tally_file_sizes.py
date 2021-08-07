#!/usr/bin/env python
"""
simple script to tally the sizes of certain files
"""
import os

def convert_unit(size_in_bytes, unit=['KB','MB','GB']):
    """ Convert the size from bytes to other units like KB, MB or GB"""
    if unit == 'KB':
        return size_in_bytes / 1024
    elif unit == 'MB':
        return size_in_bytes / 1024 / 1024
    elif unit == 'GB':
        return size_in_bytes / 1024 / 1024 / 1024



stash,total={}, 0
for f in mydir:
    if 'backup_dump' in f and 'NOT_CLIENT' not in f:
        print(f, convert_unit(os.path.getsize(basedir+f),'MB'),"GB")
        total += os.path.getsize(basedir+f)
print('Total:' convert_unit(total, 'GB'),'GB')

"""
output:
backup_dump_projectA-full.sql 2145.4968852996826 GB
backup_dump_20130414.sql 2475.9488344192505 GB
backup_dump_2013111.sql 1564.594235420227 GB
backup_dump_Test_Main-full.sql 2265.615448951721 GB
backup_dump_Test_Main2-full.sql 781.2829484939575 GB
backup_dump_newdump.sql 6163.531819343567 GB
backup_dump_20161203.sql 1751.5321989059448 GB
backup_dump_20170502-full.sql 1829.625813484192 GB
backup_dump_REORG.sql 1262.0367527008057 GB
backup_dump_NEWBACKUP.sql 665.3457975387573 GB
backup_dump_Demo3.sql 6163.531819343567 GB
backup_dump_Demo3.1.sql 1971.8606157302856 GB
backup_dump_Demo3xx-full.sql 6163.531819343567 GB
backup_dump_prod_checkpoint.sql 6163.531819343567 GB
backup_dump_newclient.sql 4328.522013664246 GB
backup_dump_2019-Main.sql 2379.44536113739 GB
backup_dump_newdump_Jan-full.sql 1775.792392730713 GB

Total 48.68283845297992 GB

"""
