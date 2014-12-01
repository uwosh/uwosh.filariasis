if hasattr(context, 'portal_type') and context.portal_type == 'FormSaveData2ContentEntry':
    index = None    
    if context.getValue('brugia-pahangi') != 'None' or ('B. pahangi' in context.getValue('a-aegypti-infected-with-filariae')):
        if context.getValue('brugia-pahangi') == '':
            index = None
        else:
            index = 'BP'
    return index
else:
    return None
