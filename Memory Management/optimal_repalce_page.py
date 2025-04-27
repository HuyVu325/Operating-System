def optimal_page_replacement(reference_string, frame_size):
    frames = []
    page_faults = 0

    for ID_PAGE in range(len(reference_string)):
        current_page = reference_string[ID_PAGE]

        if current_page in frames:
            print(f"Trang {current_page} đã có trong khung -> Không lỗi trang.")
            continue

        if len(frames) < frame_size:
            frames.append(current_page)
            page_faults += 1
            print(f"Thêm trang {current_page} vào khung -> Lỗi trang.")
        else:
            future_use = []
            for page in frames:
                if page in reference_string[ID_PAGE+1:]:
                    index = reference_string[ID_PAGE+1:].index(page) + ID_PAGE + 1
                else:
                    index = float('inf')  
                future_use.append(index)

            page_to_replace = future_use.index(max(future_use))
            replaced_page = frames[page_to_replace]
            frames[page_to_replace] = current_page
            page_faults += 1
            print(f"Thay thế trang {replaced_page} bằng {current_page} -> Lỗi trang.")

        print(f"Khung hiện tại: {frames}")

    print("\nTổng số lỗi trang:", page_faults)


# Demo
reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
frame_size = 4

optimal_page_replacement(reference_string, frame_size)
