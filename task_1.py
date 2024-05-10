def task_1(number: int) -> dict:
  return {'oct': oct(number), 'hex': hex(number)}


for _ in range(30):
  print(f"Представление числа {_} в восьмеричной системе счисления: {task_1(_)['oct']}, представление числа {_} в шестнадцатеричной системе счисления: {task_1(_)['hex']}.")