if hasattr(context, 'portal_type') and context.portal_type == 'FormSaveData2ContentEntry':
  return context.getValue('l4-larvae-300-l4-request-limit-10-shipments-year-2')
else:
  return None
