import masks

def mask_account_card(account_card: str) -> str:
    account_card_list = account_card.split()
    print(account_card_list)
    if account_card_list[0].lower() == 'счет':
        mask = masks.get_mask_account(account_card_list[1])
        return account_card_list[0] + ' ' + mask
    else:
        mask = masks.get_mask_card_number(account_card_list[-1])
        return ' '.join(account_card_list[0:-1]) + ' ' + mask



def get_date(date_need_to_format: str) -> str:
    formated_date = []
    date_need_to_format = date_need_to_format.split('-')
    formated_date.append(date_need_to_format[2][:2])
    formated_date.append(date_need_to_format[1])
    formated_date.append(date_need_to_format[0])
    return '.'.join(formated_date)

