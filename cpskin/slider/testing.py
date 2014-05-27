# -*- coding: utf-8 -*-

from plone import api
from plone.testing import z2
from plone.app.testing import FunctionalTesting
from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import applyProfile
from plone.app.testing import (login,
                               TEST_USER_NAME,
                               setRoles,
                               TEST_USER_ID)
from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE

import cpskin.slider


class CPSkinSliderPloneWithPackageLayer(PloneWithPackageLayer):
    """
    """

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'cpskin.slider:default')
        setRoles(portal, TEST_USER_ID, ['Manager'])
        login(portal, TEST_USER_NAME)
        api.content.create(
            type='News Item',
            title='Foire aux boudins',
            description='Superbe foire',
            container=portal)
        api.content.create(
            type='News Item',
            title='Festival de danse folklorique',
            description='Parfois synonyme de danse folklorique ou de danse traditionnelle...',
            container=portal)
        collection = api.content.create(
            type='Collection',
            title='SliderCollection',
            container=portal)
        collection.setLayout('slider_view')
        query = [{'i': 'Type',
                  'o': 'plone.app.querystring.operation.string.is',
                  'v': 'News Item',
                  }]
        collection.setQuery(query)


CPSKIN_SLIDER_FIXTURE = CPSkinSliderPloneWithPackageLayer(
    name="CPSKIN_SLIDER_FIXTURE",
    zcml_filename="configure.zcml",
    zcml_package=cpskin.slider)


CPSKIN_SLIDER_ROBOT_TESTING = FunctionalTesting(
    bases=(CPSKIN_SLIDER_FIXTURE, AUTOLOGIN_LIBRARY_FIXTURE,
           z2.ZSERVER_FIXTURE),
    name="cpskin.slider:Robot")
