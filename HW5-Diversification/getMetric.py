import sys

if __name__ == '__main__':
	file = sys.argv[1]
	map = {'P_IA@10': -1, 'P_IA@20': -1, 'alpha-NDCG@20': -1}
	with open(file, 'r') as f:
		lines = f.readlines()
		for line in lines:
			line = line.strip().split(',')
			