from collections import defaultdict

def counting_lfu(pages, capacity):
    cache = set()
    freq_count = defaultdict(int)
    page_faults = 0

    for page in pages:
        print(f"Yêu cầu trang: {page}")
        freq_count[page] += 1

        if page in cache:
            print(f"Trang {page} đã có trong bộ nhớ.")
        else:
            page_faults += 1
            if len(cache) < capacity:
                cache.add(page)
                print(f"Thêm trang {page} vào bộ nhớ.")
            else:
                lfu_page = min(cache, key=lambda p: freq_count[p])
                cache.remove(lfu_page)
                freq_count[lfu_page] = 0 
                print(f"Loại bỏ trang {lfu_page} (sử dụng ít nhất).")
                cache.add(page)
                print(f"Thêm trang {page} vào bộ nhớ.")
        
        print(f"Bộ nhớ hiện tại: {cache}")
        print(f"Tần suất: {dict(freq_count)}\n")

    print(f"Tổng số lần lỗi trang (Page Faults): {page_faults}")
    return page_faults

# Ví dụ chạy
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2,1,2,0,1,7,0,1]
frame_size = 3
counting_lfu(pages, frame_size)
