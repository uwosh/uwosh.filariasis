from Products.CMFCore.utils import getToolByName

def install(context):     
    site = context.getSite()   
    form = site['parasite-resources']['requisitionUpdate']['filarial-research-materials-parasite-division-requisition-form']
    if not form.hasObject('order-forms'):       
        folder =  form[form.invokeFactory('FormSaveData2ContentAdapter', 'order-forms')]
        folder.setTitleField('order-date')    
        folder.setTitle('Parasite Order Forms')    
        folder.setActionAdapter(('order-forms','parasite_requisition','custommaileradapter'))
        form.data_2_content_script()
        catalog = getToolByName(site, 'portal_catalog')
        catalog.manage_catalogRebuild()
    folder = site['parasite-resources']['requisitionUpdate']
    if not folder.hasObject('parasitesearchform'):       
        link = folder.invokeFactory('Link', 'parasitesearchform')
        link = folder[link]
        link.setTitle('Parasite Search Form')
        link.setRemoteUrl('./order_search_form')
        link.setLocation('./order_search_form')
   
