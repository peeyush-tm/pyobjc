# Generate list of signatures. 
#
# This is prelimanary code, we should probably query the Objective-C runtime
# for signatures.
#
types="@iIsSf"
max_args=3

def fun(pfx, left):
	if left==0:
		print pfx
		return

	for c in types:
		fun(pfx + c, left-1)

for i in range(max_args+1):
	for ch in "v" + types:
		fun(ch + "@:", i)
