#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
# oe_bls_cex
## Overview

{see README file}

This process:
- downloads the data needed for the spending models
- interprets that data and its metadata, applying BLS business rules
- trains two models a regressor and a penetration
- applies these to the American Community Survey
to generate the YYYYblockgroupspending data publication.
---


"""

import pandas as pd
import numpy as np
from datetime import datetime
import wget
import zipfile
import os
import warnings
warnings.simplefilter("ignore")

from oe_bls_pumd import 
def oe_cex_pumd_download(years, pumddir = './pumd/', cexurl='https://www.bls.gov/cex/'):
    """

    """

    return None

if __name__ == "__main__":
    
    # Get the PUMD 
    #   Download
    #   Read
    #   Interpret
    #   Check against MSA level reporting
    
    # Train the regressor model
    # Train the penetration model
    
    # Get the ACS for the selected year
    # Apply the models to ACS demographics
    
    # Write results to CSV
    
