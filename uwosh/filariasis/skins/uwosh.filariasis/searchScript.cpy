# imports
from Products.CMFCore.utils import getToolByName
from DateTime import DateTime

def build_date_query(fromDate, toDate):
    date_list = list()  
    date_list.append(DateTime(fromDate))
    date_list.append(DateTime(toDate))
    return {"query":date_list, "range":"minmax"}  

#-------------------------------------------------

request = context.REQUEST
catalog = getToolByName(context, 'portal_catalog')

query = dict()

name = request.get('investigatorFirstName')
if name != '':
    query['indexByInvestigatorFirstName'] = name.lower()

name = request.get('investigatorLastName')
if name != '':
    query['indexByInvestigatorLastName'] = name.lower()

name = request.get('recipientFirstName')
if name != '':
    query['indexByRecipientFirstName'] = name.lower()

name = request.get('recipientLastName')
if name != '':
    query['indexByRecipientLastName'] = name.lower()


fromDate = request.get('fromDate')
toDate = request.get('toDate')
if fromDate != '' and toDate != '':
    query['indexByOrderDate'] = build_date_query(fromDate, toDate)

resultParam1 = ''
resultParam2 = ''
resultParam3 = ''
resultParam4 = ''
resultParam5 = ''
resultParam6 = ''

if request.get('parasiteType') == 'BM':
    query['indexByBMalayi'] = 'BM'
    resultParam1 = 'getBMAdultFemaleWorms'
    resultParam2 = 'getBMAdultMaleWorms'
    resultParam3 = 'getBMInfectiveLarvae'
    resultParam4 = 'getBML4Larvae'
    resultParam5 = 'getBMMFFromJirds'
    resultParam6 = 'getBMCatBlood'
elif request.get('parasiteType') == 'BP':
    query['indexByBPahangi'] = 'BP'
    resultParam1 = 'getBPAdultFemaleWorms'
    resultParam2 = 'getBPAdultMaleWorms'
    resultParam3 = 'getBPInfectiveLarvae'
    resultParam4 = 'getBPL4Larvae'
    resultParam5 = 'getBPMFFromJirds'
    resultParam6 = 'getBPDogBlood'
elif request.get('parasiteType') == 'DI':
    query['indexByDImmitis'] = 'DI'
    resultParam1 = 'getDIAdultFemaleWorms'
    resultParam2 = 'getDIAdultMaleWorms'
    resultParam3 = 'getDIInfectiveLarvae'
    resultParam4 = ''
    resultParam5 = ''
    resultParam6 = 'getDIDogBlood'
  
search_results = catalog.searchResults(query, sort_on = 'indexByOrderDate')

column_total_1 = 0
column_total_2 = 0
column_total_3 = 0
column_total_4 = 0
column_total_5 = 0
column_total_6 = 0

for i in search_results:
    try:
	column_total_1 += i[resultParam1]
    except:
	column_total_1 += 0
    try:	
	column_total_2 += i[resultParam2]
    except:
	column_total_2 += 0
    try:	
	column_total_3 += i[resultParam3]
    except:
	column_total_3 += 0
    try:    	
	column_total_4 += i[resultParam4]
    except:
	column_total_4 += 0
    try:	
	column_total_5 += i[resultParam5]
    except:
	column_total_5 += 0
    try:	
	column_total_6 += i[resultParam6]
    except:
	column_total_6 += 0

request.set('resultParam1', resultParam1)
request.set('resultParam2', resultParam2)
request.set('resultParam3', resultParam3)
request.set('resultParam4', resultParam4)
request.set('resultParam5', resultParam5)
request.set('resultParam6', resultParam6)
request.set('column_total_1', column_total_1)
request.set('column_total_2', column_total_2) 
request.set('column_total_3', column_total_3)
request.set('column_total_4', column_total_4)
request.set('column_total_5', column_total_5)
request.set('column_total_6', column_total_6)
request.set('search_results', search_results)
request.set('number_of_results', len(search_results))

state.setNextAction('traverse_to:string:order_search_results')
return state
