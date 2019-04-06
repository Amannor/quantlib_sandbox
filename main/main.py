import csv 
import geometricBrownianMotion

def main():
	results_list = list()
	n = 100
	estimated_stock_sum = estimated_call_sum = estimated_put_sum = 0

	for i in range(n):
		print(f"seed{i} start")
		estimated_stock_price, estimated_call_price, estimated_put_price = geometricBrownianMotion.calc_prices(i)
		
		estimated_stock_sum += estimated_stock_price
		estimated_call_sum += estimated_call_price
		estimated_put_sum += estimated_put_price
		
		results_list.append(tuple((i, estimated_stock_price, estimated_call_price, estimated_put_price)))
		print(f"seed{i} end")

	# print(f"results_list {results_list}")
	print(f"estimated_stock_price_avg {estimated_stock_sum/float(n)}")
	print(f"estimated_call_price_avg {estimated_call_sum/float(n)}")
	print(f"estimated_put_price_avg {estimated_put_sum/float(n)}")


	# Todo: write to a csv file, use the following as refernce:
	# with open('results_list.csv','wb') as out:
	# 	csv_out=csv.writer(out)
	# 	csv_out.writerow(['seed','avg_estimated_stock_price', 'avg_estimated_call_price', 'avg_estimated_put_price'])
	# 	for row in data:
	# 		csv_out.writerow(row)


if __name__ == '__main__':
    main()