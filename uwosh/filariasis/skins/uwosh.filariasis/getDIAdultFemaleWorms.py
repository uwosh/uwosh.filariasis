if hasattr(context, 'portal_type') and context.portal_type == 'FormSaveData2ContentEntry':
  return context.getValue('adult-female-worms-limit-as-available')
else:
  return None
