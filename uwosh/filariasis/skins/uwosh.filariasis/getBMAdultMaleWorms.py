if hasattr(context, 'portal_type') and context.portal_type == 'FormSaveData2ContentEntry':
  return context.getValue('adult-male-worms-30-per-request-limit-10-shipments-year')
else:
  return None
l
