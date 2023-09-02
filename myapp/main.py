my_ran_string = "This is good"
def return_backwards_string(random_string):
    return "".join(reversed(random_string))



if __name__ == '__main__':
  print(return_backwards_string(my_ran_string))