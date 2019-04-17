from my_app.settings import app_cfg, init_settings
import os
import xlrd


def prep_files():




    return


def check_update_files(run_dir=app_cfg['UPDATES_DIR']):
    home = app_cfg['HOME']
    working_dir = app_cfg['WORKING_DIR']
    update_dir = app_cfg['UPDATES_DIR']
    archive_dir = app_cfg['ARCHIVES_DIR']

    path_to_main_dir = (os.path.join(home, working_dir))
    path_to_run_dir = (os.path.join(home, working_dir, run_dir))
    path_to_updates = (os.path.join(home, working_dir, update_dir))
    path_to_archives = (os.path.join(home, working_dir, archive_dir))

    update_files = os.listdir(path_to_updates)
    bookings = []
    start_row = 0
    as_of_date = ''

    print('Path to Main Dir:', path_to_main_dir)
    print('Path to Updates Dir:', path_to_updates)
    print('Path to Archives Dir:', path_to_archives)
    print('Path to Run Dir:', path_to_run_dir)

    # Does the run directory exist ?
    if not os.path.isdir(path_to_run_dir):
        print('*********')
        print('ERROR:', path_to_run_dir, 'does NOT exist')
        print('*********')
        exit()

    #
    # Open up excel workbook
    #
    # my_wb = xlrd.open_workbook(path_to_file)
    # my_sheet = my_wb.sheet_by_index(0)

    # Ok run dir exists check for files needed to run
    run_files = os.listdir(path_to_run_dir)
    date_list = []
    for run_file in run_files:
        # Ignore tmp_files
        if run_file[0:4] != 'tmp_':
            print(run_file)
            date_list.append((run_file[-13:-13 + 8]))
            file_path = (os.path.join(path_to_run_dir, run_file))
            my_wb = xlrd.open_workbook(file_path)
            # my_sheet = my_wb.sheet_by_index(1)
            print("Sheets", len(my_wb.sheet_names()))

    # 
    # print('File Date' , date_list)
    # print('rene',app_cfg['XLS_RENEWALS'])
    #
    #
    #
    #
    # print('Production Date:', app_cfg['PROD_DATE'])
    # print('Update Date:', app_cfg['UPDATE_DATE'])

    return


if __name__ == "__main__" and __package__ is None:
    print('Package Name:', __package__)
    print('running check_update_files')
    check_update_files(os.path.join(app_cfg['ARCHIVES_DIR'], '04-04-19 Updates'))
