from collections import deque

def fifo_page_replacement(page_reference, frame_size):
    frames = deque()
    in_memory = set()
    page_faults = 0

    print("Trang truy cập | Khung trang | Ghi chú")
    print("-" * 40)

    for page in page_reference:
        note = ""

        if page not in in_memory:
            page_faults += 1
            note = "Lỗi trang"

            if len(frames) >= frame_size:
                removed = frames.popleft()
                in_memory.remove(removed)

            frames.append(page)
            in_memory.add(page)
        else:
            note = "Đã có"

        # Hiển thị trạng thái khung trang
        frame_state = list(frames)
        while len(frame_state) < frame_size:
            frame_state.append("_")  # Khung trống

        print(f"{page:^14} | {frame_state} | {note}")

    print("\nTổng số lần page fault:", page_faults)

# Ví dụ dữ liệu
page_reference = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_size = 3

fifo_page_replacement(page_reference, frame_size)
