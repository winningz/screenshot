import os
import tkinter as tk
from tkinter import ttk
from PIL import ImageGrab
import time


# 전역 변수
bbox = None  # 캡처 영역 초기값
file_format = "png"  # 기본 저장 형식
is_dark_mode = False  # 다크 모드 상태

def save_text(text_widget):
    text_content = text_widget.get("1.0", tk.END).strip()
    if not text_content:
        print("텍스트 박스에 내용이 없습니다.")
        return

    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    filename = f"note{curr_time}.txt"
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text_content)
        print(f"텍스트 저장 완료: {filename}")
    except Exception as e:
        print(f"텍스트 저장 실패: {e}")

def screenshot():
    global bbox
    if bbox is None:
        print("캡처 영역이 설정되지 않았습니다.")
        return

    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    filename = f"image{curr_time}.png"
    try:
        img = ImageGrab.grab(bbox=bbox)
        img.save(filename)
        print(f"스크린샷 저장 완료: {filename}")
    except Exception as e:
        print(f"스크린샷 저장 실패: {e}")

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
        selection_window.destroy()  # 선택 창 닫기

    # 새 창 생성
    selection_window = tk.Toplevel()
    selection_window.attributes("-fullscreen", True)  # 전체 화면 활성화
    selection_window.attributes("-alpha", 0.3)  # 투명도 설정
    selection_window.attributes("-topmost", True)  # 최상위 창 설정
    selection_window.config(cursor="cross")

    # 캔버스 생성
    canvas = tk.Canvas(selection_window, bg="black", highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.bind("<ButtonPress-1>", on_button_press)  # 마우스 좌클릭 시작
    canvas.bind("<B1-Motion>", on_button_drag)  # 마우스 드래그 중
    canvas.bind("<ButtonRelease-1>", on_button_release)  # 마우스 좌클릭 종료

# 텍스트 저장
def save_text(text_widget):
    text_content = text_widget.get("1.0", tk.END).strip()
    if not text_content:
        print("텍스트 박스에 내용이 없습니다.")
        return

    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    filename = f"note{curr_time}.txt"
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text_content)
        print(f"텍스트 저장 완료: {filename}")
    except Exception as e:
        print(f"텍스트 저장 실패: {e}")

# 파일 형식 설정
def set_file_format(format_var):
    global file_format
    file_format = format_var.get()
    print(f"저장 형식 설정 완료: {file_format}")

# 다크 모드 토글
def toggle_dark_mode(root, widgets):
    global is_dark_mode
    is_dark_mode = not is_dark_mode

    bg_color = "#2e2e2e" if is_dark_mode else "#f0f0f0"
    fg_color = "white" if is_dark_mode else "black"
    text_bg = "#3e3e3e" if is_dark_mode else "white"
    text_fg = "white" if is_dark_mode else "black"

    root.config(bg=bg_color)
    for widget in widgets:
        if isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
            widget.config(bg=bg_color, fg=fg_color)
        elif isinstance(widget, tk.Text):
            widget.config(bg=text_bg, fg=text_fg)

# PageDown 단축키 캡처
def shortcut_screenshot(event):
    screenshot()

# Tkinter 창 생성
def main():
    global file_format

    root = tk.Tk()
    root.title("스크린샷 프로그램")
    root.geometry("400x450")
    widgets = []  # 위젯 목록

    # 캡처 영역 선택 버튼
    btn_select_area = tk.Button(root, text="1. 캡처 영역 선택", command=select_area, font=("Arial", 12))
    btn_select_area.pack(pady=10)
    widgets.append(btn_select_area)

    # 파일 형식 설정 (드롭박스)
    frame_format = tk.Frame(root)
    frame_format.pack(pady=10)
    frame_format.config(bg="#f0f0f0")
    widgets.append(frame_format)

    lbl_format = tk.Label(frame_format, text="2. 파일 형식 설정:", font=("Arial", 12))
    lbl_format.pack(side="left", padx=5)
    widgets.append(lbl_format)

    format_var = tk.StringVar(value="png")
    format_dropdown = ttk.Combobox(frame_format, textvariable=format_var, state="readonly", values=["png", "jpg", "bmp"], font=("Arial", 10))
    format_dropdown.pack(side="left")
    format_dropdown.bind("<<ComboboxSelected>>", lambda event: set_file_format(format_var))

    # 스크린샷 저장 버튼
    btn_screenshot = tk.Button(root, text="3. 스크린샷 저장", command=screenshot, font=("Arial", 12))
    btn_screenshot.pack(pady=10)
    widgets.append(btn_screenshot)

    # 텍스트 박스 추가
    lbl_textbox = tk.Label(root, text="4. 자유 메모 공간:", font=("Arial", 12))
    lbl_textbox.pack(pady=5)
    widgets.append(lbl_textbox)

    text_box = tk.Text(root, height=8, width=50, font=("Consolas", 12), wrap="word", bd=2, relief="solid")
    text_box.pack(pady=10, padx=10)

    widgets.append(text_box)

    # 텍스트 저장 버튼
    btn_save_text = tk.Button(root, text="텍스트 저장", command=lambda: save_text(text_box), font=("Arial", 12))
    btn_save_text.pack(pady=10)
    widgets.append(btn_save_text)

    # 다크 모드 토글 버튼
    btn_toggle_dark = tk.Button(root, text="다크 모드 전환", command=lambda: toggle_dark_mode(root, widgets), font=("Arial", 12))
    btn_toggle_dark.pack(pady=10)
    widgets.append(btn_toggle_dark)

    # PageDown 단축키 등록
    root.bind("<Next>", shortcut_screenshot)

    root.mainloop()

if __name__ == "__main__":
    main()