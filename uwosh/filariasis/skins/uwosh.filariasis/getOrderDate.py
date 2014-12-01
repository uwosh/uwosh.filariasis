if hasattr(context, 'portal_type') and context.portal_type == 'FormSaveData2ContentEntry':
  return context.getValue('order-date')
else:
  return None
