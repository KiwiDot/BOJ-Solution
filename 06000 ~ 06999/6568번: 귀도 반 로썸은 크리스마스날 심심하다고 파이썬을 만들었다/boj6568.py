# 백준 6568번 귀도 반 로썸은 크리스마스날 심심하다고 파이썬을 만들었다
c = ["STA", "LDA", "BEQ", "NOP", "DEC", "INC", "JMP", "HLT"]

while True:
    try:
        memory = [input() for i in range(32)]
        PC = value = 0
        end = False

        while not end:
            command, x = c[int(memory[PC][:3], 2)], int(memory[PC][3:], 2)
            PC = (PC + 1) % 32

            match command:
                case "STA":
                    memory[x] = bin(value)[2:].zfill(8)

                case "LDA":
                    value = int(memory[x], 2)

                case "BEQ":
                    if value == 0:
                        PC = x

                case "NOP":
                    pass

                case "DEC":
                    value = (value + 255) % 256

                case "INC":
                    value = (value + 1) % 256

                case "JMP":
                    PC = x

                case "HLT":
                    end = True

        print(bin(value)[2:].zfill(8))

    except EOFError:
        break