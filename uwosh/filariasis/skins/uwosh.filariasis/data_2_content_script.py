# This script takes existing form data in a saved data object and converts it to a content type
# Marcus DuFrane 

class REQUEST:
    pass

savedData = context['filarial-research-materials-parasite-division-requisition-form'].parasite_requisition
orderForms = context['filarial-research-materials-parasite-division-requisition-form'].get('order-forms')
formInput = savedData.getSavedFormInput()
columnNames = savedData.getColumnNames()

for i in formInput:
    request = REQUEST
    request.form = savedData.rowAsColDict(i,columnNames)
    orderForms.onSuccess(0, request)
