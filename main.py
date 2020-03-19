import sys

def mapping(s1, s2):
	if len(s1) <= len(s2):
		d = {}
		for i in range(len(s1)):
			if s1[i] not in d:
				d[s1[i]] = s2[i]
			if d[s1[i]] != s2[i]:
				return False
		return True
	return False
	
s1 = sys.argv[1]
s2 = sys.argv[2]
print (mapping(s1,s2))