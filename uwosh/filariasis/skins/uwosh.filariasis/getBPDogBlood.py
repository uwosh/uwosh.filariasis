if hasattr(context, 'portal_type') and context.portal_type == 'FormSaveData2ContentEntry':
  return context.getValue('microfilaremic-dog-blood-20cc-per-shipment-limit-1-shipment-month')
else:
  return None
