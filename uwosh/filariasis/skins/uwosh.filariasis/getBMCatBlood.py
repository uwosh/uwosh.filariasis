if hasattr(context, 'portal_type') and context.portal_type == 'FormSaveData2ContentEntry':
  return context.getValue('microfilaremic-cat-blood-5cc-per-shipment-limit-1-shipment-quarter')
else:
  return None
