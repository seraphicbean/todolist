import os

# 데이터 파일 이름
TODO_FILE = "todo_list.txt"

def load_todo_list():
    """파일에서 할 일 목록을 읽어옵니다."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_todo_list(todo_list):
    """할 일 목록을 파일에 저장합니다."""
    with open(TODO_FILE, "w", encoding="utf-8") as file:
        for todo in todo_list:
            file.write(f"{todo}\n")

def show_menu():
    """메뉴를 출력합니다."""
    print("\nTo-Do List 관리 프로그램")
    print("1. 할 일 추가")
    print("2. 할 일 삭제")
    print("3. 할 일 목록 보기")
    print("4. 프로그램 종료")

def add_todo(todo_list):
    """새로운 할 일을 추가합니다."""
    todo = input("추가할 할 일을 입력하세요: ")
    todo_list.append(todo)
    save_todo_list(todo_list)
    print(f"'{todo}'가 목록에 추가되었습니다.")

def delete_todo(todo_list):
    """할 일을 삭제합니다."""
    show_todo_list(todo_list)
    try:
        index = int(input("삭제할 할 일의 번호를 입력하세요: ")) - 1
        if 0 <= index < len(todo_list):
            deleted_todo = todo_list.pop(index)
            save_todo_list(todo_list)
            print(f"'{deleted_todo}'가 삭제되었습니다.")
        else:
            print("유효하지 않은 번호입니다.")
    except ValueError:
        print("잘못된 입력입니다. 숫자를 입력하세요.")

def show_todo_list(todo_list):
    if todo_list:
        print("\n할 일 목록:")
        for i, todo in enumerate(todo_list, 1):
            print(f"{i}. {todo}")
    else:
        print("할 일이 없습니다.")

def main():
    """메인 프로그램 루프입니다."""
    todo_list = load_todo_list()

    while True:
        show_menu()
        choice = input("원하는 작업을 선택하세요 (1/2/3/4): ")

        if choice == '1':
            add_todo(todo_list)
        elif choice == '2':
            delete_todo(todo_list)
        elif choice == '3':
            show_todo_list(todo_list)
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main()
