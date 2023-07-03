import tkinter as tk
import re

def handle_button_click():
    while True:
        input_text = entry.get()  # Lấy dữ liệu người dùng nhập vào
        if not re.match(r'^[0-9]+$', input_text):
            label_result.configure(text="Tuổi '{}' là tuổi cc gì?" .format(input_text))
            return  # Quay lại yêu cầu người dùng nhập lại
        else:
            number = int(input_text)
            if number > 120:
                label_result.configure(text="Con lạy cụ!! Người âm phủ à?")
            else:
                label_result.configure(text="Tuổi của bạn là: " + input_text)
            break  # Thoát khỏi vòng lặp khi đã có số hợp lệ

# Tạo một cửa sổ mới
window = tk.Tk()

# Thiết lập các thuộc tính của cửa sổ
window.title("Máy tính tuổi thông minh")
window.geometry("400x200")  # Kích thước cửa sổ (rộng x cao)

# Thêm các thành phần vào cửa sổ
label_welcome = tk.Label(window, text="Hãy nhập tuổi của bạn")
label_welcome.grid(row=0, column=0, pady=10, sticky="n")  # Đặt label vào cửa sổ

entry = tk.Entry(window)
entry.grid(row=1, column=0, sticky="ew")  # Đặt ô nhập liệu vào cửa sổ

button = tk.Button(window, text="Tính!", command=handle_button_click)
button.grid(row=2, column=0, pady=10, sticky="n")  # Đặt button vào cửa sổ

label_result = tk.Label(window, text="")
label_result.grid(row=3, column=0, pady=10, sticky="n") # Đặt label kết quả

# Căn chỉnh ra giữa cửa sổ
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

entry.bind("<Return>", lambda event: handle_button_click())

# Vòng lặp chính của ứng dụng
window.mainloop()
