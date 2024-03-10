'''
@version: 1.0.0
@author: 1chooo
@date: 2023/05/07

`unit_test.py`
'''

def check_merge_result(source_data, merged_data) -> None:

    source_data_len = len(source_data)
    merged_data_len = len(merged_data)

    if source_data_len / merged_data_len == 2:
        print('Merged Successful!')
    else:
        print('Merge Failed!')
        print('Lenght of source data:', source_data_len)
        print('Lenght of modified data:', merged_data_len)


def check_modified_data(modified_datas) -> None:

    if len(modified_datas) == 1440 and len(modified_datas[0]) == 9:

        print('Successful')

    else:
        print(len(modified_datas))
        print(len(modified_datas[0]))
        print('Failed!')