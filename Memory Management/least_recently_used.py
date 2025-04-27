def lru_page_replacement(pages, frame_size):
    frames = []
    page_faults = 0

    print("=== LRU Page Replacement Simulation ===\n")

    for page in pages:
        print(f"Yêu cầu trang: {page}")

        if page in frames:
            frames.remove(page)
            frames.insert(0, page)
            print("→ Trang đã có. Cập nhật thứ tự sử dụng.")
        else:
            page_faults += 1
            if len(frames) < frame_size:
                frames.insert(0, page)
                print("→ Thêm vào khung (còn chỗ).")
            else:
                removed = frames.pop()
                frames.insert(0, page)
                print(f"→ Thay thế trang {removed} bằng {page}.")

        print(f"Khung hiện tại: {frames}\n")

    print("========================================")
    print(f"Tổng số lỗi trang: {page_faults}")


# Ví dụ sử dụng
if __name__ == "__main__":
    reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    frame_size = 4
    lru_page_replacement(reference_string, frame_size)
