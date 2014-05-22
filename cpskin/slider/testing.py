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
    plone (portal root)
    |
    |-- Commune
    |   `-- Services communaux
    |       `-- Finances
    |
    `-- Loisirs
        |-- Tourisme
        |   `-- Promenades
        |
        `-- Art & Culture
            |-- Bibliothèques
            `-- Artistes
                |-- Tata
                `-- Yoyo
    """

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'cpskin.slider:default')
        setRoles(portal, TEST_USER_ID, ['Manager'])
        login(portal, TEST_USER_NAME)
        api.content.create(
            type='Folder',
            title='ENSEIGNEMENT',
            id='enseignement',
            container=portal)


CPSKIN_SLIDER_FIXTURE = CPSkinSliderPloneWithPackageLayer(
    name="CPSKIN_SLIDER_FIXTURE",
    zcml_filename="configure.zcml",
    zcml_package=cpskin.slider)


CPSKIN_SLIDER_ROBOT_TESTING = FunctionalTesting(
    bases=(CPSKIN_SLIDER_FIXTURE, AUTOLOGIN_LIBRARY_FIXTURE,
           z2.ZSERVER_FIXTURE),
    name="cpskin.slider:Robot")
