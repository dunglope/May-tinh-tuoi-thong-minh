import tkinter as tk

def handle_button_click():
    while True:
        input_text = entry.get()  # Lấy dữ liệu người dùng nhập vào
        if not input_text.isdigit():
            label_result_notdigit.configure(text="Tuổi '{}' là tuổi cc gì?".format(input_text))
            return  # Quay lại yêu cầu người dùng nhập lại
        else:
            number = int(input_text)
            if number > 120:
                label_result_elder.configure(text="Con lạy cụ!! Người âm phủ à?")
            else:
                label_result.configure(text="Tuổi của bạn là {}".format(number))
            break  # Thoát khỏi vòng lặp khi đã có số hợp lệ

def change_language(selected_language):
    if selected_language == "English":
        label_welcome.configure(text="Enter your age")
        button.configure(text="Go!")
        label_result.configure(text="")
        label_result_elder.configure(text="You still alive?")
        label_result_notdigit.configure(text="wtf is {} years old???".format())
        window.title("Smart age calculator")
    elif selected_language == "Vietnamese":
        label_welcome.configure(text="Hãy nhập tuổi của bạn")
        button.configure(text="Tính!")
        label_result.configure(text="")
        window.title("Máy tính tuổi thông minh")

# Tạo một cửa sổ mới
window = tk.Tk()

# Thiết lập các thuộc tính của cửa sổ
window.title("Máy tính tuổi thông minh")
window.geometry("400x200")  # Kích thước cửa sổ (rộng x cao)

# Thêm các thành phần vào cửa sổ
label_welcome = tk.Label(window, text="Hãy nhập tuổi của bạn")
label_welcome.pack()  # Đặt label vào cửa sổ

entry = tk.Entry(window)
entry.pack()  # Đặt ô nhập liệu vào cửa sổ

button = tk.Button(window, text="Tính!", command=handle_button_click)
button.pack()  # Đặt button vào cửa sổ

label_result_notdigit = tk.Label(window, text="")
label_result_notdigit.pack()  # Đặt label kết quả
label_result_elder = tk.Label(window, text="")
label_result_elder.pack()
label_result = tk.Label(window, text="")
label_result.pack()

#*************************UNDER DEVELOPMENT*************************

# Tạo OptionMenu cho việc chọn ngôn ngữ
#language_var = tk.StringVar()
#language_var.set("Vietnamese")  # Ngôn ngữ mặc định

#language_menu = tk.OptionMenu(window, language_var, "Vietnamese", "English", command=lambda value: change_language(value))
#language_menu.pack()

#********************************************************************

entry.bind("<Return>", lambda event: handle_button_click())

# Vòng lặp chính của ứng dụng
window.mainloop()
