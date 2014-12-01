from Products.Five import zcml
from Products.Five import fiveconfigure

from Testing import ZopeTestCase as ztc

from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

from AccessControl import Unauthorized
from mechanize._mechanize import LinkNotFoundError

from smtplib import SMTPRecipientsRefused
from Products.validation import validation

from Products.CMFCore.utils import getToolByName 

import uwosh.filariasis
import uwosh.pfg.d2c

@onsetup
def setup_uwosh_filariasis():
    fiveconfigure.debug_mode = True
    zcml.load_config('configure.zcml', uwosh.pfg.d2c)
    zcml.load_config('configure.zcml', uwosh.filariasis)
    fiveconfigure.debug_mode = False
    ztc.installPackage('uwosh.pfg.d2c')
    ztc.installPackage('uwosh.filariasis')

setup_uwosh_filariasis()
ptc.setupPloneSite()

class MockMailHost(object):
    """A mock mail host to avoid actually sending emails when testing."""

    def getId(self):
        return 'MailHost'

    def send(self, message, mto=None, mfrom=None, subject=None, encode=None):
        isEmail = validation.validatorFor('isEmail')
        if (isEmail(mto) == 1):
            return
        else:    
            raise SMTPRecipientsRefused
        
    def secureSend(self, message, mto=None, mfrom=None, subject=None, encode=None):
        isEmail = validation.validatorFor('isEmail')
        if (isEmail(mto) == 1):
            return
        else:    
            raise SMTPRecipientsRefused
        

class TestCase(ptc.PloneTestCase):
    """A base class for all the tests in this package."""
    
    def afterSetUp(self):
        self.portal.MailHost = MockMailHost()
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.loginAsPortalOwner()
        installer.installProduct('Products.PloneFormGen')
        installer.installProduct('uwosh.pfg.d2c')
        self.createFolders()
        self.importForm()
        print 'installing filariasis ...',
        installer.installProduct('uwosh.filariasis')
        print 'done'
        #check to see order form folder exists
        self.checkForOrderFormsFolder()
        

    def becomeManager(self):
        self.setRoles(['Authenticated', 'Member', 'Manager', 'Owner'])

    def createFolders(self):
        self.portal.invokeFactory('Folder', 'parasite-resources')
        self.portal['parasite-resources'].invokeFactory('Folder', 'requisitionUpdate')

    def importForm(self):
        print ''
        print 'importing form ...',
        self.portal['parasite-resources']['requisitionUpdate'].manage_importObject('filarial-research-materials-parasite-division-requisition-form.zexp')
        print 'done'
    #also turns off maileradapter
    def checkForOrderFormsFolder(self):
        form = self.portal['parasite-resources']['requisitionUpdate']['filarial-research-materials-parasite-division-requisition-form']['order-forms']
        form.setActionAdapter(('order-forms','parasite_requisition'))

class FunctionalTestCase(TestCase, ptc.FunctionalTestCase):
    pass
