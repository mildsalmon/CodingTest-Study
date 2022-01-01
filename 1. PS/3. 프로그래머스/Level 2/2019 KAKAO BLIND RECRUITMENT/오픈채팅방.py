def msg(admin_chat) -> str:
    global uid_to_name

    action, uid = admin_chat

    if action == "Enter":
        return f"{uid_to_name[uid]}님이 들어왔습니다."
    elif action == "Leave":
        return f"{uid_to_name[uid]}님이 나갔습니다."


def solution(record) -> list:
    global uid_to_name

    admin_chat: list = []
    uid_to_name: dict = {}
    
    for i, row in enumerate(record):
        temp: list = row.split()

        if temp[0] != "Leave":
            uid_to_name[temp[1]] = temp[2]

        if temp[0] != "Change":
            admin_chat.append((temp[0], temp[1]))

    answer: list = list(map(msg, admin_chat))

    return answer

if __name__ == "__main__":
    solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])