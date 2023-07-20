def solution(n):
    output = [1]
    for i in range(2, n + 1):
        output.append(output[-1] + i)
    return output

def generate_output(input_num):
    if input_num <= 0:
        return "Input harus lebih besar dari 0."
    result = solution(input_num)
    return "-".join(str(x) for x in result)

if __name__ == "__main__":
    input_num = int(input("Masukkan angka untuk menghasilkan output: "))
    output_str = generate_output(input_num)
    print(f"Output: {output_str}")
