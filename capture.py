import tkinter as tk

# Tkinter 창 생성
def main():
    root = tk.Tk()
    root.title("스크린샷 프로그램")
    root.geometry("400x450")

    # 캡처 영역 선택 버튼
    btn_select_area = tk.Button(root, text="1. 캡처 영역 선택", font=("Arial", 12))
    btn_select_area.pack(pady=10)

    # 텍스트 박스 추가
    lbl_textbox = tk.Label(root, text="2. 자유 메모 공간:", font=("Arial", 12))
    lbl_textbox.pack(pady=5)

    text_box = tk.Text(root, height=8, width=50, font=("Consolas", 12), wrap="word", bd=2, relief="solid")
    text_box.pack(pady=10, padx=10)

    root.mainloop()

if __name__ == "__main__":
    main()