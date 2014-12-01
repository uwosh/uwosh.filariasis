if hasattr(context, 'portal_type') and context.portal_type == 'FormSaveData2ContentEntry':
  return context.getValue('a-aegypti-infected-with-filariae')
else:                      
  return None
