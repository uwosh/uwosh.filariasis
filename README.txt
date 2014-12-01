Introduction
============
To install this product, include uwosh.filariasis in your Plone
buildout.cfg

TO DO
D2C metadata scripts need to be limited per form. Right now they wil
include any D2C form and will fail on forms without attributes that
other forms have. Just need to ad a check to make sure the attribute
the script is trying to index exists in the form.

Also the search script should be verified to only search inside a form
not site wide.
