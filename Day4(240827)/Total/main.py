# generics_farm


class Farm:
    def __init__(self, kind):
        self.kind = kind

    def __init__(self, kind, amount):
        self.kind = kind
        self.amount = amount

    def __str__(self):
        return f"({self.kind})"


class Fruit:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"({self.name})"


class Vegetable:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"({self.name})"


class Nut:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"({self.name})"


class FarmManager:
    def __init__(self):
        self.FarmList = []

    def addNewKind(self, farm, amount):
        farms = Farm(farm, amount)
        self.FarmList.append(farms)
        print(f"추가됨 : {farms}")

    def removeKind(self, kind):
        for f in self.FarmList:
            if f.kind == kind:
                self.FarmList.remove(kind)
                print(f"삭제됨:{kind}")
                return  # 삭제 후 메서드 종료
        print(f"{kind}을 찾지 못하였습니다.")

    def changeAmount(self, kind, amount):
        for f in self.FarmList:
            if f.kind == kind:
                f.amount = amount
                print(f"변경 완료 :{kind} - {amount}")
                return

    def printFarm(self):
        print("--현재 농장 목록--")
        for f in self.FarmList:
            print(f)

    def buyFarm():
        pass

    def removeFarm(farm):
        pass

    def printBuyFarm():
        pass


if __name__ == "__main__":
    manager = FarmManager()
    manager.addNewKind("사과", 10)
    manager.addNewKind("당근", 5)
    manager.printFarm()  # 농장 목록 출력
    manager.changeAmount("사과", 15)  # 사과의 양 변경
    # manager.removeKind("당근")  # 당근 삭제
    # manager.printFarm()  # 농장 목록 다시 출력
