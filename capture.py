import tkinter as tk

bbox = None  # 캡처 영역 초기값

# GUI로 영역 설정
def select_area():
    global bbox

    start_x, start_y = 0, 0

    def on_button_press(event):
        nonlocal start_x, start_y
        start_x, start_y = event.x, event.y
        canvas.delete("selection")  # 기존 선택 영역 제거

    def on_button_drag(event):
        nonlocal start_x, start_y
        canvas.delete("selection")
        canvas.create_rectangle(start_x, start_y, event.x, event.y, outline="red", width=2, tag="selection")

    def on_button_release(event):
        nonlocal start_x, start_y
        global bbox
        end_x, end_y = event.x, event.y
        bbox = (min(start_x, end_x), min(start_y, end_y), max(start_x, end_x), max(start_y, end_y))
        print(f"캡처 영역: {bbox}")
        selection_window.destroy()

    selection_window = tk.Toplevel()
    selection_window.attributes("-fullscreen", True)
    selection_window.config(cursor="cross")

    canvas = tk.Canvas(selection_window, bg="black", highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.bind("<ButtonPress-1>", on_button_press)
    canvas.bind("<B1-Motion>", on_button_drag)
    canvas.bind("<ButtonRelease-1>", on_button_release)

# Tkinter 창 생성
def main():
    root = tk.Tk()
    root.title("스크린샷 프로그램")
    root.geometry("400x450")

    # 캡처 영역 선택 버튼
    btn_select_area = tk.Button(root, text="1. 캡처 영역 선택", command=select_area, font=("Arial", 12))
    btn_select_area.pack(pady=10)

    # 텍스트 박스 추가
    lbl_textbox = tk.Label(root, text="2. 자유 메모 공간:", font=("Arial", 12))
    lbl_textbox.pack(pady=5)

    text_box = tk.Text(root, height=8, width=50, font=("Consolas", 12), wrap="word", bd=2, relief="solid")
    text_box.pack(pady=10, padx=10)

    root.mainloop()

if __name__ == "__main__":
    main()