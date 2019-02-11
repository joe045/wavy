"""
file to specify model specifications such that models can be added 
and data can be imported easily
"""

from datetime import datetime, timedelta

model_dict={'ARCMFC':
            {'Hs':'VHM0',
            'lons':'lon',
            'lats':'lat',
            'rotlons':'rlon',
            'rotlats':'rlat',
            'time': 'time',
            'path':('/lustre/storeA/project/'
                    + 'copernicus/sea/mywavewam8r625/arctic/'),
            #'file_template':'%Y%m%d_MyWaveWam8r625_b%Y%m%d.nc',
            'file_template':'_MyWaveWam8r625_b%Y%m%d.nc',
            'basetime':datetime(1970,1,1),
            'units_time':'seconds since 1970-01-01 00:00:00',
            'delta_t':'0000-00-00 (01:00:00)'
            },
        'ARCMFCnew':
            {'Hs':'VHM0',
            'lons':'longitude',
            'lats':'latitude',
            'rotlons':'rlon',
            'rotlats':'rlat',
            'time': 'time',
            'path':('/lustre/storeB/users/anac/HINDCAST2017/BETAMAX1.20/'),
            'file_template':'%Y%m%d00.nc',
            'basetime':datetime(1970,1,1),
            'units_time':'seconds since 1970-01-01 00:00:00',
            'delta_t':'0000-00-00 (01:00:00)'
            },
        'mwam4':
            {'Hs':'hs',
            'lons':'longitude',
            'lats':'latitude',
            'rotlons':'rlon',
            'rotlats':'rlat',
            'time': 'time',
            'path_template':('/lustre/storeB/immutable/' +  
                           'archive/projects/metproduction/' + 
                           'DNMI_WAVE/%Y/%m/%d/'),
            'path':('/lustre/storeB/immutable/archive/' + 
                    'projects/metproduction/DNMI_WAVE/'),
            #'file_template':'MyWave_wam4_WAVE_%Y%m%dT%HZ.nc',
            'file_template':'MyWave_wam4_WAVE_%Y%m%dT%HZ.nc',
            'basetime':datetime(1970,1,1),
            'units_time':'seconds since 1970-01-01 00:00:00',
            'delta_t':'0000-00-00 (01:00:00)'
            },
        'mwam8':
            {'Hs':'VHM0',
            'lons':'longitude',
            'lats':'latitude',
            'rotlons':'rlon',
            'rotlats':'rlat',
            'time': 'time',
            'path_template':('/lustre/storeB/immutable/' +
                           'archive/projects/metproduction/' +
                           'DNMI_WAVE/%Y/%m/%d/'),
            'path':('/lustre/storeB/immutable/archive/' +
                    'projects/metproduction/DNMI_WAVE/'),
            #'file_template':'MyWave_wam8_WAVE_%Y%m%dT%HZ.nc',
            'file_template':'MyWave_wam8_WAVE_%Y%m%dT%HZ.nc',
            'basetime':datetime(1970,1,1),
            'units_time':'seconds since 1970-01-01 00:00:00',
            'delta_t':'0000-00-00 (01:00:00)'
            },
        'ecwam':
            {'Hs':'significant_wave_height',
            'lons':'longitude',
            'lats':'latitude',
            'time': 'time',
            'path_template':('/vol/data/ec/'),
            'path':('/vol/data/ec/'),
            'file_template':'ecwam_%Y%m%dT%HZ.nc',
            'basetime':datetime(1970,1,1),
            'units_time':'seconds since 1970-01-01 00:00:00',
            'delta_t':'0000-00-00 (01:00:00)'
            },
        'swanKC': # incomplete
            {'Hs':'VHM0',
            'lons':'longitude',
            'lats':'latitude',
            'time': 'time',
            'path_template':('/lustre/storeB/project/fou/om/SWAN/' 
                            + 'Sula/Nowind/OUTER/'),
            'path':('/lustre/storeB/project/fou/om/SWAN/' 
                            + 'Sula/Nowind/OUTER/'),
            'file_template':'swan_0wind%Y/%m/%d/.nc',
            'basetime':datetime(1970,1,1),
            'units_time':'seconds since 1970-01-01 00:00:00',
            'delta_t':'0000-00-00 (01:00:00)'
            },
        'MoskNC': # NOcurrents
            {'Hs':'hs',
            'rotlons':'rlon',
            'rotlats':'rlat',
            'time': 'time',
            'path_template':('/lustre/storeB/users/anac/resultscurr'
                            +'/experiment/NOcurrents/'),
            'path':('/lustre/storeB/users/anac/resultscurr'
                            +'/experiment/NOcurrents/'),
            # NOcurrentsWAVE2018021401.nc, NOcurrentsWAVE2018030100.nc
            'file_template':'NOcurrentsWAVE%Y%m*.nc',
            'file_coords':('/lustre/storeB/users/anac/resultscurr/' 
                     + 'experiment/TRUEcoordDepthc1exte.nc'),
            'basetime':datetime(1970,1,1),
            'units_time':'seconds since 1970-01-01 00:00:00',
            'delta_t':'0000-00-00 (01:00:00)'
            },
        'MoskWC': # withcurrents
            {'Hs':'hs',
            'rotlons':'rlon',
            'rotlats':'rlat',
            'time': 'time',
            'path_template':('/lustre/storeB/users/anac/resultscurr'
                            +'/experiment/withcurrents/'),
            'path':('/lustre/storeB/users/anac/resultscurr'
                            +'/experiment/withcurrents/'),
            'file_template':'withCWAVE%Y%m*.nc',
            'file_coords':('/lustre/storeB/users/anac/resultscurr/'
                    +'experiment/TRUEcoordDepthc1exte.nc'),
            'basetime':datetime(1970,1,1),
            'units_time':'seconds since 1970-01-01 00:00:00',
            'delta_t':'0000-00-00 (01:00:00)'
            },
        'Erin1W': # one way coupled experiment
            {'Hs':'hs',
            'lons':'longitude',
            'lats':'latitude',
            'time':'time',
            'path':('/lustre/storeB/users/erinet/coup_exp_output/'
                    + 'ST3_experiments/1waycoup_direct_ST3/'),
            'path_template':('/lustre/storeB/users/erinet'
                    + '/coup_exp_output/ST3_experiments/'
                    + '1waycoup_direct_ST3/'),
            'file_template':'ww3.%Y%m%dT%H_hs.nc',
            'basetime':datetime(1990,01,01),
            'units_time':'days since 1990-01-01 00:00:00',
            'time_conventions': ('relative julian days with decimal part' 
                        + ' as parts of the day'),
            'delta_t':'3h',
            '_FillValue':9.96921e+36
            },
        'Erin2W': # two way coupled experiment
            {'Hs':'hs',
            'lons':'longitude',
            'lats':'latitude',
            'time':'time',
            'path':('/lustre/storeB/users/erinet/coup_exp_output/'
                    + 'ST3_experiments/Exp2_direct_ST3/'),
            'path_template':('/lustre/storeB/users/erinet/'
                    + 'coup_exp_output/ST3_experiments/'
                    + 'Exp2_direct_ST3/'),
            'file_template':'ww3.%Y%m%dT%H_hs.nc',
            'basetime':datetime(1990,01,01),
            'units_time':'days since 1990-01-01 00:00:00',
            'time_conventions': ('relative julian days with decimal part'
                        + ' as parts of the day'),
            'delta_t':'3h',
            '_FillValue':9.96921e+36
            }
        }

explst = ['OPEWAVE','NoCBM1.2WAVE','withCurrBM1.2WAVE','BETAM106OPEWAVE','NoCWAVE','WithCWAVE','Erin1W','Erin2W']
