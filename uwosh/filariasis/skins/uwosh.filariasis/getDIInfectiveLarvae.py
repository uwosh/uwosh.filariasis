if hasattr(context, 'portal_type') and context.portal_type == 'FormSaveData2ContentEntry':
  return context.getValue('infective-larvae-1000-l3-request-limit-5-shipments-year')
else:
  return None
