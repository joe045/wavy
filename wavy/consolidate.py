#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------#
'''
The main task of this module is to consolidate multiple sources of 
observations to perform a collective collocation/analysis
'''
# --- import libraries ------------------------------------------------#
# standard library imports
import numpy as np
from datetime import datetime

# own imports
from wavy.utils import flatten
from wavy.satmod import satellite_class
from wavy.insitumod import insitu_class
from wavy.wconfig import load_or_default
from wavy.quicklookmod import quicklook_class_sat as qls
# ---------------------------------------------------------------------#

# read yaml config files:
variable_info = load_or_default('variable_info.yaml')

# --- global functions ------------------------------------------------#

def consolidate_scos(scos):
    """
    consolidate sco.vars: 
        'sea_surface_wave_significant_height', 'time',
        'latitude', 'longitude', 'datetime'
    """
    varlst = []
    lonlst = []
    latlst = []
    timelst = []
    dtimelst = []
    for sco in scos:
        varlst.append(sco.vars[sco.stdvarname])
        lonlst.append(sco.vars['longitude'])
        latlst.append(sco.vars['latitude'])
        timelst.append(sco.vars['time'])
        dtimelst.append(sco.vars['datetime'])
    # flatten all, make arrays
    varlst = np.array(flatten(varlst))
    lonlst = np.array(flatten(lonlst))
    latlst = np.array(flatten(latlst))
    timelst = np.array(flatten(timelst))
    dtimelst = np.array(flatten(dtimelst))
    # sort according to time
    idx = np.argsort(timelst)
    # make dict
    vardict = {
            sco.stdvarname:varlst[idx],
            'longitude':lonlst[idx],
            'latitude':latlst[idx],
            'time':timelst[idx],
            'time_unit':sco.vars['time_unit'],
            'datetime':dtimelst[idx] }
    return vardict

def find_valid_oco(ocos):
    state = False
    for i,o in enumerate(ocos):
        if 'vars' in vars(o).keys():
            state = True
            break
    if state is True:
        return i
    else:
        print("")
        print("Caution: no valid observation object with values found!")
        print("")


# --------------------------------------------------------------------#

class consolidate_class(qls):
    '''
    Class to handle multiple satellite_class objects
    '''
    def __init__(self,ocos):
        print('# ----- ')
        print(" ### Initializing consolidate_class object ###")
        print(" ")
        i = find_valid_oco(ocos)
        self.ocos = ocos
        self.varalias = ocos[i].varalias
        self.stdvarname = ocos[i].stdvarname
        self.varname = ocos[i].varname
        self.units = ocos[i].units
        self.sdate = ocos[i].sdate
        self.edate = ocos[i].edate
        self.vars = consolidate_scos(ocos)
        self.obsname = 'consolidated-obs'
        self.obstype = 'consolidated-obs'
        self.label = 'consolidated-obs'
        self.mission = 'mission'
        self.product = 'product'
        self.provider = 'provider'
        self.nID = 'nID'
        self.sensor = 'sensor'
        print(" ")
        print (" ### consolidate_class object initialized ###")
        print ('# ----- ')

    def rename_consolidate_object_parameters(self,**kwargs):
        if kwargs.get('obsname') is not None:
            self.obsname = kwargs.get('obsname')
        if kwargs.get('mission') is not None:
            self.mission = kwargs.get('mission')
        if kwargs.get('obstype') is not None:
            self.obstype = kwargs.get('obstype')
        if kwargs.get('product') is not None:
            self.product = kwargs.get('product')
        if kwargs.get('provider') is not None:
            self.provider = kwargs.get('provider')
        if kwargs.get('nID') is not None:
            self.nID = kwargs.get('nID')
        if kwargs.get('sensor') is not None:
            self.sensor = kwargs.get('sensor')
        return
