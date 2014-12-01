## Controller Validator "formNotEmpty"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=
##title=
##
# Example validator code

# validate your variables here
recFirstName = context.REQUEST.get('recipientFirstName', None)
recLastName = context.REQUEST.get('recipientLastName', None)
invFirstName = context.REQUEST.get('investigatorFirstName', None)
invLastName = context.REQUEST.get('investigatorLastName', None)
toDate = context.REQUEST.get('toDate', None)
fromDate = context.REQUEST.get('fromDate', None)
BM = context.REQUEST.get('BMalayi', None)
BP = context.REQUEST.get('BPahangi', None)
DI = context.REQUEST.get('DImmitus', None)


if recFirstName is '' and recLastName is '' and invFirstName is '' and invLastName is '' and toDate is '' and fromDate is '' and BM is None and BP is None and DI is None:
   state.setError('isEmpty', 'Search Form cannot be empty')

if state.getErrors():
   # An error has occurred.  Set the status to 'failure' 
   # (the default initial status is 'success')
   state.setStatus('failure')

# No errors.  Always make sure to return the ControllerState object
return state
