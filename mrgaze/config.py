#!/opt/local/bin/python
"""
Configuration file supoort

This file is part of mrgaze.

    mrgaze is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    mrgaze is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with mrgaze.  If not, see <http://www.gnu.org/licenses/>.

Copyright 2014 California Institute of Technology.
"""

import os
import ConfigParser


def LoadConfig(data_dir, subjsess=''):
    """
    Load ET pipeline configuration parameters
    
    Check first for a global configuration in the root directory,
    then for a specific configuration in the subject/session directory.
    The subj/sess config has precedence.
    
    Arguments
    ----
    root_dir : string
        Root directory containing videos subdir.
    subjsess_dir : string
        Subject/Session subdirectory.
        
    Returns
    ----
    config : config object (see ConfigParser package)
        Configuration object.
    """
    
    # Root config filename
    root_cfg_file = os.path.join(data_dir, 'mrgaze.cfg')
    
    # Subject/Session config filename
    ss_dir = os.path.join(data_dir, subjsess)
    ss_cfg_file = os.path.join(ss_dir, 'mrgaze.cfg')
    
    # Create a new parser
    config = ConfigParser.ConfigParser()
    
    # Check first for subject/session config
    if os.path.isfile(ss_cfg_file):
        
        # Load existing subj/sess config file
        config.read(ss_cfg_file)

    elif os.path.isfile(root_cfg_file):
        
        # Load existing root config file
        config.read(root_cfg_file)
        
    else:

        # Write a new default root config file
        config = InitConfig(config)
        with open(root_cfg_file,'wb') as cfg_stream:
            config.write(cfg_stream)
            cfg_stream.close()
            
    return config
   

def SaveConfig(config, data_dir):
    """ Save configuration 

    Arguments
    ----
    config : Configuration settings
    data_dir : Directory to store the settings in 

    """

    # Root config filename
    root_cfg_file = os.path.join(data_dir, 'mrgaze.cfg')
    
    with open(root_cfg_file,'wb') as cfg_stream:
        config.write(cfg_stream)
        cfg_stream.close()
    
def InitConfig(config):
    
    # Add video defaults
    config.add_section('VIDEO')
    config.set('VIDEO','inputextension','.mpg')
    config.set('VIDEO','outputextension','.mov')
    config.set('VIDEO','inputfps','29.97')
    config.set('VIDEO','downsampling','4')
    config.set('VIDEO','border','16')
    config.set('VIDEO','rotate','0')
    config.set('VIDEO','gauss_sd','0')
    
    config.add_section('PUPILSEG')
    config.set('PUPILSEG','method','otsu')
    config.set('PUPILSEG','pupil_percmax','25')
    config.set('PUPILSEG','glint_percmax','1')
    config.set('PUPILSEG','pupil_threshold','20')
    config.set('PUPILSEG','k_inpaint', '5')
    config.set('PUPILSEG','k_dil','5')
    config.set('PUPILSEG','histogram_equalization','False')

    config.add_section('RANSAC')
    config.set('RANSAC','maxiterations','5')
    config.set('RANSAC','maxrefinements','3')
    config.set('RANSAC','maxinlierperc','95')
    
    config.add_section('LBP')
    config.set('LBP','enabled','True')
    config.set('LBP','minneighbors','40')
    config.set('LBP','scalefactor','1.05')
    
    config.add_section('ARTIFACTS')
    config.set('ARTIFACTS','mrclean','True')
    config.set('ARTIFACTS','zthresh','8.0')
    config.set('ARTIFACTS','motioncorr','highpass')
    config.set('ARTIFACTS','mocokernel','151')
    
    config.add_section('CALIBRATION')
    config.set('CALIBRATION','calibrate','False')
    config.set('CALIBRATION','targetx','[0.5, 0.1, 0.9, 0.1, 0.1, 0.5, 0.1, 0.9, 0.5]')
    config.set('CALIBRATION','targety','[0.5, 0.9, 0.9, 0.1, 0.9, 0.9, 0.5, 0.5, 0.1]')
    config.set('CALIBRATION','heatpercmin','5')
    config.set('CALIBRATION','heatpercmax','95')
    config.set('CALIBRATION','heatsigma','2.0')

    config.add_section('OUTPUT')
    config.set('OUTPUT','verbose','True')
    config.set('OUTPUT','graphics','False')
    config.set('OUTPUT','overwrite','True')
    
    return config
  
