def run():
  my_list = [1, "Hello", True, 4.5]
  my_dict = {"fristname" : "Facundo", "lastname": "garcia"}

  super_list = [
    {"fristname" : "Facundo", "lastname": "garcia"},
    {"fristname" : "Luisa", "lastname": "alvarez"},
    {"fristname" : "Sebastian", "lastname": "Moreno"},
    {"fristname" : "Son", "lastname": "goku"},
    {"fristname" : "Son", "lastname": "Gohan"}
  ]

  super_dict = {
    "natural_nums": [1,2,3,4,5],
    "integer_nums": [-1,-2,0,1,2],
    "floating_nums": [1.1, 2.5, 6.65]
  }

  for key, value in super_dict.items():
    print(key, "-", value)

if __name__ == '__main__':
  run()