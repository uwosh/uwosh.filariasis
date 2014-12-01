from DateTime import DateTime
import logging
logger=logging.getLogger('uwosh.filariasis')
if hasattr(context, 'portal_type') and context.portal_type == 'FormSaveData2ContentEntry':
    theString = context.getValue('order-date')
    try:
        return DateTime(theString)
    except Exception, e:
        logger.info('exception is %s for datetime string "%s" from object %s' % (e, theString, context))
        return None
else:
  return None
