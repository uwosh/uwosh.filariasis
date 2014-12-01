if hasattr(context, 'portal_type') and context.portal_type == 'FormSaveData2ContentEntry':
    index = None
    
    if context.getValue('brugia-malayi') != 'None' or ('B. malayi' in context.getValue('a-aegypti-infected-with-filariae')):
        if context.getValue('brugia-malayi') == '':
            index = None
        else:
            index = 'BM'
    return index
else:
    return None
