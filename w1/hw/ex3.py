import math
import random


def exercise3(num_sample, loss_name):
    if not num_sample.isnumeric():
        print("Number of sample must be int")
        return
    num_sample = int(num_sample)
    if not loss_name in ("MAE", "MSE", "RMSE"):
        print(f"{loss_name} is not supported")
        return
    if loss_name == "MAE":
        sum_MAE = 0
        for i in range(num_sample):
            y_predict = random.uniform(0, 10)
            y_target = random.uniform(0, 10)
            loss = math.fabs(y_target - y_predict)
            print(f"""loss name: {loss_name}
                      sample: {i}
                      predict: {y_predict}
                      target: {y_target}
                      loss: {loss}                                        
""")
            sum_MAE += loss
        print(f"final MAE = {sum_MAE / num_sample}")
    elif loss_name == "MSE":
        sum_MSE = 0
        for i in range(num_sample):
            y_predict = random.uniform(0, 10)
            y_target = random.uniform(0, 10)
            loss = math.pow(y_predict - y_target, 2)
            print(f"""loss name: {loss_name}
                      sample: {i}
                      predict: {y_predict}
                      target: {y_target}
                      loss: {loss}                                        
""")
            sum_MSE += loss
        print(f"Final MSE = {sum_MSE / num_sample}")
    elif loss_name == "RMSE":
        sum_MSE = 0
        for i in range(num_sample):
            y_predict = random.uniform(0, 10)
            y_target = random.uniform(0, 10)
            loss = math.pow(y_predict - y_target, 2)
            print(f"""loss name: {loss_name}
                      sample: {i}
                      predict: {y_predict}
                      target: {y_target}
                      loss: {loss}                                        
""")
            sum_MSE += loss
        print(f"final RMSE = {math.sqrt(sum_MSE/num_sample)}")


n = input("Input number of sample: ")
loss_name = input("Input of loss name: ")
exercise3(n, loss_name)
