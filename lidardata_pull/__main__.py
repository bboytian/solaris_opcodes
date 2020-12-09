# imports
import datetime as dt
import subprocess as sub

from ..global_imports.solaris_opcodes import *


# main func
@verbose
@announcer
def main(
        lidar_ip, lidaruser, idrsa_dir,
        lidardata_dir,
        lidarname,
        syncday_lst
):
    '''
    pulls the data from the lidar laptop.
    By default syncs current day and previous day's data.

    Parameters
        lidar_ip (str): IP address of the lidar laptop
        lidaruser (str): username of the lidar laptop
        lidardata_dir (str): directory containing all the date directories
                             that contain the lidar data
        lidarname (str): name of lidar in the solaris server
        syncday_lst (lst): list objects are strings of the format DATEFMT
    '''
    # rsync
    cmd_l = [
        'rsync',
        '-azzvi',
        f"-e '{DIRCONFN(WINDOWFILESDIR, SSHFILE)}' -o 'StrictHostKeyChecking=no' -i '{idesa_dir}'",
        # f"-e ssh -o 'StrictHostKeyChecking=no' -i '{IDRSADIR}'",
        '{}@{}:{}/./{{{}}}'.format(
            lidaruser, lidar_ip, lidardata_dir,
            ','.join(syncday_lst)
        ),
        SOLARISMPLDIR.format(lidarname)
    ]
    cmd_subrun = sub.run(cmd_l, stdout=sub.PIPE, stderr=sub.STDOUT)
    print(cmd_subrun.stdout.decode('utf-8'))


# running
if __name__ == '__main__':
    '''
    Test out the transfer without the need for using ssh
    '''
    main(
        '172.16.39.48', 'mpluser',
        'C:/Users/mpluser/Desktop/smmpl_E2',
        'smmpl_E2',
        [
            'test'
        ]
    )
