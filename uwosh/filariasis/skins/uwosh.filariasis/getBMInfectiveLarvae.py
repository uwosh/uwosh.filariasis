if hasattr(context, 'portal_type') and context.portal_type == 'FormSaveData2ContentEntry':
  return context.getValue('infective-larvae-300-l3-request-limit-10-shipments-year')
else:
  return None
