# Set the runtime to cpu or gpu.
runtime = "gpu"  # OR "cpu"

if runtime == "cpu":
    runtimeFlag = "cpu"
elif runtime == "gpu":
    runtimeFlag = "cuda:0"
else:
    print("Invalid runtime. Please set it to either 'cpu' or 'gpu'.")
    runtimeFlag = None

print("Runtime flag is:", runtimeFlag)
