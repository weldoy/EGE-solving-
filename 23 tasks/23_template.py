def f(x, y):
    if x > y: return 0
    elif x == y: return 1
    else: pass # сюда пишем какою-то функцию


print(f('первое число', 'второе число'))

# Если вычетание, то x < y == 0
# else : пишем функцию
# не содержит числа -> x>y and x == какое-то число return 0
# содержит число -> f(старт, обяз.число) * f(обяз.число, конец)