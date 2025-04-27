NONE = -1

def best_fit(memory_blocks, process_sizes):
    global NONE
    NUMBER_OF_BLOCK = len(memory_blocks)
    NUMBER_OF_PROCESS = len(process_sizes)

    allocation = [NONE] * NUMBER_OF_PROCESS
    block_used = [NONE] * NUMBER_OF_BLOCK
    remaining_blocks = memory_blocks.copy()  

    for ID_PROCESS in range(NUMBER_OF_PROCESS):
        best_index = NONE

        for ID_BLOCK in range(NUMBER_OF_BLOCK):
            if (block_used[ID_BLOCK] == NONE) and (remaining_blocks[ID_BLOCK] >= process_sizes[ID_PROCESS]):
                if best_index == NONE or remaining_blocks[ID_BLOCK] < remaining_blocks[best_index]:
                    best_index = ID_BLOCK

        if best_index != NONE:
            allocation[ID_PROCESS] = best_index
            block_used[best_index] = "BUSY"
            remaining_blocks[best_index] -= process_sizes[ID_PROCESS]

    # In kết quả
    print("Tiến trình | Kích thước | Khối nhớ cấp phát | Dung lượng còn lại")
    for ID_PROCESS in range(NUMBER_OF_PROCESS):
        index = allocation[ID_PROCESS]
        if index != NONE:
            block_number = index + 1
            remaining = remaining_blocks[index]
        else:
            block_number = "Không cấp"
            remaining = "-"
        print(f"{ID_PROCESS+1:^10} | {process_sizes[ID_PROCESS]:^10} | {block_number:^17} | {str(remaining):^20}")

# Ví dụ dữ liệu
memory_blocks = [100, 500, 200, 300, 600]
process_sizes = [212, 417, 112, 426]

best_fit(memory_blocks, process_sizes)
