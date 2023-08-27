#
# (INPUT)---> (NEURON) ---> (OUTPUT)
#
import random

inputs = [5]
weight = 1
bias = 0


class Neuron:
    def __init__(self) -> None:
        self.bias = random.random()
        self.weight = random.random()
        self.output = 0
    
    def relu(self, x):
        return max(0, x)

    def forward(self, inputs):
        # weighted sum and bias
        self.output = inputs * self.weight + self.bias
        # activation function
        self.output = self.relu(self.output)
        return self.output
    
def mean_squared_error(predicted, target):
    return (predicted - target)**2
neuron = Neuron()


inputs = [1, 2, 3, 4, 5]
targets = [i for i in inputs]  # Corresponding target values for regression



learning_rate = 0.1
for i in range(100):
    for i in range(len(inputs)):
        input('step')
        input_value = inputs[i]
        target_value = targets[i]
        
        output = neuron.forward(input_value)
        loss = mean_squared_error(output, target_value)
        
        # Backpropagation (backward pass)
        gradient_output = 2 * (output - target_value)
        print('gradient output:', gradient_output)

        gradient_weight = gradient_output * input_value
        print('gradient weight', gradient_weight) 
        gradient_bias = gradient_output

        print('gradient bias', gradient_bias) 
        
        # Update parameters
        neuron.weight -= learning_rate * gradient_weight
        print(learning_rate * gradient_weight)
        neuron.bias -= learning_rate * gradient_bias
        print(learning_rate * gradient_bias)
        print(f"Input: {input_value:.2f}, Output: {output:.2f}, Target: {target_value:.2f}, Loss: {loss:.4f}, Weight: {neuron.weight}, Bias: {neuron.bias}")

for i in range(10):
    neuron.forward(i)
    print(i, neuron.output)