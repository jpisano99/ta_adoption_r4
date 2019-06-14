#
# [Source Column Name, Which SS/Excel sheet ?, Source Column Num, NEW Column name]
#
sheet_map = [['ERP End Customer Name', 'XLS_BOOKINGS', -1, 'Customer Name'],
             ['End Customer Global Ultimate Name', 'XLS_BOOKINGS', -1, 'Customer Alias'],
             ['pss', 'SS_COVERAGE', -1, 'PSS'],
             ['tsa', 'SS_COVERAGE', -1, 'TSA'],
             ['Sales Agent Name', 'XLS_BOOKINGS', -1, 'AM'],
             ['Project Manager', 'SS_AS', -1, 'AS PM'],
             ['AS Engineer 1', 'SS_AS', -1, 'AS CSE 1'],
             ['AS Engineer 2', 'SS_AS', -1, 'AS CSE 2'],
             ['Project Status/PM Completion', 'SS_AS', -1, 'AS Status'],
             ['Delivery Comments', 'SS_AS', -1, 'AS Comments'],
             ['Provisioning completed', 'SS_SAAS', -1, 'SAAS Status'],
             ['CSM', 'SS_CX', -1, 'CX Contact'],
             ['Comments', 'SS_CX', -1, 'CX Next Steps'],
             # ['CuSM Name', 'SS_CX', -1, 'CX Contact'],
             # ['Next Action', 'SS_CX', -1, 'CX Next Steps'],

             ['Start Date', 'XLS_SUBSCRIPTIONS', -1, 'Sub Start'],
             ['Initial Term', 'XLS_SUBSCRIPTIONS', -1, 'Sub Initial Term'],
             ['Status', 'XLS_SUBSCRIPTIONS', -1, 'Sub Status'],
             # ['Renewal Date', 'XLS_SUBSCRIPTIONS', -1, 'Sub Renew Date'],


             ['Renewal Date', 'XLS_RENEWALS', -1, ' Next Renewal Date'],
             ['Product Bookings', 'XLS_RENEWALS', -1, 'Next Renewal Revenue'],
             ['Fiscal Quarter ID', 'XLS_RENEWALS', -1, 'Next Renewal Qtr'],
             ['Renewal Comments', '', -1, ''],
             ['Orders Found', '', -1, ''],
             ['Total Bookings', 'XLS_BOOKINGS', -1, ''],
             ['Service Bookings', '', -1, ''],
             ['Product Type', 'SS_SKU', -1, '*DELETE*'],
             ['Bundle Product ID', 'XLS_BOOKINGS', -1, '*DELETE*'],
             ['Product Description', 'SS_SKU', -1, 'Platform Type'],
             ['Sensor Count', 'SS_SKU', -1, ''],
             ['Active Sensors', '', -1, ''],
             ['Sales Level 1', 'XLS_BOOKINGS', -1, ''],
             ['Sales Level 2', 'XLS_BOOKINGS', -1, ''],
             ['Sales Level 3', 'XLS_BOOKINGS', -1, ''],
             ['Sales Level 4', 'XLS_BOOKINGS', -1, ''],
             ['Sales Level 5', 'XLS_BOOKINGS', -1, ''],
             ['Sales Level 6', 'XLS_BOOKINGS', -1, '']]

sheet_keys = [['XLS_BOOKINGS', 'ERP End Customer Name', -1],
              # ['SS_CX', 'Account Name', -1],
              ['SS_CX', 'Customer', -1],
              ['SS_SAAS', 'Customer name', -1],
              ['SS_AS', 'Customer Name', -1]]
