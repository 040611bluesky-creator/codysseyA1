CATEGORIES = [
    "텍스트 생성",
    "이미지 생성",
    "영상 생성",
    "페르소나",
    "자동화",
    "기타",
]

prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "다음 주제와 핵심 키워드로 초보자가 읽기 쉬운 블로그 글을 작성해 주세요.\n주제: {topic}\n키워드: {keywords}",
        "category": "텍스트 생성",
        "favorite": True,
    },
    {
        "title": "이미지 프롬프트 다듬기",
        "content": "아래 설명을 이미지 생성 AI에 넣기 좋은 영어 프롬프트로 바꿔 주세요. 구도, 조명, 스타일을 구체적으로 포함하세요.\n설명: {description}",
        "category": "이미지 생성",
        "favorite": False,
    },
    {
        "title": "파이썬 튜터 페르소나",
        "content": "당신은 친절한 파이썬 튜터입니다. 어려운 용어는 쉬운 말로 바꾸고, 짧은 코드 예시를 함께 들어 설명하세요.",
        "category": "페르소나",
        "favorite": True,
    },
]


def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


def input_not_empty(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print("입력값이 비어 있습니다. 다시 입력해 주세요.")


def choose_category():
    print("카테고리:")
    for index, name in enumerate(CATEGORIES, start=1):
        print(f"{index}. {name}")
    print("번호를 선택하거나 카테고리 이름을 직접 입력하세요.")

    while True:
        choice = input("카테고리: ").strip()
        if not choice:
            print("입력값이 비어 있습니다. 다시 입력해 주세요.")
            continue
        if choice.isdigit():
            number = int(choice)
            if 1 <= number <= len(CATEGORIES):
                return CATEGORIES[number - 1]
            print("목록에 있는 번호를 선택하거나 이름을 직접 입력해 주세요.")
            continue
        return choice


def add_prompt():
    print("\n[프롬프트 추가]")
    title = input_not_empty("제목: ")
    content = input_not_empty("내용: ")
    category = choose_category()

    prompts.append(
        {
            "title": title,
            "content": content,
            "category": category,
            "favorite": False,
        }
    )
    print("프롬프트가 추가되었습니다.")


def show_list():
    print("\n[프롬프트 목록]")
    if not prompts:
        print("저장된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompts, start=1):
        star = " ⭐" if prompt["favorite"] else ""
        print(f"{index}. [{prompt['category']}] {prompt['title']}{star}")


def show_by_category():
    print("준비 중입니다")


def search_prompt():
    print("준비 중입니다")


def show_detail():
    print("준비 중입니다")


def toggle_favorite():
    print("준비 중입니다")


def show_favorites():
    print("준비 중입니다")


def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            toggle_favorite()
        elif choice == "7":
            show_favorites()
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 번호입니다. 다시 선택해 주세요.")


if __name__ == "__main__":
    main()
