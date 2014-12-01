if hasattr(context, 'portal_type') and context.portal_type == 'FormSaveData2ContentEntry':
  return context.getValue('mf-from-peritoneal-cavity-of-jirds-2-m-mf-per-request-limit-1-shipment-month')
else:
  return None
