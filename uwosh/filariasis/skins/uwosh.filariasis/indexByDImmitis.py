if hasattr(context, 'portal_type') and context.portal_type == 'FormSaveData2ContentEntry':
    index = None    
    if context.getValue('dirofilaria-immitis') != 'None' or ('D. immitis' in context.getValue('a-aegypti-infected-with-filariae')):
        if context.getValue('dirofilaria-immitis') == '':
            index = None
        else:
            index = 'DI'
    return index
else:
    return None
