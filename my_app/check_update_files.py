from my_app.settings import app_cfg, init_settings
from my_app.func_lib.push_list_to_xls import push_list_to_xls
import os
import xlrd
import json


def prep_raw_files():
    bookings = []
    start_row = 2
    wb = xlrd.open_workbook(file_path)
    ws = wb.sheet_by_index(0)
    for row in range(start_row, ws.nrows):
        bookings.append(ws.row_values(row))

    push_list_to_xls(bookings, 'tmp_working_bookings', 'updates')
    return


def file_checks(run_dir=app_cfg['UPDATES_DIR']):
    home = app_cfg['HOME']
    working_dir = app_cfg['WORKING_DIR']
    update_dir = app_cfg['UPDATES_DIR']
    archive_dir = app_cfg['ARCHIVES_DIR']

    path_to_main_dir = (os.path.join(home, working_dir))
    if not os.path.exists(path_to_main_dir):
        print(path_to_main_dir, " does NOT Exist !")
        exit()

    path_to_run_dir = (os.path.join(home, working_dir, run_dir))
    if not os.path.exists(path_to_run_dir):
        print(path_to_run_dir, " does NOT Exist !")
        exit()

    path_to_updates = (os.path.join(home, working_dir, update_dir))
    if not os.path.exists(path_to_updates):
        print(path_to_updates, " does NOT Exist !")
        exit()

    path_to_archives = (os.path.join(home, working_dir, archive_dir))
    if not os.path.exists(path_to_archives):
        print(path_to_archives, " does NOT Exist !")
        exit()

    if not os.listdir(path_to_run_dir):
        print('Directory', path_to_run_dir, 'contains NO files')
        exit()

    #  Get the required Files
    files_needed = {}
    # Do we have RAW files to process ?
    for var in app_cfg:
        if var.find('RAW') != -1:
            # Look for any config var containing the word 'RAW'
            files_needed[app_cfg[var]] = 'Missing'

    # See if we have the files and they have consistent dates
    run_files = os.listdir(path_to_run_dir)
    date_list = []
    for file_needed, status in files_needed.items():
        for run_file in run_files:
            date_tag = run_file[-13:-13 + 8]  # Grab the date if any
            run_file = run_file[:len(run_file)-14]  # Grab the name without the date
            if run_file == file_needed:
                date_list.append(date_tag)  # Grab the date
                files_needed[file_needed] = 'Found'
                break

    base_date = date_list[0]
    for date_stamp in date_list:
        if date_stamp != base_date:
            print('ERROR: Inconsistent date stamp found')
            exit()

    # Read the config_dict.json file
    # with open(os.path.join(path_to_run_dir, app_cfg['META_DATA_FILE'])) as json_input:
    #     config_dict = json.load(json_input)
    # print(config_dict)

    # Since we have a consistent date then Create the json file for config_data.json. Put the time_stamp in it
    config_dict = {'run_time_stamp': base_date}
    with open(os.path.join(path_to_run_dir, app_cfg['META_DATA_FILE']), 'w') as json_output:
        json.dump(config_dict, json_output)

    for file_name, status in files_needed.items():
        if status != 'Found':
            print('ERROR: File ', file_name, 'is missing')
            exit()

    #
    # We now have all files to re-create a new set of data

    # Delete all previous tmp_ files
    for file_name in run_files:
        if file_name[0:4] == 'tmp_':
            os.remove(os.path.join(path_to_run_dir, file_name))

    # Here is what we have
    print('Our directories:')

    print('\tPath to Main Dir:', path_to_main_dir)
    print('\tPath to Updates Dir:', path_to_updates)
    print('\tPath to Archives Dir:', path_to_archives)
    print('\tPath to Run Dir:', path_to_run_dir)

    processing_date = date_list[0]
    print('We are processing files:')
    for file_name in files_needed:
        print('\t\t', file_name + '', processing_date + '.xlsx')
    exit()

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
    file_list = []
    for run_file in run_files:
        # Ignore tmp_files
        if run_file[0:4] != 'tmp_':
            print(run_file)
            date_list.append((run_file[-13:-13 + 8]))
            file_path = (os.path.join(path_to_run_dir, run_file))
            file_list.append(file_path)
            # my_wb = xlrd.open_workbook(file_path)
            # my_sheet = my_wb.sheet_by_index(1)
            # print("Sheets", len(my_wb.sheet_names()))

    # 
    print('File Dates', date_list)
    print('File List', file_list)
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
    #file_checks(os.path.join(app_cfg['UPDATES_DIR']))
    file_checks(os.path.join(app_cfg['ARCHIVES_DIR'], '04-04-19 Updates'))
