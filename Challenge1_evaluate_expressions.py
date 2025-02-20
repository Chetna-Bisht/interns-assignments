import re
def evaluate_expression(expression):
    expression = expression.replace('^', '**')
    try:
        return eval(expression, {"__builtins__": None}, {})
    except Exception as e:
        return f"Error: {e}"
def process_expressions(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                expression = line.strip()
                if not expression:
                    continue
                if expression.endswith('='):
                    expression = expression[:-1].strip()
                result = evaluate_expression(expression)
                outfile.write(f"{expression} = {result}\n")
        print(f"Results saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    process_expressions(input_file, output_file)
