"""!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""
# Pentru această temă pentru acasă, nu este necesar să rezolvi toate exercițiile.
# Poți alege să lucrezi doar:

# la primele două
# sau
# doar la ultimul exercițiu,

# în funcție de preferințele și timpul disponibil.
"""!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""



"""
Task: Creați o funcție cu numele `temp_converter` care returnează două funcții interne:
- `to_fahrenheit(celsius)`: convertește temperatura din Celsius în Fahrenheit
- `to_celsius(fahrenheit)`: convertește temperatura din Fahrenheit în Celsius

Exemplu de utilizare:
to_f, to_c = temp_converter()
fahrenheit = to_f(20) # returnează 68.0
"""
# CODUL TĂU VINE MAI JOS:
def temp_converter():
    def to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32

    def to_celsius(fahrenheit):
        return (fahrenheit - 32)*(5/9)

    return to_fahrenheit, to_celsius

to_f, to_c = temp_converter()
fahrenheit = to_f(20)
print(fahrenheit)
# CODUL TĂU VINE MAI SUS:


"""
Task: Creați o funcție cu numele `fibonacci_generator` care returnează două funcții interne:
- `fib_until(limit)`: returnează secvența Fibonacci până la un anumit număr `limit`
- `fib_n_terms(n)`: returnează primele `n` termeni ai secvenței Fibonacci

Exemplu de utilizare:
fib_until, fib_n_terms = fibonacci_generator()
fib_until(20)  # returnează secvența Fibonacci până la 20
fib_n_terms(5)  # returnează primii 5 termeni ai secvenței Fibonacci
"""
# CODUL TĂU VINE MAI JOS:
def fibonacci_generator():
    fib_list = [0, 1]
    def fib_until(limit):
        if limit <= 0:
            return []
        elif limit == 1:
            return [0]
        else:
            while len(fib_list) < limit:
                next_fib = fib_list[-1] + fib_list[-2]
                fib_list.append(next_fib)
            return fib_list
    def fib_n_terms(n):
        return fib_list[:n:]
    return fib_until, fib_n_terms

fib_until, fib_n_terms = fibonacci_generator()
print(fib_until(20))
print(fib_n_terms(5))
# CODUL TĂU VINE MAI SUS:


"""
Task: Creați o funcție cu numele `create_bank_account` care va returna un dicționar 
cu funcțiile interne:
- `deposit(amount)`: adaugă o sumă la soldul contului
- `withdraw(amount)`: retrage o sumă din cont dacă există suficient fond
- `balance()`: returnează soldul curent al contului
- `history()`: returnează istoricul tranzacțiilor

Exemplu de utilizare:
cont = create_bank_account(1000)
cont["deposit"](500)
print(cont["balance"]())  # 1500
"""
# CODUL TĂU VINE MAI JOS:
def create_bank_account(amount=0):
    total_balance = amount
    history_of_transactions = []

    def deposit(amount):
        nonlocal total_balance
        if amount > 0:
            total_balance += amount
            history_of_transactions.append(f"deposit:+{amount}")
        else:
            history_of_transactions.append(f"deposit:Insuf funds")

    def withdraw(amount):
        nonlocal total_balance
        if amount > total_balance and amount>0:
            history_of_transactions.append(f"withdraw:Insuf funds")
        else:
            total_balance -= amount
            history_of_transactions.append(f"withdraw:-{amount}")

    def balance():
        return total_balance

    def history():
        return history_of_transactions.copy()

    return {
        "deposit": deposit,
        "withdraw": withdraw,
        "balance": balance,
        "history": history,
    }

cont = create_bank_account(1000)
cont["deposit"](500)
print(cont["balance"]())  # 1500
print(cont["history"]())
# CODUL TĂU VINE MAI SUS:




