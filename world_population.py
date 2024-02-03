import matplotlib.pyplot as plt
import numpy as np
import csv


PATH = "./world_population.csv"


def main(_filter):
	data = get_world_population(_filter)
	countries = list(data.keys())
	percentages = list(data.values())

	radius = np.abs(percentages) * 50
	num_data = len(countries)

	plt.scatter(
		np.arange(num_data) + 10 * np.random.randn(num_data),
		countries,
		c=np.random.randint(0, 50, num_data),
		s=radius
	)
	plt.show()


def get_world_population(_filter=None):
	with open(PATH, 'r') as file:
		reader = csv.DictReader(file, delimiter=',')
		return {
			row["Country/Territory"]: float(row["World Population Percentage"])
			for row in reader
			if filter_data(row, _filter)
		}


def filter_data(row, _filter):
	if _filter in ["north america", "south america", "asia", "africa", "europe", "oceania"]:
		return row["Continent"].lower() == _filter
	elif isinstance(_filter, float):
		return float(row["World Population Percentage"]) >= _filter
	elif _filter is None:
		return True
	return False


if __name__ == '__main__':
	try:
		print("Type a minimal percentage or a continent to filter the data :3")
		print("Continents: North America, South America, Asia, Africa, Europe, Oceania")
		data_filter = input("=> ").lower()
		data_filter = float(data_filter)
	except ValueError:
		pass
	finally:
		if data_filter == "":
			data_filter = None
		main(data_filter)
