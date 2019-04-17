'''
python script to generate ground truth label_file for classification part and proposal file for
proposal generation part

Example:
python process_proposal.py TH14_Temporal_annotations_validation

Output:
label_file: contains all the name of frame that should be classified as containing actions
proposal_file: contains all the name of video that has action annotations, the first line is
    video_name and the number of proposals N split by space. The following N lines are the start
    and end point of action proposals

'''

import os
import sys

file_dir = sys.argv[1]
label_res = []
proposal_res = {}
for filename in os.listdir(file_dir):
    with open(file_dir+filename, 'r') as file:
        for line in file:
            line_split = line.split()
            name = line_split[0]
            a = int(float(line_split[1]) * 10)
            b = int(float(line_split[2]) * 10)
            if name in proposal_res:
                proposal_res[name].append((a,b))
            else:
                proposal_res[name] = [(a,b)]
            for i in range(a,b+1):
                idx = '0'*(4-len(str(i))) + str(i)
                label_res.append(name + '_' + idx)

label_res.sort()
with open('label_file', 'w') as label_file:
    for label in label_res:
        label_file.write("%s\n" % label)

with open('proposal_file', 'w') as proposal_file:
    for key in sorted(proposal_res.keys()):
        proposal_file.write("%s %d\n" % (key, len(proposal_res[key])))
        for proposal in proposal_res[key]:
            proposal_file.write("%d %d\n" % (proposal[0], proposal[1]))
