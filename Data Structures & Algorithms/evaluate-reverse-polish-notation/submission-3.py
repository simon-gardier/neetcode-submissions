class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        current_operands = []
        for token in tokens:
            if token == "+":
                current_operands.append(current_operands.pop() + current_operands.pop())

            elif token == "-":
                operand_2 = current_operands.pop()
                operand_1 = current_operands.pop()
                current_operands.append(operand_1 - operand_2)

            elif token == "*":
                current_operands.append(current_operands.pop() * current_operands.pop())

            elif token == "/":
                operand_2 = current_operands.pop()
                operand_1 = current_operands.pop()
                current_operands.append(int(operand_1 / operand_2))

            else:
                current_operands.append(int(token))
    
        return current_operands.pop()
