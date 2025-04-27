def worst_fit(memory_blocks, process_sizes):
    NONE = -1
    NUMBER_OF_BLOCK = len(memory_blocks)
    NUMBER_OF_PROCESS = len(process_sizes)

    block_used = [NONE] * NUMBER_OF_BLOCK
    allocation = [NONE] * NUMBER_OF_PROCESS

    remaining_blocks = memory_blocks.copy()

    for ID_PROCESS in range(NUMBER_OF_PROCESS):
        worst_index = NONE
        for ID_BLOCK in range(NUMBER_OF_BLOCK):
            if block_used[ID_BLOCK] == NONE and remaining_blocks[ID_BLOCK] >= process_sizes[ID_PROCESS]:
                if worst_index == NONE or remaining_blocks[ID_BLOCK] > remaining_blocks[worst_index]:
                    worst_index = ID_BLOCK

        if worst_index != NONE:
            allocation[ID_PROCESS] = worst_index
            block_used[worst_index] = "BUSY"
            remaining_blocks[worst_index] -= process_sizes[ID_PROCESS]

    # In kết quả
    print("Tiến trình | Kích thước | Khối nhớ cấp phát | Dung lượng còn lại")
    for ID_PROCESS in range(NUMBER_OF_PROCESS):
        index = allocation[ID_PROCESS]
        remaining = remaining_blocks[index] if index != NONE else "Không xác định"
        print(f"{ID_PROCESS+1:^10} | {process_sizes[ID_PROCESS]:^10} | {index+1 if index != NONE else 'Không cấp':^17} | {remaining:^18}")

# Ví dụ dữ liệu
memory_blocks = [100, 500, 200, 300, 600]
process_sizes = [212, 417, 112, 426]

worst_fit(memory_blocks, process_sizes)
