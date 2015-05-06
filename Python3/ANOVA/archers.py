#!/usr/bin/env python
"""
(C) 2015 Nikolay Manchev, [CleverOwl blog](http://http://www.cleverowl.uk)
This work is licensed under the Creative Commons Attribution 4.0 International
License. To view a copy of this license, visit
http://creativecommons.org/licenses/by/4.0/.
"""

import numpy as np

from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison
from scipy import stats

data = np.rec.array([
('Pat', 5),
('Pat', 4),
('Pat', 4),
('Pat', 3),
('Pat', 9),
('Pat', 4),
('Jack', 4),
('Jack', 8),
('Jack', 7),
('Jack', 5),
('Jack', 1),
('Jack', 5),
('Alex', 9),
('Alex', 8),
('Alex', 8),
('Alex', 10),
('Alex', 5),
('Alex', 10)], dtype = [('Archer','|U5'),('Score', '<i8')])

f, p = stats.f_oneway(data[data['Archer'] == 'Pat'].Score,
	              data[data['Archer'] == 'Jack'].Score,
                      data[data['Archer'] == 'Alex'].Score)

print ('One-way ANOVA')
print ('=============')

print ('F value:', f)
print ('P value:', p, '\n')

mc = MultiComparison(data['Score'], data['Archer'])
result = mc.tukeyhsd()

print(result)
print(mc.groupsunique)
