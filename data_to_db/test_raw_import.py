# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 10:36:00 2015

@author: ailij_000
"""

import nose
import raw_import as raw

def test_b():
    assert 'b' == 'b'

class test_csv:
    def test_open_file(self):
        assert raw.open_file() == True

    
if __name__ == '__main__':
   nose.run(argv=["verbosity=3"])
