if hasattr(context, 'portal_type') and context.portal_type == 'FormSaveData2ContentEntry':
  return context.getValue('principal-investigator-first-name').lower()
else:
  return None
